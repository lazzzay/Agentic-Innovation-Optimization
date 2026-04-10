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

    LLMs sometimes wrap JSON in ```json ... ``` blocks, or add text before/after.
    This function robustly extracts the JSON content.
    """
    text = text.strip()

    # Case 1: Markdown code block (```json ... ``` or ``` ... ```)
    code_block = re.search(r"```(?:json)?\s*\n?(.*?)```", text, re.DOTALL)
    if code_block:
        return code_block.group(1).strip()

    # Case 2: Already starts with { or [ — likely raw JSON
    if text.startswith(("{", "[")):
        return text

    # Case 3: JSON embedded in text — find the outermost { } or [ ]
    # Check [ before { so that arrays are matched as whole arrays, not inner objects
    for start_char, end_char in [("[", "]"), ("{", "}")]:
        start = text.find(start_char)
        if start == -1:
            continue
        # Find the matching closing bracket
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

    # Nothing worked — return as-is and let the caller handle the error
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
