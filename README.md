[![Build Status](https://travis-ci.org/ShivaShankerReddy/py_string_case.svg?branch=master)](https://travis-ci.org/ShivaShankerReddy/py_string_case)[PyPI](https://pypi.org/project/py-str-case/)

# py_str_case

This module is extension of [stringcase](https://github.com/okunishinishi/python-stringcase/).

Convert string cases between camel case, pascal case, snake case etc...

# Examples

```
import py_str_case
py_str_case.camelcase('foo_bar_baz') # => "fooBarBaz"
py_str_case.camelcase('FooBarBaz') # => "fooBarBaz"
py_str_case.capitalcase('foo_bar_baz') # => "Foo_bar_baz"
py_str_case.capitalcase('FooBarBaz') # => "FooBarBaz"
py_str_case.constcase('foo_bar_baz') # => "FOO_BAR_BAZ"
py_str_case.constcase('FooBarBaz') # => "FOO_BAR_BAZ"
py_str_case.lowercase('foo_bar_baz') # => "foo_bar_baz"
py_str_case.lowercase('FooBarBaz') # => "foobarbaz"
py_str_case.pascalcase('foo_bar_baz') # => "FooBarBaz"
py_str_case.pascalcase('FooBarBaz') # => "FooBarBaz"
py_str_case.pathcase('foo_bar_baz') # => "foo/bar/baz"
py_str_case.pathcase('FooBarBaz') # => "foo/bar/baz"
py_str_case.sentencecase('foo_bar_baz') # => "Foo bar baz"
py_str_case.sentencecase('FooBarBaz') # => "Foo bar baz"
py_str_case.snakecase('foo_bar_baz') # => "foo_bar_baz"
py_str_case.snakecase('FooBarBaz') # => "foo_bar_baz"
py_str_case.spinalcase('foo_bar_baz') # => "foo-bar-baz"
py_str_case.spinalcase('FooBarBaz') # => "-foo-bar-baz"
py_str_case.titlecase('foo_bar_baz') # => "Foo Bar Baz"
py_str_case.titlecase('FooBarBaz') # => " Foo Bar Baz"
py_str_case.trimcase('foo_bar_baz') # => "foo_bar_baz"
py_str_case.trimcase(' FooBarBaz ') # => "FooBarBaz"
py_str_case.uppercase('foo_bar_baz') # => "FOO_BAR_BAZ"
py_str_case.uppercase('FooBarBaz') # => "FOOBARBAZ"
py_str_case.alphanumcase('_Foo., Bar') # =>'FooBar'
py_str_case.alphanumcase('Foo_123 Bar!') # =>'Foo123Bar'
```

# Failure Message

```
py_str_case.alphanumcase('') # =>'Enter the string to convert..'
```


# Install

`pip install py_str_case`
