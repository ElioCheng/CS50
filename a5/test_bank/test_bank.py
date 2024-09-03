import pytest
from bank import value

def test_random():
    assert value("Hello, buddy") == 0
    assert value("How u doin") == 20
    assert value("What's happening") == 100
