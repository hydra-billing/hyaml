# HYAML

HYAML is an expression-oriented language which serves the purpose of writing consice config files without introducing all the power of a fully-featured scripting language. In a nutshell, it's an extensible DSL for writing configs.

The syntax is inspired by the Python programming language. At the same time, it lacks a lot of features Python has since they're not relevant to the common configuration tasks. For example, you won't see list expressions or lambdas here.

Initially, HYAML was built with the library named [CodeTalker](https://pypi.org/project/CodeTalker/). That lib got the job done, however, its main purpose was to be as fast as possible. To be the fastest language parser around CodeTalker used Cython underneath that is essentially C with Python-like syntax. Since Cython, just as C, is a compiled language, it compiles CodeTalker's sources on installation. As time went by, this became a major pain point for maintenance. In addition to that, HYAML wasn't meant to be _that_ fast because of the way it's used: after reading a config file all HYAML-expressions are translated to regular Python functions. This is done once on startup and it's usually _fast enough_. Eventually, HYAML's backend was switched to [ANTLR](https://www.antlr.org/).

## Installation

Use pip to install HYAML. It's tested against Python 3.7 and work with earlier versions is not guaranteed.

```
pip install hyaml
```

### Work-in-progress version

To install a version that hasn't yet been published to the main index run the following command:

```
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple hyaml
```

## Language

HYAML is an expression-oriented language or, to put it another way, it's a one-liner-oriented language. It doesn't support statements or things like assignments (directly, though it can be enhanced in certain ways).

## Features

### Primitives

The exhaustive list of supported primitive values:

- Numbers, including integers and floats (use regular notation, as in `1`, `-1`, `1.0`).
- Strings, enclosed by single or double quotes (`'foo'`, `"bar"`).
- Boolean values are represented as `true` and `false`.
- Variables (`$var_name`).

### Basic math

Addition, subtraction, multiplication, and division are backed by Python. Pay special attention to division since it's translated to `/` which is float point division rather than integer one (namely, `//`). It works like this for historical reasons only.

```
1 + 5  # addition
-3--5  # subtraction, translated to "-3 - -5", use if you don't like spaces
5 * 2  # multiplication
10 / 2 # division
```

### Logical operators

Logical operators are `and`, `or`, and `not`, just as in Python:

```
$a and $b           # conjunction
$b or $c            # disjunction
not $a              # negation
$a and ($b or $c)   # grouping
$foo and not false  # negation precedes other operations, conjunction precedes disjunction
```

### Comparsison

Again, as in Python and most modern programming languages

```
1 > 2  # > stands for greater
1 >= 2 # greater or equal
1 < 2  # less
1 <= 2 # less or equal
1 == 2 # equal
1 != 2 # not equal
```

Range comparisons are supported :tada:

```
10 > $a > 5 # checks whether $a less than 10 and greater than 5
```

### Lists and dicts

Compared to the previous version of HYAML lists (aka arrays) and dicts (aka associative arrays, maps, and hashmaps) are first-level citizens :tada::

```
[1, 2, 3] + [$x, $y, $z] # concatenation of two lists
{abc: 123}               # creates a dict in python {"abc: 123"}
```

Note that dict keys don't require quotes and support hyphens and colons as non-terminating symbols. In other words, `{Sub-Attr:1: 500}` is translated to `{"Sub-Attr:1": 500}`.

### Accessing attributes

A common task when working with HYAML is accessing nested values in a dict. This is what `.` does:

```
$dict_var.Dict-Key-Name.Nested-Key-Name:1
```

The expression above corresponds to the following Python code

```python
dict_var["Dict-Key-Name"]["Nested-Key-Name:1"]
```

`-`, `_`, `:` are special characters allowed for attribute names. When a dict doesn't have the key requested, it will produce a runtime error.

### Calling methods

Values in HYAML can have methods. Essentially, they are not methods at all but regular functions. There's nothing special about method calls except for adding parentheses is required even if the method doesn't take arguments.

```
"abc".substring(1)
$var.upper()
'0xfade114'.to_i(16)
```

Methods returning booleans usually end with `?`:

```
1.odd?()
```

### Work around null

`null` value (known in Python as `None`) is a common source of errors when the value you're working with is not set. It's a burden for both static (such as C or C++) and dynamic (such as Python or JavaScript) languages. Nowadays, many of them offer a concise form of checks for value presence (null-checks). HYAML follows the trend and has support for the [safe navigation operator](https://en.wikipedia.org/wiki/Safe_navigation_operator):

```
$dict_var?.Key-Name:1
```

In the example above, if `$dict_var` is `None` or doesn't contain `Key-Name:1` this won't produce an error. Of course, you can have chains when accessing nested attributes:

```
$dict_var?.Key?.Nested-Key # this is safe now, yay!
```

The operators works for methods as well:

```
$dict_var?.substring(4)?.size() or 0
```

## API

### Translator API

Translator takes a (presumably) valid string HYAML and generates a (most likely) valid Python expression:

```python
from hyaml.translator import translate

translate("$foo")
# get(variables, 'foo')
translate("1.odd?()")
# is_odd(1)
```

### Compiler API

Compiler takes one step further and makes a function from the given expression:

```python
from hyaml.compiler import compile

nine_plus_five = compiler("9 + 5")
nine_plus_five()
# 9
```

For using variables in expressions you'll need to add bindings to functions:

```python
from hyaml.compiler import Compiler
compile = Compiler(bindings=("variables",))

inc = compile("$var + 1")
inc({"var": 1})
# 2
inc({"var": 10})
# 11
```

In order to work with methods you'll need to provide a table of functions to the compiler:

```python
from hyaml.compiler import Compiler

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
from hyaml.compiler import Compiler

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

## Running tests

```bash
python -m unittest tests/test_*
```

## Playground

HYAML is provided with interactive shell for testing out the language, fire it up with `hyaml`

```
$ hyaml

>>> evaluate("$x.starts_with?('foo')", x="foobar")
True
>>>
```
Your command history is stored in the `~/.hyaml_history` file.

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

## Development

HYAML works with Python 3.7+. Install Python and pip then run

```bash
pip install -e .[dev]
```

## Packaging and publishing

Update the version number in setup.py, set a new tag (`-s` is not required if you don't sign your commits):

```
git tag -a -s -m 'Version x.y.z' vx.y.z
```

According to the [docs](https://packaging.python.org/tutorials/packaging-projects/), run the following commands:

```
pip install --upgrade setuptools wheel twine
python3 setup.py sdist bdist_wheel
```

You may want to publish the package to the Test PyPi repo first:

```
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

If you're sure and ready, publish it to the main index:

```
twine upload dist/*
```

Note that for publishing you'll be asked for your credentials for access to PyPi repositories. See additional [instructions](https://packaging.python.org/guides/using-testpypi/#setting-up-testpypi-in-pypirc) on managing credentials.

## Contributing

Bug reports and pull requests are welcome on GitHub at <https://github.com/latera/hyaml>.
