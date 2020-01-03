import pytest
from py_str_case import *

def test_upper_case():
    assert uppercase("hello") == "HELLO"


def test_lower_case():
    assert lowercase("Hello") == "hello"


def test_capital_case():
    assert capitalcase("hello") == "Hello"


def test_const_case():
    assert constcase("foo_bar") == "FOO_BAR"


def test_pascal_case():
    assert pascalcase("foo_bar") == "Foobar"


def test_path_case():
    assert pathcase("foo_bar") == "foo/bar"


def test_sentence_case():
    assert sentencecase("FooBar") == "Foo bar"


def test_snake_case():
    assert snakecase("fooBarBaz") == "foo_bar_baz"


def test_spinal_case():
    assert spinalcase("foo_bar_baz") == "foo-bar-baz"


def test_title_case():
    assert titlecase("foo_bar") == "Foo Bar"


def test_trim_case():
    assert trimcase(" hello ") == "hello"


def test_alphanum_case():
    assert alphanumcase("Foo_123 Bar!") == "Foo123Bar"


def test_fail_lower_case():
    assert lowercase("") == "Enter the string to convert.."
