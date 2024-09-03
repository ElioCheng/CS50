import pytest
from twttr import shorten

def test_random():
    assert shorten("Hello! Good morning!") == "Hll! Gd mrnng!"
    assert shorten("CS50") == "CS50"
    assert shorten("AEIOU") == ""
