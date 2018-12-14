def safe_get(obj, attr):
    if obj is not None and attr in obj:
        return obj[attr]
    else:
        return None


def safe_call(obj, f, *args):
    if obj is None:
        return None
    else:
        return f(obj, *args)


def get(dict, key):
    return dict[key]

