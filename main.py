"""
main
"""

import re


def string_validation(func):
    def wrapper(param):
        if not param:
            return("Enter the string to convert..")
        else:
            return (func(param))
    return (wrapper)


@string_validation
def camelcase(string):
    """ Convert string into camel case.
    Args:
        string: String to convert.
    Returns:
        string: Camel case string.
    """

    string = re.sub(r"^[\-_\.]+", '', str(string))
    return lowercase(string[0]) + re.sub(r"[\-_\.\s]([a-z])", lambda matched: uppercase(matched.group(1)), string[1:])


@string_validation
def capitalcase(string):
    """Convert string into capital case.
    First letters will be uppercase.
    Args:
        string: String to convert.
    Returns:
        string: Capital case string.
    """

    # string = str(string)
    return string.capitalize()


@string_validation
def constcase(string):
    """Convert string into upper snake case.
    Join punctuation with underscore and convert letters into uppercase.
    Args:
        string: String to convert.
    Returns:
        string: Const cased string.
    """

    return uppercase(snakecase(string))


@string_validation
def lowercase(string):
    """Convert string into lower case.
    Args:
        string: String to convert.
    Returns:
        string: Lowercase case string.
    """

    return str(string).lower()


@string_validation
def pascalcase(string):
    """Convert string into pascal case.
    Args:
        string: String to convert.
    Returns:
        string: Pascal case string.
    """

    return capitalcase(camelcase(string))


@string_validation
def pathcase(string):
    """Convert string into path case.
    Join punctuation with slash.
    Args:
        string: String to convert.
    Returns:
        string: Path cased string.
    """
    string = snakecase(string)
    return re.sub(r"_", "/", string)


@string_validation
def backslashcase(string):
    """Convert string into spinal case.
    Join punctuation with backslash.
    Args:
        string: String to convert.
    Returns:
        string: Spinal cased string.
    """
    str1 = re.sub(r"_", r"\\", snakecase(string))

    return str1
    # return re.sub(r"\\n", "", str1))  # TODO: make regex fot \t ...


@string_validation
def sentencecase(string):
    """Convert string into sentence case.
    First letter capped and each punctuations are joined with space.
    Args:
        string: String to convert.
    Returns:
        string: Sentence cased string.
    """
    joiner = ' '
    string = re.sub(r"[\-_\.\s]", joiner, str(string))
    return capitalcase(trimcase(
        re.sub(r"[A-Z]", lambda matched: joiner +
                                         lowercase(matched.group(0)), string)
    ))


@string_validation
def snakecase(string):
    """Convert string into snake case.
    Join punctuation with underscore
    Args:
        string: String to convert.
    Returns:
        string: Snake cased string.
    """

    string = re.sub(r"[\-\.\s]", '_', str(string))
    return lowercase(string[0]) + re.sub(r"[A-Z]",
                        lambda matched: '_' + lowercase(matched.group(0)),
                        string[1:]
        )


@string_validation
def spinalcase(string):
    """Convert string into spinal case.
    Join punctuation with hyphen.
    Args:
        string: String to convert.
    Returns:
        string: Spinal cased string.
    """

    return re.sub(r"_", "-", snakecase(string))


@string_validation
def dotcase(string):
    """Convert string into dot case.
    Join punctuation with dot.
    Args:
        string: String to convert.
    Returns:
        string: Dot cased string.
    """

    return re.sub(r"_", ".", snakecase(string))


@string_validation
def titlecase(string):
    """Convert string into sentence case.
    First letter capped while each punctuations is capitalsed
    and joined with space.
    Args:
        string: String to convert.
    Returns:
        string: Title cased string.
    """

    return ' '.join(
        [capitalcase(word) for word in snakecase(string).split("_")]
    )


@string_validation
def trimcase(string):
    """Convert string into trimmed string.
    Args:
        string: String to convert.
    Returns:
        string: Trimmed case string
    """

    return str(string).strip()


@string_validation
def uppercase(string):
    """Convert string into upper case.
    Args:
        string: String to convert.
    Returns:
        string: Uppercase case string.
    """

    return str(string).upper()


@string_validation
def alphanumcase(string):
    """Cuts all non-alphanumeric symbols,
    i.e. cuts all expect except 0-9, a-z and A-Z.
    Args:
        string: String to convert.
    Returns:
        string: String with cutted non-alphanumeric symbols.
    """
    return ''.join(filter(str.isalnum, str(string)))



print(alphanumcase('Foo_123 Bar!'))
