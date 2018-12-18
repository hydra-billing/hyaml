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


def to_s(value):
    if value is None:
        return ""
    else:
        return str(value)
