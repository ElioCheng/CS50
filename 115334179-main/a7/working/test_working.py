import pytest
from working import convert

def test_random():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"


def test_edgecases():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("11:59 PM to 12:00 AM") == "23:59 to 00:00"


def test_invalid_formats():
    with pytest.raises(ValueError):
        convert("25 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("9:61 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("9 AM to 5 XYZ")
    with pytest.raises(ValueError):
        convert("9 AM to")
    with pytest.raises(ValueError):
        convert("9:00 AM 5:00 PM")

def test_missing_values():
    with pytest.raises(ValueError):
        convert("9 AM to 5")
    with pytest.raises(ValueError):
        convert("9 to 5 PM")

        
