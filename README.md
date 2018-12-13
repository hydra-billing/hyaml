# HYAML

HYAML is a language for configuring Hydra Billing software parts, such as HARD.

The syntax is inspired by the Python programming language. It is enhanced with a number of features useful for writing concise and readable config files. At the same time, it lacks a lot of feature Python has since they're not relevant to the common configuration tasks. For example, you won't see list expressions or lambdas here.

Initially, HYAML was built with the library named [CodeTalker](https://pypi.org/project/CodeTalker/). That lib got the job done, however, its main purpose was to be as fast as possible. To be the fastest language parser around CodeTalker used Cython underneath that is essentially C with Python-like syntax. Since Cython, just as C, is a compiled language it compiles CodeTalker's sources on installation. As time went by, this became a major maintenance pain point. In addition to that, HYAML wasn't meant to be fast because of the way it's used: after reading the config file all HYAML-expressions are translated to regular Python functions. This is done once on startup and it's usually _fast enough_. Eventually, HYAML's backend was switched to ANTLR.

## Installation

```
#
```

## API

### Translator API

Translator takes a (presumably) valid string HYAML and generates a (most likely) valid Python expression:

```python
from hydra.hyaml.translator import translate

translate("$foo") 
# variables.get('foo')
translate("1.odd?()")
# is_odd(1)
```

### Compiler API

Compiler takes one step further and makes a function from the given expression:

```python
from hydra.hyaml.compiler import compile

nine_plus_five = compiler("9 + 5")
nine_plus_five() 
# 9
```

For using variables in expressions you'll need to add bindings to functions:

```python
from hydra.hyaml.compiler import Compiler
compile = Compiler(bindings=("variables",))

inc = compile("$var + 1")
inc({"var": 1})
# 2
inc({"var": 10})
# 11
```

In order to work with methods you'll need to provide a table of functions to the compiler:

```python
from hydra.hyaml.compiler import Compiler

methods = {
    "square": lambda x: x ** 2, 
    "is_like": lambda x, y: x.startswith(y)
}
compile = Compiler(method_name=methods)

square = compile("5.square()")
square()
# 25
like = compiler("'abcdef'.like?('ab')")
like()
# True
```

Finally, using variables and methods together:

```python
from hydra.hyaml.compiler import Compiler

methods = {
    "square": lambda x: x ** 2, 
    "is_like": lambda x, y: x.startswith(y)
}
compile = Compiler(method_name=methods, bindings=("variables",))
square = compile("$x.square()")
square({"x": 10})
# 100
square({"x": 7})
# 49
like = compile("'abcdef'.like?($str)")
like({"str": "ab"})
# True
like({"str": "abc"})
# True
```

For those who curious, there's a module named "prelude" which holds globally available methods. They are used for implementing some language features. Specifically, the subscription operator (aka square brackets) relies on `get`, safe navigation to attributes and method calls relies on `safe_get` and `safe_call` respectively. You can override those methods with your own variants using `method_table` (but you cannot remove them, why would you anyway?).

## Development

HYAML works with Python 3.7+. Install Python and pip then run

```bash
pip install -r requirements.txt
```

## Running tests

```bash
python -m unittest tests/test_*
```

## Playground

HYAML is provided with interactive shell for testing out the language, fire it up with `./bin/console`

```
./bin/console

(Pdb) translate("$var")
"variables.get('var')"
(Pdb) evaluate("1 + 1")
2
(Pdb) evaluate("1 + $x", {"x": 2})
3
```

## ANTLR

TL;DR: ANTLR is a tool for building language parsers. Be sure you visited its [website](https://www.antlr.org/) and checked out the [source code](https://github.com/antlr/antlr4). ANTLR is written in Java but can generate parsers in Python. Compared to CodeTalker it has plenty of [examples](https://github.com/jszheng/py3antlr4book) and a ton of answered question at StackOverflow.

In order to build a new parser, follow the instructions (taken from the ANTLR's github [page](https://github.com/antlr/antlr4/blob/master/doc/python-target.md)):

- Install ANTLR from https://www.antlr.org/.
- Define your language grammar in the .g4 format (there's an extension for VSCode!).
- Generate the output by running
  ```bash
  antlr4 -Dlanguage=Python3 MyGrammar.g4
  ```
- Add all generated/updated files to commit.
- You're all set!

## G4

One can the documentation or even read a book about ANTLR but building a new language can be done by examples. At least, this is the way Hyaml.g4 was written.

## Lexer/Parser API

A simple example of using generated lexer and parser follows:

```python
import sys
from antlr4 import *
from HyamlLexer import HyamlLexer
from HyamlParser import HyamlParser

def main(argv):
    input = FileStream(argv[1])
    ### Create a lexer instance and pass an IO object to its constructor
    lexer = HyamlLexer(input)
    stream = CommonTokenStream(lexer)
    ### Create a parser and feed it with tokens
    parser = HyamlParser(stream)
    tree = parser.prog()
    lisp_tree_str = tree.toStringTree(recog=parser)
    ### Print a simple tree representation
    print(lisp_tree_str)

if __name__ == '__main__':
    main(sys.argv)
```

Running this script with `python parser-example.py sample.txt` prints something like:
```
(prog (expr (expr $cdr) (callChain (link (methodCall . some (arguments ( (exprList (expr (listLiteral [ ]))) )))))) \n)
```

For transforming parsed structures you'll need a listener.

## Listener API

Along with a lexer and a parser, ANTLR generates a listener, a class which can be used to track the parsing process. In order to use it, create a subclass for the generated listener and implement necessary hook methods:

```python
class Listener(MyGrammarListener):
    def __init__(self):
        self._initial_state = MyState()

    def enterMyExpression(self, ctx):
        self._modifyStateAsNeeded()

    def exitMyExpression(self, ctx):
        self._modifyStateAsNeeded()
```

Check out `translator.py` to see a real example, it's rather straightforward.


