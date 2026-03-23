# Generated from hyaml/grammar/Hyaml.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,28,125,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,3,1,35,8,1,1,1,1,1,1,1,1,1,3,1,41,8,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        5,1,60,8,1,10,1,12,1,63,9,1,1,2,1,2,4,2,67,8,2,11,2,12,2,68,1,3,
        1,3,1,3,3,3,74,8,3,1,3,3,3,77,8,3,1,4,1,4,1,4,5,4,82,8,4,10,4,12,
        4,85,9,4,1,5,1,5,3,5,89,8,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,3,7,
        99,8,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,5,9,110,8,9,10,9,12,9,
        113,9,9,1,10,1,10,3,10,117,8,10,1,10,1,10,1,11,1,11,1,11,1,11,1,
        11,0,1,2,12,0,2,4,6,8,10,12,14,16,18,20,22,0,1,1,0,26,27,136,0,24,
        1,0,0,0,2,40,1,0,0,0,4,66,1,0,0,0,6,70,1,0,0,0,8,78,1,0,0,0,10,86,
        1,0,0,0,12,92,1,0,0,0,14,96,1,0,0,0,16,102,1,0,0,0,18,106,1,0,0,
        0,20,114,1,0,0,0,22,120,1,0,0,0,24,25,3,2,1,0,25,1,1,0,0,0,26,27,
        6,1,-1,0,27,41,3,22,11,0,28,29,5,14,0,0,29,41,3,2,1,10,30,41,3,14,
        7,0,31,41,3,20,10,0,32,41,5,21,0,0,33,35,5,15,0,0,34,33,1,0,0,0,
        34,35,1,0,0,0,35,36,1,0,0,0,36,41,5,16,0,0,37,41,5,24,0,0,38,41,
        5,10,0,0,39,41,5,11,0,0,40,26,1,0,0,0,40,28,1,0,0,0,40,30,1,0,0,
        0,40,31,1,0,0,0,40,32,1,0,0,0,40,34,1,0,0,0,40,37,1,0,0,0,40,38,
        1,0,0,0,40,39,1,0,0,0,41,61,1,0,0,0,42,43,10,13,0,0,43,44,5,17,0,
        0,44,60,3,2,1,14,45,46,10,12,0,0,46,47,5,15,0,0,47,60,3,2,1,13,48,
        49,10,11,0,0,49,50,5,18,0,0,50,60,3,2,1,12,51,52,10,9,0,0,52,53,
        5,12,0,0,53,60,3,2,1,10,54,55,10,8,0,0,55,56,5,13,0,0,56,60,3,2,
        1,9,57,58,10,14,0,0,58,60,3,4,2,0,59,42,1,0,0,0,59,45,1,0,0,0,59,
        48,1,0,0,0,59,51,1,0,0,0,59,54,1,0,0,0,59,57,1,0,0,0,60,63,1,0,0,
        0,61,59,1,0,0,0,61,62,1,0,0,0,62,3,1,0,0,0,63,61,1,0,0,0,64,67,3,
        6,3,0,65,67,3,12,6,0,66,64,1,0,0,0,66,65,1,0,0,0,67,68,1,0,0,0,68,
        66,1,0,0,0,68,69,1,0,0,0,69,5,1,0,0,0,70,71,7,0,0,0,71,76,5,20,0,
        0,72,74,5,28,0,0,73,72,1,0,0,0,73,74,1,0,0,0,74,75,1,0,0,0,75,77,
        3,10,5,0,76,73,1,0,0,0,76,77,1,0,0,0,77,7,1,0,0,0,78,83,3,2,1,0,
        79,80,5,1,0,0,80,82,3,2,1,0,81,79,1,0,0,0,82,85,1,0,0,0,83,81,1,
        0,0,0,83,84,1,0,0,0,84,9,1,0,0,0,85,83,1,0,0,0,86,88,5,2,0,0,87,
        89,3,8,4,0,88,87,1,0,0,0,88,89,1,0,0,0,89,90,1,0,0,0,90,91,5,3,0,
        0,91,11,1,0,0,0,92,93,5,4,0,0,93,94,3,2,1,0,94,95,5,5,0,0,95,13,
        1,0,0,0,96,98,5,4,0,0,97,99,3,8,4,0,98,97,1,0,0,0,98,99,1,0,0,0,
        99,100,1,0,0,0,100,101,5,5,0,0,101,15,1,0,0,0,102,103,5,20,0,0,103,
        104,5,6,0,0,104,105,3,2,1,0,105,17,1,0,0,0,106,111,3,16,8,0,107,
        108,5,1,0,0,108,110,3,16,8,0,109,107,1,0,0,0,110,113,1,0,0,0,111,
        109,1,0,0,0,111,112,1,0,0,0,112,19,1,0,0,0,113,111,1,0,0,0,114,116,
        5,7,0,0,115,117,3,18,9,0,116,115,1,0,0,0,116,117,1,0,0,0,117,118,
        1,0,0,0,118,119,5,8,0,0,119,21,1,0,0,0,120,121,5,2,0,0,121,122,3,
        2,1,0,122,123,5,3,0,0,123,23,1,0,0,0,13,34,40,59,61,66,68,73,76,
        83,88,98,111,116
    ]

class HyamlParser ( Parser ):

    grammarFileName = "Hyaml.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'('", "')'", "'['", "']'", "':'", 
                     "'{'", "'}'", "<INVALID>", "'true'", "'false'", "'and'", 
                     "'or'", "'not'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'?.'", "'.'", "'?'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NEWLINE", "TRUE", "FALSE", "AND", "OR", 
                      "NOT", "SIGN", "NUMBER", "MULT_DIV_OP", "COMP_OP", 
                      "ID_SYMBOL", "ID", "VAR", "LETTER", "DIGIT", "STRING", 
                      "WS", "SAFE_ACCESS", "ACCESS", "PRED" ]

    RULE_prog = 0
    RULE_expr = 1
    RULE_callChain = 2
    RULE_attributeOrDispatch = 3
    RULE_exprList = 4
    RULE_args = 5
    RULE_subscription = 6
    RULE_listLiteral = 7
    RULE_keyValuePair = 8
    RULE_keyValuePairs = 9
    RULE_dictLiteral = 10
    RULE_parens = 11

    ruleNames =  [ "prog", "expr", "callChain", "attributeOrDispatch", "exprList", 
                   "args", "subscription", "listLiteral", "keyValuePair", 
                   "keyValuePairs", "dictLiteral", "parens" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    NEWLINE=9
    TRUE=10
    FALSE=11
    AND=12
    OR=13
    NOT=14
    SIGN=15
    NUMBER=16
    MULT_DIV_OP=17
    COMP_OP=18
    ID_SYMBOL=19
    ID=20
    VAR=21
    LETTER=22
    DIGIT=23
    STRING=24
    WS=25
    SAFE_ACCESS=26
    ACCESS=27
    PRED=28

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parens(self):
            return self.getTypedRuleContext(HyamlParser.ParensContext,0)


        def NOT(self):
            return self.getToken(HyamlParser.NOT, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HyamlParser.ExprContext)
            else:
                return self.getTypedRuleContext(HyamlParser.ExprContext,i)


        def listLiteral(self):
            return self.getTypedRuleContext(HyamlParser.ListLiteralContext,0)


        def dictLiteral(self):
            return self.getTypedRuleContext(HyamlParser.DictLiteralContext,0)


        def VAR(self):
            return self.getToken(HyamlParser.VAR, 0)

        def NUMBER(self):
            return self.getToken(HyamlParser.NUMBER, 0)

        def SIGN(self):
            return self.getToken(HyamlParser.SIGN, 0)

        def STRING(self):
            return self.getToken(HyamlParser.STRING, 0)

        def TRUE(self):
            return self.getToken(HyamlParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(HyamlParser.FALSE, 0)

        def MULT_DIV_OP(self):
            return self.getToken(HyamlParser.MULT_DIV_OP, 0)

        def COMP_OP(self):
            return self.getToken(HyamlParser.COMP_OP, 0)

        def AND(self):
            return self.getToken(HyamlParser.AND, 0)

        def OR(self):
            return self.getToken(HyamlParser.OR, 0)

        def callChain(self):
            return self.getTypedRuleContext(HyamlParser.CallChainContext,0)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.state = 27
                self.parens()
                pass
            elif token in [14]:
                self.state = 28
                self.match(HyamlParser.NOT)
                self.state = 29
                self.expr(10)
                pass
            elif token in [4]:
                self.state = 30
                self.listLiteral()
                pass
            elif token in [7]:
                self.state = 31
                self.dictLiteral()
                pass
            elif token in [21]:
                self.state = 32
                self.match(HyamlParser.VAR)
                pass
            elif token in [15, 16]:
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==15:
                    self.state = 33
                    self.match(HyamlParser.SIGN)


                self.state = 36
                self.match(HyamlParser.NUMBER)
                pass
            elif token in [24]:
                self.state = 37
                self.match(HyamlParser.STRING)
                pass
            elif token in [10]:
                self.state = 38
                self.match(HyamlParser.TRUE)
                pass
            elif token in [11]:
                self.state = 39
                self.match(HyamlParser.FALSE)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 61
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 59
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = HyamlParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 42
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 43
                        self.match(HyamlParser.MULT_DIV_OP)
                        self.state = 44
                        self.expr(14)
                        pass

                    elif la_ == 2:
                        localctx = HyamlParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 45
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 46
                        self.match(HyamlParser.SIGN)
                        self.state = 47
                        self.expr(13)
                        pass

                    elif la_ == 3:
                        localctx = HyamlParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 48
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 49
                        self.match(HyamlParser.COMP_OP)
                        self.state = 50
                        self.expr(12)
                        pass

                    elif la_ == 4:
                        localctx = HyamlParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 51
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 52
                        self.match(HyamlParser.AND)
                        self.state = 53
                        self.expr(10)
                        pass

                    elif la_ == 5:
                        localctx = HyamlParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 54
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 55
                        self.match(HyamlParser.OR)
                        self.state = 56
                        self.expr(9)
                        pass

                    elif la_ == 6:
                        localctx = HyamlParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 57
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 58
                        self.callChain()
                        pass

             
                self.state = 63
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CallChainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributeOrDispatch(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HyamlParser.AttributeOrDispatchContext)
            else:
                return self.getTypedRuleContext(HyamlParser.AttributeOrDispatchContext,i)


        def subscription(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HyamlParser.SubscriptionContext)
            else:
                return self.getTypedRuleContext(HyamlParser.SubscriptionContext,i)


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
        self.enterRule(localctx, 4, self.RULE_callChain)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 66
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [26, 27]:
                        self.state = 64
                        self.attributeOrDispatch()
                        pass
                    elif token in [4]:
                        self.state = 65
                        self.subscription()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 68 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeOrDispatchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(HyamlParser.ID, 0)

        def SAFE_ACCESS(self):
            return self.getToken(HyamlParser.SAFE_ACCESS, 0)

        def ACCESS(self):
            return self.getToken(HyamlParser.ACCESS, 0)

        def args(self):
            return self.getTypedRuleContext(HyamlParser.ArgsContext,0)


        def PRED(self):
            return self.getToken(HyamlParser.PRED, 0)

        def getRuleIndex(self):
            return HyamlParser.RULE_attributeOrDispatch

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttributeOrDispatch" ):
                listener.enterAttributeOrDispatch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttributeOrDispatch" ):
                listener.exitAttributeOrDispatch(self)




    def attributeOrDispatch(self):

        localctx = HyamlParser.AttributeOrDispatchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_attributeOrDispatch)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            _la = self._input.LA(1)
            if not(_la==26 or _la==27):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 71
            self.match(HyamlParser.ID)
            self.state = 76
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==28:
                    self.state = 72
                    self.match(HyamlParser.PRED)


                self.state = 75
                self.args()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprListContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 8, self.RULE_exprList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.expr(0)
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 79
                self.match(HyamlParser.T__0)
                self.state = 80
                self.expr(0)
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprList(self):
            return self.getTypedRuleContext(HyamlParser.ExprListContext,0)


        def getRuleIndex(self):
            return HyamlParser.RULE_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgs" ):
                listener.enterArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgs" ):
                listener.exitArgs(self)




    def args(self):

        localctx = HyamlParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(HyamlParser.T__1)
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 18992276) != 0):
                self.state = 87
                self.exprList()


            self.state = 90
            self.match(HyamlParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubscriptionContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 12, self.RULE_subscription)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(HyamlParser.T__3)
            self.state = 93
            self.expr(0)
            self.state = 94
            self.match(HyamlParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 14, self.RULE_listLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(HyamlParser.T__3)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 18992276) != 0):
                self.state = 97
                self.exprList()


            self.state = 100
            self.match(HyamlParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyValuePairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(HyamlParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(HyamlParser.ExprContext,0)


        def getRuleIndex(self):
            return HyamlParser.RULE_keyValuePair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeyValuePair" ):
                listener.enterKeyValuePair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeyValuePair" ):
                listener.exitKeyValuePair(self)




    def keyValuePair(self):

        localctx = HyamlParser.KeyValuePairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_keyValuePair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(HyamlParser.ID)
            self.state = 103
            self.match(HyamlParser.T__5)
            self.state = 104
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyValuePairsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def keyValuePair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HyamlParser.KeyValuePairContext)
            else:
                return self.getTypedRuleContext(HyamlParser.KeyValuePairContext,i)


        def getRuleIndex(self):
            return HyamlParser.RULE_keyValuePairs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeyValuePairs" ):
                listener.enterKeyValuePairs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeyValuePairs" ):
                listener.exitKeyValuePairs(self)




    def keyValuePairs(self):

        localctx = HyamlParser.KeyValuePairsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_keyValuePairs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.keyValuePair()
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 107
                self.match(HyamlParser.T__0)
                self.state = 108
                self.keyValuePair()
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DictLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def keyValuePairs(self):
            return self.getTypedRuleContext(HyamlParser.KeyValuePairsContext,0)


        def getRuleIndex(self):
            return HyamlParser.RULE_dictLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDictLiteral" ):
                listener.enterDictLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDictLiteral" ):
                listener.exitDictLiteral(self)




    def dictLiteral(self):

        localctx = HyamlParser.DictLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_dictLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(HyamlParser.T__6)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 115
                self.keyValuePairs()


            self.state = 118
            self.match(HyamlParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParensContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(HyamlParser.ExprContext,0)


        def getRuleIndex(self):
            return HyamlParser.RULE_parens

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)




    def parens(self):

        localctx = HyamlParser.ParensContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_parens)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(HyamlParser.T__1)
            self.state = 121
            self.expr(0)
            self.state = 122
            self.match(HyamlParser.T__2)
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
                return self.precpred(self._ctx, 13)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 14)
         




