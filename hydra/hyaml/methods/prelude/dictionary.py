from copy import copy


def merge(dictionary, *args):
    if len(args) == 2:
        key, value = args
        return {**dictionary, key: value}
    elif isinstance(args[0], list):
        if len(args[0]) == 2 and not isinstance(args[0][0], list):
            key, value = args[0]
            return {**dictionary, key: value}
        else:
            return {**dictionary, **{key: value for (key, value) in args[0]}}
    else:
        return {**dictionary, **args[0]}


def pairs(dictionary):
    return list(sorted(dictionary.items()))


def except_(dictionary, *keys):
    return {k: v for (k, v) in dictionary.items() if k not in keys}

