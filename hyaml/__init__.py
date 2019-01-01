def main():
    from hyaml.translator import translate
    from hyaml.compiler import Compiler
    from code import interact

    methods = {"square": lambda x: x ** 2, "take": lambda xs, y: xs[:y]}

    _compiler_with_variables = Compiler(bindings=("variables",), method_table=methods)

    evaluate = lambda expr, **lcls: _compiler_with_variables(expr)(lcls)
    interact(local={"evaluate": evaluate})
