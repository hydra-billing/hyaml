# HYAML

HYAML is a language for configuring Hydra Billing software parts, such as HARD.

The syntax is inspired by the Python programming language. It is enhanced with a number of features useful for writing concise and readable config files. At the same time, it lacks a lot of feature Python has since they're not relevant to the common configuration tasks. For example, you won't see list expressions or lambdas here.

Initially, HYAML was built with the library named [CodeTalker](https://pypi.org/project/CodeTalker/). That lib got the job done, however, its main purpose was to be as fast as possible. To be the fastest language parser around CodeTalker used Cython underneath that is essentially C with Python-like syntax. Since Cython, just as C, is a compiled language it compiles CodeTalker's sources on installation. As time went by, this became a major maintenance pain point. In addition to that, HYAML wasn't meant to be fast because of the way it's used: after reading the config file all HYAML-expressions are translated to regular Python functions. This is done once on startup and it's usually _fast enough_. Eventually, HYAML's backend was switched to ANTLR.

## ANTLR

TL;DR: ANTLR is a tool for building language parsers. Be sure you visited its [website](https://www.antlr.org/) and checked out the [source code](https://github.com/antlr/antlr4). ANTLR is written in Java but can generate parsers in Python. Compared to CodeTalker it has plenty of [examples](https://github.com/jszheng/py3antlr4book) and a ton of answered question at StackOverflow.

In order to build a new parser, follow the instructions (taken from the ANTLR's github [page](https://github.com/antlr/antlr4/blob/master/doc/python-target.md)):

- Install ANTLR from https://www.antlr.org/.
- Define your language grammar in the .g4 format (there's an extension for VSCode!).
- Generate the output by running
  ```bash
  antlr4 -Dlanguage=Python3 -no-listener -visitor MyGrammar.g4
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

For transforming parsed structures you'll need a visitor.

## Traversing API

