"""
Simple test.

$ python -m pytest tests/
"""


def test_pass():
    assert 1 == 1


def test_fail():
    assert 1 == 2

# pep 8 fail