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


    # Enter a parse tree produced by HyamlParser#link.
    def enterLink(self, ctx:HyamlParser.LinkContext):
        pass

    # Exit a parse tree produced by HyamlParser#link.
    def exitLink(self, ctx:HyamlParser.LinkContext):
        pass


    # Enter a parse tree produced by HyamlParser#callChain.
    def enterCallChain(self, ctx:HyamlParser.CallChainContext):
        pass

    # Exit a parse tree produced by HyamlParser#callChain.
    def exitCallChain(self, ctx:HyamlParser.CallChainContext):
        pass


    # Enter a parse tree produced by HyamlParser#methodCall.
    def enterMethodCall(self, ctx:HyamlParser.MethodCallContext):
        pass

    # Exit a parse tree produced by HyamlParser#methodCall.
    def exitMethodCall(self, ctx:HyamlParser.MethodCallContext):
        pass


    # Enter a parse tree produced by HyamlParser#attribute.
    def enterAttribute(self, ctx:HyamlParser.AttributeContext):
        pass

    # Exit a parse tree produced by HyamlParser#attribute.
    def exitAttribute(self, ctx:HyamlParser.AttributeContext):
        pass


    # Enter a parse tree produced by HyamlParser#exprList.
    def enterExprList(self, ctx:HyamlParser.ExprListContext):
        pass

    # Exit a parse tree produced by HyamlParser#exprList.
    def exitExprList(self, ctx:HyamlParser.ExprListContext):
        pass


    # Enter a parse tree produced by HyamlParser#arguments.
    def enterArguments(self, ctx:HyamlParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by HyamlParser#arguments.
    def exitArguments(self, ctx:HyamlParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by HyamlParser#subscription.
    def enterSubscription(self, ctx:HyamlParser.SubscriptionContext):
        pass

    # Exit a parse tree produced by HyamlParser#subscription.
    def exitSubscription(self, ctx:HyamlParser.SubscriptionContext):
        pass


    # Enter a parse tree produced by HyamlParser#boolLiteral.
    def enterBoolLiteral(self, ctx:HyamlParser.BoolLiteralContext):
        pass

    # Exit a parse tree produced by HyamlParser#boolLiteral.
    def exitBoolLiteral(self, ctx:HyamlParser.BoolLiteralContext):
        pass


    # Enter a parse tree produced by HyamlParser#boolOperator.
    def enterBoolOperator(self, ctx:HyamlParser.BoolOperatorContext):
        pass

    # Exit a parse tree produced by HyamlParser#boolOperator.
    def exitBoolOperator(self, ctx:HyamlParser.BoolOperatorContext):
        pass


    # Enter a parse tree produced by HyamlParser#listLiteral.
    def enterListLiteral(self, ctx:HyamlParser.ListLiteralContext):
        pass

    # Exit a parse tree produced by HyamlParser#listLiteral.
    def exitListLiteral(self, ctx:HyamlParser.ListLiteralContext):
        pass


