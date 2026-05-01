"""Shared utilities — JSON parsing, retry logic, common helpers."""

from __future__ import annotations

import json
import logging
import re

logger = logging.getLogger(__name__)


class LLMOutputParseError(Exception):
    """Raised when LLM output cannot be parsed as valid JSON."""

    def __init__(self, raw_text: str, expected_schema: str = ""):
        self.raw_text = raw_text
        self.expected_schema = expected_schema
        super().__init__(
            f"Failed to parse LLM output as JSON. "
            f"Raw text (first 200 chars): {raw_text[:200]}"
        )


def extract_json(text: str) -> str:
    """Extract JSON from LLM output, handling markdown code blocks and preamble.

    LLMs differ in how they wrap structured outputs:
      - Anthropic typically returns raw JSON.
      - Gemini and others often wrap it in ```json ... ``` fences, sometimes
        with surrounding prose, sometimes without a closing fence (truncation).
      - Some prepend prose like "Here is the result:\\n```json\\n{...}".

    The strategy is: peel off any leading/trailing markdown fences, then either
    return the result if it already starts with a JSON token, or fall through
    to bracket-matched scan that picks the outermost balanced object/array.
    """
    text = text.strip()

    # If the text begins with a markdown fence, strip both the leading fence
    # and any matching trailing fence (plus any prose after it). We only do
    # this when the fence is at the very start, otherwise a stray ``` mid-text
    # would over-strip into the JSON region.
    if text.startswith("```"):
        text = re.sub(r"^```[ \t]*(?:json|JSON)?[ \t]*\n?", "", text)
        text = re.sub(r"\n?[ \t]*```.*\Z", "", text, flags=re.DOTALL)
        text = text.strip()

    # Already JSON.
    if text.startswith(("{", "[")):
        return text

    # JSON embedded in prose — pick the first occurring opener and
    # bracket-match it. Sorting by position handles array-with-preamble
    # vs. nested-object cases without a fixed precedence.
    candidates: list[tuple[int, str, str]] = []
    obj_pos = text.find("{")
    arr_pos = text.find("[")
    if obj_pos != -1:
        candidates.append((obj_pos, "{", "}"))
    if arr_pos != -1:
        candidates.append((arr_pos, "[", "]"))
    candidates.sort(key=lambda c: c[0])

    for start, start_char, end_char in candidates:
        depth = 0
        in_string = False
        escape_next = False
        for i, char in enumerate(text[start:], start):
            if escape_next:
                escape_next = False
                continue
            if char == "\\":
                escape_next = True
                continue
            if char == '"':
                in_string = not in_string
                continue
            if in_string:
                continue
            if char == start_char:
                depth += 1
            elif char == end_char:
                depth -= 1
                if depth == 0:
                    return text[start : i + 1]

    # Nothing worked — return as-is and let the caller raise.
    return text


def parse_json_output(raw_text: str, context: str = "") -> dict | list:
    """Parse LLM output as JSON with robust error handling.

    Args:
        raw_text: Raw text from the LLM response
        context: Description of what was expected (for error messages)

    Returns:
        Parsed JSON as dict or list

    Raises:
        LLMOutputParseError: If parsing fails after all attempts
    """
    # Handle LangChain content format (can be list of content blocks)
    if isinstance(raw_text, list):
        raw_text = raw_text[0].get("text", "") if raw_text else ""

    text = str(raw_text).strip()
    if not text:
        raise LLMOutputParseError(text, context)

    extracted = extract_json(text)

    try:
        return json.loads(extracted)
    except json.JSONDecodeError as e:
        logger.warning("JSON parse failed for %s: %s", context, e)
        raise LLMOutputParseError(text, context) from e
