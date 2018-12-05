# Generated from Hyaml.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\31")
        buf.write("n\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5")
        buf.write("\3*\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\7\3:\n\3\f\3\16\3=\13\3\3\4\3\4\5\4A\n\4\3")
        buf.write("\5\6\5D\n\5\r\5\16\5E\3\6\3\6\3\6\5\6K\n\6\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\b\3\b\3\b\7\bU\n\b\f\b\16\bX\13\b\3\t\3\t\5")
        buf.write("\t\\\n\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\f\3\f\3\r")
        buf.write("\3\r\5\rj\n\r\3\r\3\r\3\r\2\3\4\16\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\2\4\3\2\n\13\3\2\f\r\2s\2\32\3\2\2\2\4)\3\2")
        buf.write("\2\2\6@\3\2\2\2\bC\3\2\2\2\nG\3\2\2\2\fN\3\2\2\2\16Q\3")
        buf.write("\2\2\2\20Y\3\2\2\2\22_\3\2\2\2\24c\3\2\2\2\26e\3\2\2\2")
        buf.write("\30g\3\2\2\2\32\33\5\4\3\2\33\3\3\2\2\2\34\35\b\3\1\2")
        buf.write("\35\36\7\3\2\2\36\37\5\4\3\2\37 \7\4\2\2 *\3\2\2\2!\"")
        buf.write("\7\16\2\2\"*\5\4\3\16#*\5\30\r\2$*\7\22\2\2%*\7\26\2\2")
        buf.write("&*\7\17\2\2\'*\7\30\2\2(*\5\24\13\2)\34\3\2\2\2)!\3\2")
        buf.write("\2\2)#\3\2\2\2)$\3\2\2\2)%\3\2\2\2)&\3\2\2\2)\'\3\2\2")
        buf.write("\2)(\3\2\2\2*;\3\2\2\2+,\f\f\2\2,-\7\20\2\2-:\5\4\3\r")
        buf.write("./\f\13\2\2/\60\7\21\2\2\60:\5\4\3\f\61\62\f\n\2\2\62")
        buf.write("\63\5\26\f\2\63\64\5\4\3\13\64:\3\2\2\2\65\66\f\t\2\2")
        buf.write("\66:\5\b\5\2\678\f\b\2\28:\5\22\n\29+\3\2\2\29.\3\2\2")
        buf.write("\29\61\3\2\2\29\65\3\2\2\29\67\3\2\2\2:=\3\2\2\2;9\3\2")
        buf.write("\2\2;<\3\2\2\2<\5\3\2\2\2=;\3\2\2\2>A\5\n\6\2?A\5\f\7")
        buf.write("\2@>\3\2\2\2@?\3\2\2\2A\7\3\2\2\2BD\5\6\4\2CB\3\2\2\2")
        buf.write("DE\3\2\2\2EC\3\2\2\2EF\3\2\2\2F\t\3\2\2\2GH\7\5\2\2HJ")
        buf.write("\7\23\2\2IK\7\27\2\2JI\3\2\2\2JK\3\2\2\2KL\3\2\2\2LM\5")
        buf.write("\20\t\2M\13\3\2\2\2NO\7\5\2\2OP\7\23\2\2P\r\3\2\2\2QV")
        buf.write("\5\4\3\2RS\7\6\2\2SU\5\4\3\2TR\3\2\2\2UX\3\2\2\2VT\3\2")
        buf.write("\2\2VW\3\2\2\2W\17\3\2\2\2XV\3\2\2\2Y[\7\3\2\2Z\\\5\16")
        buf.write("\b\2[Z\3\2\2\2[\\\3\2\2\2\\]\3\2\2\2]^\7\4\2\2^\21\3\2")
        buf.write("\2\2_`\7\7\2\2`a\5\4\3\2ab\7\b\2\2b\23\3\2\2\2cd\t\2\2")
        buf.write("\2d\25\3\2\2\2ef\t\3\2\2f\27\3\2\2\2gi\7\7\2\2hj\5\16")
        buf.write("\b\2ih\3\2\2\2ij\3\2\2\2jk\3\2\2\2kl\7\b\2\2l\31\3\2\2")
        buf.write("\2\13)9;@EJV[i")
        return buf.getvalue()


class HyamlParser ( Parser ):

    grammarFileName = "Hyaml.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'.'", "','", "'['", "']'", 
                     "<INVALID>", "'true'", "'false'", "'and'", "'or'", 
                     "'not'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'{}'", "'?'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NEWLINE", 
                      "TRUE", "FALSE", "AND", "OR", "NOT", "NUMBER", "CALC_OP", 
                      "COMP_OP", "VAR", "ID", "LETTER", "DIGIT", "EMPTY_HASH", 
                      "PRED", "STRING", "WS" ]

    RULE_prog = 0
    RULE_expr = 1
    RULE_link = 2
    RULE_callChain = 3
    RULE_methodCall = 4
    RULE_attribute = 5
    RULE_exprList = 6
    RULE_arguments = 7
    RULE_subscription = 8
    RULE_boolLiteral = 9
    RULE_boolOperator = 10
    RULE_listLiteral = 11

    ruleNames =  [ "prog", "expr", "link", "callChain", "methodCall", "attribute", 
                   "exprList", "arguments", "subscription", "boolLiteral", 
                   "boolOperator", "listLiteral" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    NEWLINE=7
    TRUE=8
    FALSE=9
    AND=10
    OR=11
    NOT=12
    NUMBER=13
    CALC_OP=14
    COMP_OP=15
    VAR=16
    ID=17
    LETTER=18
    DIGIT=19
    EMPTY_HASH=20
    PRED=21
    STRING=22
    WS=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(HyamlParser.ExprContext,0)


        def getRuleIndex(self):
            return HyamlParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = HyamlParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HyamlParser.ExprContext)
            else:
                return self.getTypedRuleContext(HyamlParser.ExprContext,i)


        def NOT(self):
            return self.getToken(HyamlParser.NOT, 0)

        def listLiteral(self):
            return self.getTypedRuleContext(HyamlParser.ListLiteralContext,0)


        def VAR(self):
            return self.getToken(HyamlParser.VAR, 0)

        def EMPTY_HASH(self):
            return self.getToken(HyamlParser.EMPTY_HASH, 0)

        def NUMBER(self):
            return self.getToken(HyamlParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(HyamlParser.STRING, 0)

        def boolLiteral(self):
            return self.getTypedRuleContext(HyamlParser.BoolLiteralContext,0)


        def CALC_OP(self):
            return self.getToken(HyamlParser.CALC_OP, 0)

        def COMP_OP(self):
            return self.getToken(HyamlParser.COMP_OP, 0)

        def boolOperator(self):
            return self.getTypedRuleContext(HyamlParser.BoolOperatorContext,0)


        def callChain(self):
            return self.getTypedRuleContext(HyamlParser.CallChainContext,0)


        def subscription(self):
            return self.getTypedRuleContext(HyamlParser.SubscriptionContext,0)


        def getRuleIndex(self):
            return HyamlParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HyamlParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HyamlParser.T__0]:
                self.state = 27
                self.match(HyamlParser.T__0)
                self.state = 28
                self.expr(0)
                self.state = 29
                self.match(HyamlParser.T__1)
                pass
            elif token in [HyamlParser.NOT]:
                self.state = 31
                self.match(HyamlParser.NOT)
                self.state = 32
                self.expr(12)
                pass
            elif token in [HyamlParser.T__4]:
                self.state = 33
                self.listLiteral()
                pass
            elif token in [HyamlParser.VAR]:
                self.state = 34
                self.match(HyamlParser.VAR)
                pass
            elif token in [HyamlParser.EMPTY_HASH]:
                self.state = 35
                self.match(HyamlParser.EMPTY_HASH)
                pass
            elif token in [HyamlParser.NUMBER]:
                self.state = 36
                self.match(HyamlParser.NUMBER)
                pass
            elif token in [HyamlParser.STRING]:
                self.state = 37
                self.match(HyamlParser.STRING)
                pass
            elif token in [HyamlParser.TRUE, HyamlParser.FALSE]:
                self.state = 38
                self.boolLiteral()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 57
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 55
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = HyamlParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 41
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 42
                        self.match(HyamlParser.CALC_OP)
                        self.state = 43
                        self.expr(11)
                        pass

                    elif la_ == 2:
                        localctx = HyamlParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 44
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 45
                        self.match(HyamlParser.COMP_OP)
                        self.state = 46
                        self.expr(10)
                        pass

                    elif la_ == 3:
                        localctx = HyamlParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 47
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 48
                        self.boolOperator()
                        self.state = 49
                        self.expr(9)
                        pass

                    elif la_ == 4:
                        localctx = HyamlParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 51
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 52
                        self.callChain()
                        pass

                    elif la_ == 5:
                        localctx = HyamlParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 53
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 54
                        self.subscription()
                        pass

             
                self.state = 59
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class LinkContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methodCall(self):
            return self.getTypedRuleContext(HyamlParser.MethodCallContext,0)


        def attribute(self):
            return self.getTypedRuleContext(HyamlParser.AttributeContext,0)


        def getRuleIndex(self):
            return HyamlParser.RULE_link

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLink" ):
                listener.enterLink(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLink" ):
                listener.exitLink(self)




    def link(self):

        localctx = HyamlParser.LinkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_link)
        try:
            self.state = 62
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.methodCall()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.attribute()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CallChainContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def link(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HyamlParser.LinkContext)
            else:
                return self.getTypedRuleContext(HyamlParser.LinkContext,i)


        def getRuleIndex(self):
            return HyamlParser.RULE_callChain

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallChain" ):
                listener.enterCallChain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallChain" ):
                listener.exitCallChain(self)




    def callChain(self):

        localctx = HyamlParser.CallChainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_callChain)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 64
                    self.link()

                else:
                    raise NoViableAltException(self)
                self.state = 67 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MethodCallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(HyamlParser.ID, 0)

        def arguments(self):
            return self.getTypedRuleContext(HyamlParser.ArgumentsContext,0)


        def PRED(self):
            return self.getToken(HyamlParser.PRED, 0)

        def getRuleIndex(self):
            return HyamlParser.RULE_methodCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodCall" ):
                listener.enterMethodCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodCall" ):
                listener.exitMethodCall(self)




    def methodCall(self):

        localctx = HyamlParser.MethodCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_methodCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(HyamlParser.T__2)
            self.state = 70
            self.match(HyamlParser.ID)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HyamlParser.PRED:
                self.state = 71
                self.match(HyamlParser.PRED)


            self.state = 74
            self.arguments()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AttributeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(HyamlParser.ID, 0)

        def getRuleIndex(self):
            return HyamlParser.RULE_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute" ):
                listener.enterAttribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute" ):
                listener.exitAttribute(self)




    def attribute(self):

        localctx = HyamlParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(HyamlParser.T__2)
            self.state = 77
            self.match(HyamlParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HyamlParser.ExprContext)
            else:
                return self.getTypedRuleContext(HyamlParser.ExprContext,i)


        def getRuleIndex(self):
            return HyamlParser.RULE_exprList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprList" ):
                listener.enterExprList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprList" ):
                listener.exitExprList(self)




    def exprList(self):

        localctx = HyamlParser.ExprListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_exprList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.expr(0)
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HyamlParser.T__3:
                self.state = 80
                self.match(HyamlParser.T__3)
                self.state = 81
                self.expr(0)
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgumentsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprList(self):
            return self.getTypedRuleContext(HyamlParser.ExprListContext,0)


        def getRuleIndex(self):
            return HyamlParser.RULE_arguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArguments" ):
                listener.enterArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArguments" ):
                listener.exitArguments(self)




    def arguments(self):

        localctx = HyamlParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(HyamlParser.T__0)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HyamlParser.T__0) | (1 << HyamlParser.T__4) | (1 << HyamlParser.TRUE) | (1 << HyamlParser.FALSE) | (1 << HyamlParser.NOT) | (1 << HyamlParser.NUMBER) | (1 << HyamlParser.VAR) | (1 << HyamlParser.EMPTY_HASH) | (1 << HyamlParser.STRING))) != 0):
                self.state = 88
                self.exprList()


            self.state = 91
            self.match(HyamlParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SubscriptionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(HyamlParser.ExprContext,0)


        def getRuleIndex(self):
            return HyamlParser.RULE_subscription

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubscription" ):
                listener.enterSubscription(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubscription" ):
                listener.exitSubscription(self)




    def subscription(self):

        localctx = HyamlParser.SubscriptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_subscription)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(HyamlParser.T__4)
            self.state = 94
            self.expr(0)
            self.state = 95
            self.match(HyamlParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BoolLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(HyamlParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(HyamlParser.FALSE, 0)

        def getRuleIndex(self):
            return HyamlParser.RULE_boolLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolLiteral" ):
                listener.enterBoolLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolLiteral" ):
                listener.exitBoolLiteral(self)




    def boolLiteral(self):

        localctx = HyamlParser.BoolLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_boolLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            _la = self._input.LA(1)
            if not(_la==HyamlParser.TRUE or _la==HyamlParser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BoolOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(HyamlParser.AND, 0)

        def OR(self):
            return self.getToken(HyamlParser.OR, 0)

        def getRuleIndex(self):
            return HyamlParser.RULE_boolOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolOperator" ):
                listener.enterBoolOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolOperator" ):
                listener.exitBoolOperator(self)




    def boolOperator(self):

        localctx = HyamlParser.BoolOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_boolOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            _la = self._input.LA(1)
            if not(_la==HyamlParser.AND or _la==HyamlParser.OR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ListLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprList(self):
            return self.getTypedRuleContext(HyamlParser.ExprListContext,0)


        def getRuleIndex(self):
            return HyamlParser.RULE_listLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListLiteral" ):
                listener.enterListLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListLiteral" ):
                listener.exitListLiteral(self)




    def listLiteral(self):

        localctx = HyamlParser.ListLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_listLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(HyamlParser.T__4)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HyamlParser.T__0) | (1 << HyamlParser.T__4) | (1 << HyamlParser.TRUE) | (1 << HyamlParser.FALSE) | (1 << HyamlParser.NOT) | (1 << HyamlParser.NUMBER) | (1 << HyamlParser.VAR) | (1 << HyamlParser.EMPTY_HASH) | (1 << HyamlParser.STRING))) != 0):
                self.state = 102
                self.exprList()


            self.state = 105
            self.match(HyamlParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         




