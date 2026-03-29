def main():
    import os
    import readline
    from hyaml.translator import translate
    from hyaml.compiler import compile_expression
    from code import interact

    def evaluate(expr, **lcls):
        fn = compile_expression(expr, bindings=("variables",))
        return fn(variables=lcls)

    histfile = os.path.join(os.path.expanduser("~"), ".hyaml_history")
    try:
        readline.read_history_file(histfile)
    except FileNotFoundError:
        pass

    interact(banner="HYAML Playgroud", local={"evaluate": evaluate, "translate": translate})

    readline.write_history_file(histfile)
