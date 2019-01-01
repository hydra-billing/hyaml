def main():
    from hyaml.translator import translate
    from hyaml.compiler import compile
    from code import interact

    def evaluate(expr, **lcls):
        fn = compile(expr, bindings=("variables",))
        return fn(variables=lcls)

    interact(local={"evaluate": evaluate, "translate": translate})
