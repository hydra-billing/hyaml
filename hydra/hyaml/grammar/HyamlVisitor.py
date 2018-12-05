# Generated from Hyaml.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .HyamlParser import HyamlParser
else:
    from HyamlParser import HyamlParser

# This class defines a complete generic visitor for a parse tree produced by HyamlParser.

class HyamlVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by HyamlParser#prog.
    def visitProg(self, ctx:HyamlParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HyamlParser#expr.
    def visitExpr(self, ctx:HyamlParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HyamlParser#link.
    def visitLink(self, ctx:HyamlParser.LinkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HyamlParser#callChain.
    def visitCallChain(self, ctx:HyamlParser.CallChainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HyamlParser#methodCall.
    def visitMethodCall(self, ctx:HyamlParser.MethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HyamlParser#attribute.
    def visitAttribute(self, ctx:HyamlParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HyamlParser#exprList.
    def visitExprList(self, ctx:HyamlParser.ExprListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HyamlParser#arguments.
    def visitArguments(self, ctx:HyamlParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HyamlParser#subscription.
    def visitSubscription(self, ctx:HyamlParser.SubscriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HyamlParser#boolLiteral.
    def visitBoolLiteral(self, ctx:HyamlParser.BoolLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HyamlParser#boolOperator.
    def visitBoolOperator(self, ctx:HyamlParser.BoolOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HyamlParser#listLiteral.
    def visitListLiteral(self, ctx:HyamlParser.ListLiteralContext):
        return self.visitChildren(ctx)



del HyamlParser