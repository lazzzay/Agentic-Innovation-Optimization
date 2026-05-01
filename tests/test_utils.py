"""Tests for JSON parsing utilities."""

import pytest

from aip.utils import LLMOutputParseError, extract_json, parse_json_output


class TestExtractJson:
    def test_raw_json_object(self):
        assert extract_json('{"key": "value"}') == '{"key": "value"}'

    def test_raw_json_array(self):
        assert extract_json('[1, 2, 3]') == '[1, 2, 3]'

    def test_markdown_code_block(self):
        text = '```json\n{"key": "value"}\n```'
        assert extract_json(text) == '{"key": "value"}'

    def test_markdown_code_block_no_language(self):
        text = '```\n{"key": "value"}\n```'
        assert extract_json(text) == '{"key": "value"}'

    def test_json_with_preamble(self):
        text = 'Here is the result:\n{"key": "value"}'
        assert extract_json(text) == '{"key": "value"}'

    def test_json_with_surrounding_text(self):
        text = 'The analysis is:\n{"score": 42}\nThat is the result.'
        assert extract_json(text) == '{"score": 42}'

    def test_nested_json(self):
        text = '{"outer": {"inner": [1, 2]}}'
        assert extract_json(text) == '{"outer": {"inner": [1, 2]}}'

    def test_whitespace_handling(self):
        text = '  \n  {"key": "value"}  \n  '
        assert extract_json(text) == '{"key": "value"}'

    def test_array_with_preamble(self):
        text = 'Here are the signals:\n[{"topic": "x"}]'
        assert extract_json(text) == '[{"topic": "x"}]'

    def test_markdown_fence_without_closing(self):
        # Gemini sometimes emits a leading ```json fence but no closing fence
        # (truncation, format drift). The extractor must still recover the JSON.
        text = '```json\n{"key": "value", "nested": {"a": 1}}'
        assert extract_json(text) == '{"key": "value", "nested": {"a": 1}}'

    def test_markdown_fence_with_trailing_prose(self):
        # Some providers append explanatory prose after the closing fence.
        text = '```json\n{"key": "value"}\n```\nHope this helps!'
        assert extract_json(text) == '{"key": "value"}'

    def test_uppercase_json_language_tag(self):
        text = '```JSON\n{"key": "value"}\n```'
        assert extract_json(text) == '{"key": "value"}'

    def test_markdown_fence_with_leading_prose_and_no_closing(self):
        # Worst-case Gemini format: leading prose, opening fence, no closing.
        text = 'Here is the JSON:\n```json\n{"key": "value"}'
        assert extract_json(text) == '{"key": "value"}'


class TestParseJsonOutput:
    def test_valid_json(self):
        result = parse_json_output('{"key": "value"}')
        assert result == {"key": "value"}

    def test_json_in_code_block(self):
        result = parse_json_output('```json\n{"key": 1}\n```')
        assert result == {"key": 1}

    def test_empty_raises(self):
        with pytest.raises(LLMOutputParseError):
            parse_json_output("")

    def test_invalid_json_raises(self):
        with pytest.raises(LLMOutputParseError):
            parse_json_output("this is not json at all")

    def test_list_content_format(self):
        result = parse_json_output([{"text": '{"key": "value"}'}])
        assert result == {"key": "value"}

    def test_empty_list_raises(self):
        with pytest.raises(LLMOutputParseError):
            parse_json_output([])
