import pytest
from fuel import convert
from fuel import gauge

def test_convert():
    assert convert("99/100") == 99
    assert convert("2/3") == 67

    with pytest.raises(ZeroDivisionError):
        convert("3/0")

    with pytest.raises(ValueError):
        convert("cat/dog")

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(75) == "75%"
