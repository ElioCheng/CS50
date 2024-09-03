import pytest
from um import count

def test_random():
    assert count("um") == 1
    assert count("um, um, um") == 3
    assert count("um... um, um!") == 3
    assert count("I was, um, thinking about it.") == 1
    assert count("yummy") == 0
    assert count("umbrella") == 0
    assert count("Um, UM, uM") == 3

