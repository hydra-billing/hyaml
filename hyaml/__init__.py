def main():
    from hyaml.translator import translate
    from hyaml.compiler import compile_expression
    from code import interact

    def evaluate(expr, **lcls):
        fn = compile_expression(expr, bindings=("variables",))
        return fn(variables=lcls)

    interact(local={"evaluate": evaluate, "translate": translate})
