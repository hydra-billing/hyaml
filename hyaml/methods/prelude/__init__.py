from hyaml.methods.prelude import (
    runtime,
    string,
    number,
    polymorphic,
    dictionary,
    array,
)

runtime = runtime.__dict__
string = string.__dict__
number = number.__dict__
polymorphic = polymorphic.__dict__
dictionary = dictionary.__dict__
array = array.__dict__

all = {**runtime, **string, **number, **polymorphic, **dictionary, **array}
