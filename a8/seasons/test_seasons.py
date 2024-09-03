import pytest
from seasons import season

def test_random():
    with pytest.raises(ValueError):
        season(2025, 5, 31)

