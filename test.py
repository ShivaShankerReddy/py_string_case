import pytest
from main import *

def test_upper_case():
    assert uppercase("hello") == "HELLO"


def test_lower_case():
    assert lowercase("Hello") == "hello"()


# def test_capital_case():
#     assert capitalcase("") == "".capitalize()


# def test_capital_case():
#     # assert 