import pytest
from plates import is_valid

def test_random():
    assert is_valid("00ejd") == False
    assert is_valid("a") == False
    assert is_valid("abcdefg") == False
    assert is_valid("abc22a") == False
    assert is_valid("abcd12") == True
    assert is_valid("abc d") == False
    assert is_valid("a345") == False
    assert is_valid("abc013") == False

