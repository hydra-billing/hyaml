from hyaml.methods.prelude.polymorphic import to_s


def map_join(array, separator=","):
    return list(map(lambda pair: separator.join(pair), array))


def join(array, separator=""):
    return separator.join(map(to_s, array))
