# Generated from Hyaml.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .HyamlParser import HyamlParser
else:
    from HyamlParser import HyamlParser

# This class defines a complete listener for a parse tree produced by HyamlParser.
class HyamlListener(ParseTreeListener):

    # Enter a parse tree produced by HyamlParser#prog.
    def enterProg(self, ctx:HyamlParser.ProgContext):
        pass

    # Exit a parse tree produced by HyamlParser#prog.
    def exitProg(self, ctx:HyamlParser.ProgContext):
        pass


    # Enter a parse tree produced by HyamlParser#expr.
    def enterExpr(self, ctx:HyamlParser.ExprContext):
        pass

    # Exit a parse tree produced by HyamlParser#expr.
    def exitExpr(self, ctx:HyamlParser.ExprContext):
        pass


    # Enter a parse tree produced by HyamlParser#callChain.
    def enterCallChain(self, ctx:HyamlParser.CallChainContext):
        pass

    # Exit a parse tree produced by HyamlParser#callChain.
    def exitCallChain(self, ctx:HyamlParser.CallChainContext):
        pass


    # Enter a parse tree produced by HyamlParser#attributeOrDispatch.
    def enterAttributeOrDispatch(self, ctx:HyamlParser.AttributeOrDispatchContext):
        pass

    # Exit a parse tree produced by HyamlParser#attributeOrDispatch.
    def exitAttributeOrDispatch(self, ctx:HyamlParser.AttributeOrDispatchContext):
        pass


    # Enter a parse tree produced by HyamlParser#exprList.
    def enterExprList(self, ctx:HyamlParser.ExprListContext):
        pass

    # Exit a parse tree produced by HyamlParser#exprList.
    def exitExprList(self, ctx:HyamlParser.ExprListContext):
        pass


    # Enter a parse tree produced by HyamlParser#args.
    def enterArgs(self, ctx:HyamlParser.ArgsContext):
        pass

    # Exit a parse tree produced by HyamlParser#args.
    def exitArgs(self, ctx:HyamlParser.ArgsContext):
        pass


    # Enter a parse tree produced by HyamlParser#subscription.
    def enterSubscription(self, ctx:HyamlParser.SubscriptionContext):
        pass

    # Exit a parse tree produced by HyamlParser#subscription.
    def exitSubscription(self, ctx:HyamlParser.SubscriptionContext):
        pass


    # Enter a parse tree produced by HyamlParser#listLiteral.
    def enterListLiteral(self, ctx:HyamlParser.ListLiteralContext):
        pass

    # Exit a parse tree produced by HyamlParser#listLiteral.
    def exitListLiteral(self, ctx:HyamlParser.ListLiteralContext):
        pass


    # Enter a parse tree produced by HyamlParser#keyValuePair.
    def enterKeyValuePair(self, ctx:HyamlParser.KeyValuePairContext):
        pass

    # Exit a parse tree produced by HyamlParser#keyValuePair.
    def exitKeyValuePair(self, ctx:HyamlParser.KeyValuePairContext):
        pass


    # Enter a parse tree produced by HyamlParser#keyValuePairs.
    def enterKeyValuePairs(self, ctx:HyamlParser.KeyValuePairsContext):
        pass

    # Exit a parse tree produced by HyamlParser#keyValuePairs.
    def exitKeyValuePairs(self, ctx:HyamlParser.KeyValuePairsContext):
        pass


    # Enter a parse tree produced by HyamlParser#dictLiteral.
    def enterDictLiteral(self, ctx:HyamlParser.DictLiteralContext):
        pass

    # Exit a parse tree produced by HyamlParser#dictLiteral.
    def exitDictLiteral(self, ctx:HyamlParser.DictLiteralContext):
        pass


    # Enter a parse tree produced by HyamlParser#parens.
    def enterParens(self, ctx:HyamlParser.ParensContext):
        pass

    # Exit a parse tree produced by HyamlParser#parens.
    def exitParens(self, ctx:HyamlParser.ParensContext):
        pass


