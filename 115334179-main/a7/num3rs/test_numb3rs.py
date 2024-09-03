import pytest
from numb3rs import validate

def test_random():
    assert validate("255.255.0.0") == True
    assert validate("cat.6.6.6") == False
    assert validate("-1.3.999") == False
    assert validate("999.3.4.5") == False
    assert validate("260.3.4.5") == False
    assert validate("256.256.256.256") == False
    assert validate("192.168.1.1.") == False
    assert validate("123.456.789.0") == False
    assert validate("12.34.56.78.90") == False
    assert validate("abcd.efgh.ijkl.mnop") == False
    assert validate("192.168.-1.1") == False
    assert validate("192.168.1") == False
    assert validate("192.168.1.1.") == False
