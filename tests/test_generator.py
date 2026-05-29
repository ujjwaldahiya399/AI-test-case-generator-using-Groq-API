
import os
import pytest

def test_api_key_exists():
    assert os.environ.get("GROQ_API_KEY") is not None, "GROQ_API_KEY not set"

def test_requirement_file_exists():
    assert os.path.exists("sample_requirement.txt"), "sample_requirement.txt not found"

def test_groq_importable():
    import groq
    assert groq is not None
