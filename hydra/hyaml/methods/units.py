def bytes(number):
    return int(number)


_base = 1024
_kilo = _base ** 1
_mega = _base ** 2
_giga = _base ** 3
_tera = _base ** 4


def kilobytes(number):
    return bytes(number) * _kilo


def megabytes(number):
    return bytes(number) * _mega


def gigabytes(number):
    return bytes(number) * _giga


def terabytes(number):
    return bytes(number) * _tera
