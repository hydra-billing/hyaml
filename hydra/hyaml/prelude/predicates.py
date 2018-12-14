import re


def is_even(n):
    return n % 2 == 0


def is_odd(n):
    return not is_even(n)


def is_like(string, pattern):
    return re.match(pattern, string) is not None


def is_empty(value):
    return not value


def is_in(value, container):
    return value in container


def is_null(value):
    return value is None


def _starts_with(value, string):
    return value.startswith(string)


is_starts_with = _starts_with


def _ends_with(value, string):
    return value.endswith(string)


is_ends_with = _ends_with
