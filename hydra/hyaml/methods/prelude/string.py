import re
from datetime import datetime


def length(string):
    return len(string)


def substring(string, start, end=None):
    return string[start:end]


def to_i(string, base=None):
    if base is None:
        return int(string)
    else:
        return int(string, base)


def unhex(string):
    if string.startswith("0x"):
        hexed = string[2:]
    else:
        hexed = string

    return bytes.fromhex(hexed).decode("utf-8")


def replace(string, pattern, replacement=""):
    return string.replace(pattern, replacement)


def regexp_replace(string, pattern, replacement=""):
    return re.sub(pattern, replacement, string)


def reverse(string):
    return string[::-1]


def pad_left(string, length, pad_with):
    return string.rjust(length, pad_with)


def pad_right(string, length, pad_with):
    return string.ljust(length, pad_with)


def _starts_with(value, string):
    return value.startswith(string)


is_starts_with = _starts_with


def _ends_with(value, string):
    return value.endswith(string)


is_ends_with = _ends_with


def is_like(string, pattern):
    return re.match(pattern, string) is not None


def split(string, separator=None, max=-1):
    return string.split(separator, max)


def strip(string):
    return string.strip()


def upper(string):
    return string.upper()


def lower(string):
    return string.lower()


def to_date(string, fmt):
    return datetime.strptime(string, fmt)
