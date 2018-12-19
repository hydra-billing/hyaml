from datetime import timedelta


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


def seconds(number):
    return timedelta(seconds=number)


def minutes(number):
    return timedelta(minutes=number)


def hours(number):
    return timedelta(hours=number)


def days(number):
    return timedelta(days=number)


def weeks(number):
    return timedelta(weeks=number)


def months(number):
    return timedelta(days=number * 30)


def years(number):
    return timedelta(days=number * 365)

