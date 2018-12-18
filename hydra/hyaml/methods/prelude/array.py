def map_join(array, separator=","):
    return list(map(lambda pair: separator.join(pair), array))
