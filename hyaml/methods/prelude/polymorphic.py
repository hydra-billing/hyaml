from datetime import datetime


def to_hex(value):
    if isinstance(value, str):
        return value.encode().hex()
    else:
        return hex(value)


def is_empty(value):
    return not value


def is_in(value, container):
    return value in container


def is_null(value):
    return value is None


def to_s(value, fmt=None):
    if value is None:
        return ""
    elif isinstance(value, datetime):
        return value.strftime(fmt)
    else:
        return str(value)


def try_(value, key, default=None):
    if value is None:
        return default
    elif isinstance(value, dict):
        return value.get(key, default)
    elif isinstance(value, list):
        if -len(value) <= key < len(value):
            return value[key]
        else:
            return default
    elif key in value:
        return value[key]
    else:
        return default


def coalesce(value, *args):
    if value is not None:
        return value

    for arg in args:
        if arg is not None:
            return arg
    else:
        return None


def to_list(value):
    if value is None:
        return []
    elif isinstance(value, dict):
        return list(sorted(value.items()))
    elif isinstance(value, list):
        return value
    else:
        return [value]
