# Generated from pyToJava.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("U\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\5\3\37\n\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\7\4(\n")
        buf.write("\4\f\4\16\4+\13\4\3\5\3\5\3\6\6\6\60\n\6\r\6\16\6\61\3")
        buf.write("\7\3\7\3\7\5\7\67\n\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\13\3\13\3\13\5\13H\n\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\7\13P\n\13\f\13\16\13S\13\13\3\13\2")
        buf.write("\3\24\f\2\4\6\b\n\f\16\20\22\24\2\2\2R\2\26\3\2\2\2\4")
        buf.write("\32\3\2\2\2\6$\3\2\2\2\b,\3\2\2\2\n/\3\2\2\2\f\66\3\2")
        buf.write("\2\2\168\3\2\2\2\20<\3\2\2\2\22?\3\2\2\2\24G\3\2\2\2\26")
        buf.write("\27\5\4\3\2\27\30\5\f\7\2\30\31\7\2\2\3\31\3\3\2\2\2\32")
        buf.write("\33\7\4\2\2\33\34\7\r\2\2\34\36\7\t\2\2\35\37\5\6\4\2")
        buf.write("\36\35\3\2\2\2\36\37\3\2\2\2\37 \3\2\2\2 !\7\n\2\2!\"")
        buf.write("\7\13\2\2\"#\5\n\6\2#\5\3\2\2\2$)\5\b\5\2%&\7\f\2\2&(")
        buf.write("\5\b\5\2\'%\3\2\2\2(+\3\2\2\2)\'\3\2\2\2)*\3\2\2\2*\7")
        buf.write("\3\2\2\2+)\3\2\2\2,-\7\r\2\2-\t\3\2\2\2.\60\5\f\7\2/.")
        buf.write("\3\2\2\2\60\61\3\2\2\2\61/\3\2\2\2\61\62\3\2\2\2\62\13")
        buf.write("\3\2\2\2\63\67\5\16\b\2\64\67\5\20\t\2\65\67\5\22\n\2")
        buf.write("\66\63\3\2\2\2\66\64\3\2\2\2\66\65\3\2\2\2\67\r\3\2\2")
        buf.write("\289\7\r\2\29:\7\3\2\2:;\5\24\13\2;\17\3\2\2\2<=\7\5\2")
        buf.write("\2=>\5\24\13\2>\21\3\2\2\2?@\7\6\2\2@A\7\t\2\2AB\5\24")
        buf.write("\13\2BC\7\n\2\2C\23\3\2\2\2DE\b\13\1\2EH\7\r\2\2FH\7\16")
        buf.write("\2\2GD\3\2\2\2GF\3\2\2\2HQ\3\2\2\2IJ\f\6\2\2JK\7\7\2\2")
        buf.write("KP\5\24\13\7LM\f\5\2\2MN\7\b\2\2NP\5\24\13\6OI\3\2\2\2")
        buf.write("OL\3\2\2\2PS\3\2\2\2QO\3\2\2\2QR\3\2\2\2R\25\3\2\2\2S")
        buf.write("Q\3\2\2\2\t\36)\61\66GOQ")
        return buf.getvalue()


class pyToJavaParser ( Parser ):

    grammarFileName = "pyToJava.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'def'", "'return'", "'print'", 
                     "'*'", "'-'", "'('", "')'", "':'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "DEF", "RETURN", "PRINT", 
                      "MUL", "SUB", "LPAREN", "RPAREN", "COLON", "COMMA", 
                      "ID", "INT", "WS" ]

    RULE_program = 0
    RULE_functionDefinition = 1
    RULE_parameters = 2
    RULE_parameter = 3
    RULE_block = 4
    RULE_statement = 5
    RULE_assignment = 6
    RULE_returnStatement = 7
    RULE_printStatement = 8
    RULE_expression = 9

    ruleNames =  [ "program", "functionDefinition", "parameters", "parameter", 
                   "block", "statement", "assignment", "returnStatement", 
                   "printStatement", "expression" ]

    EOF = Token.EOF
    T__0=1
    DEF=2
    RETURN=3
    PRINT=4
    MUL=5
    SUB=6
    LPAREN=7
    RPAREN=8
    COLON=9
    COMMA=10
    ID=11
    INT=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionDefinition(self):
            return self.getTypedRuleContext(pyToJavaParser.FunctionDefinitionContext,0)


        def statement(self):
            return self.getTypedRuleContext(pyToJavaParser.StatementContext,0)


        def EOF(self):
            return self.getToken(pyToJavaParser.EOF, 0)

        def getRuleIndex(self):
            return pyToJavaParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = pyToJavaParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.functionDefinition()
            self.state = 21
            self.statement()
            self.state = 22
            self.match(pyToJavaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionDefinitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(pyToJavaParser.DEF, 0)

        def ID(self):
            return self.getToken(pyToJavaParser.ID, 0)

        def LPAREN(self):
            return self.getToken(pyToJavaParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(pyToJavaParser.RPAREN, 0)

        def COLON(self):
            return self.getToken(pyToJavaParser.COLON, 0)

        def block(self):
            return self.getTypedRuleContext(pyToJavaParser.BlockContext,0)


        def parameters(self):
            return self.getTypedRuleContext(pyToJavaParser.ParametersContext,0)


        def getRuleIndex(self):
            return pyToJavaParser.RULE_functionDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDefinition" ):
                listener.enterFunctionDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDefinition" ):
                listener.exitFunctionDefinition(self)




    def functionDefinition(self):

        localctx = pyToJavaParser.FunctionDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_functionDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(pyToJavaParser.DEF)
            self.state = 25
            self.match(pyToJavaParser.ID)
            self.state = 26
            self.match(pyToJavaParser.LPAREN)
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==pyToJavaParser.ID:
                self.state = 27
                self.parameters()


            self.state = 30
            self.match(pyToJavaParser.RPAREN)
            self.state = 31
            self.match(pyToJavaParser.COLON)
            self.state = 32
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParametersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pyToJavaParser.ParameterContext)
            else:
                return self.getTypedRuleContext(pyToJavaParser.ParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(pyToJavaParser.COMMA)
            else:
                return self.getToken(pyToJavaParser.COMMA, i)

        def getRuleIndex(self):
            return pyToJavaParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)




    def parameters(self):

        localctx = pyToJavaParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.parameter()
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==pyToJavaParser.COMMA:
                self.state = 35
                self.match(pyToJavaParser.COMMA)
                self.state = 36
                self.parameter()
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(pyToJavaParser.ID, 0)

        def getRuleIndex(self):
            return pyToJavaParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)




    def parameter(self):

        localctx = pyToJavaParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(pyToJavaParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pyToJavaParser.StatementContext)
            else:
                return self.getTypedRuleContext(pyToJavaParser.StatementContext,i)


        def getRuleIndex(self):
            return pyToJavaParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = pyToJavaParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 44
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 47 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(pyToJavaParser.AssignmentContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(pyToJavaParser.ReturnStatementContext,0)


        def printStatement(self):
            return self.getTypedRuleContext(pyToJavaParser.PrintStatementContext,0)


        def getRuleIndex(self):
            return pyToJavaParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = pyToJavaParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_statement)
        try:
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pyToJavaParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.assignment()
                pass
            elif token in [pyToJavaParser.RETURN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.returnStatement()
                pass
            elif token in [pyToJavaParser.PRINT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 51
                self.printStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(pyToJavaParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(pyToJavaParser.ExpressionContext,0)


        def getRuleIndex(self):
            return pyToJavaParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = pyToJavaParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(pyToJavaParser.ID)
            self.state = 55
            self.match(pyToJavaParser.T__0)
            self.state = 56
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ReturnStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(pyToJavaParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(pyToJavaParser.ExpressionContext,0)


        def getRuleIndex(self):
            return pyToJavaParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)




    def returnStatement(self):

        localctx = pyToJavaParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(pyToJavaParser.RETURN)
            self.state = 59
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PrintStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(pyToJavaParser.PRINT, 0)

        def LPAREN(self):
            return self.getToken(pyToJavaParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(pyToJavaParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(pyToJavaParser.RPAREN, 0)

        def getRuleIndex(self):
            return pyToJavaParser.RULE_printStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStatement" ):
                listener.enterPrintStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStatement" ):
                listener.exitPrintStatement(self)




    def printStatement(self):

        localctx = pyToJavaParser.PrintStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_printStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(pyToJavaParser.PRINT)
            self.state = 62
            self.match(pyToJavaParser.LPAREN)
            self.state = 63
            self.expression(0)
            self.state = 64
            self.match(pyToJavaParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return pyToJavaParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class IntExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pyToJavaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(pyToJavaParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntExpression" ):
                listener.enterIntExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntExpression" ):
                listener.exitIntExpression(self)


    class IdExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pyToJavaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(pyToJavaParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdExpression" ):
                listener.enterIdExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdExpression" ):
                listener.exitIdExpression(self)


    class SubExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pyToJavaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pyToJavaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(pyToJavaParser.ExpressionContext,i)

        def SUB(self):
            return self.getToken(pyToJavaParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubExpression" ):
                listener.enterSubExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubExpression" ):
                listener.exitSubExpression(self)


    class MulExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pyToJavaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pyToJavaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(pyToJavaParser.ExpressionContext,i)

        def MUL(self):
            return self.getToken(pyToJavaParser.MUL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulExpression" ):
                listener.enterMulExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulExpression" ):
                listener.exitMulExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = pyToJavaParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pyToJavaParser.ID]:
                localctx = pyToJavaParser.IdExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 67
                self.match(pyToJavaParser.ID)
                pass
            elif token in [pyToJavaParser.INT]:
                localctx = pyToJavaParser.IntExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 68
                self.match(pyToJavaParser.INT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 79
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 77
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = pyToJavaParser.MulExpressionContext(self, pyToJavaParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 71
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 72
                        self.match(pyToJavaParser.MUL)
                        self.state = 73
                        self.expression(5)
                        pass

                    elif la_ == 2:
                        localctx = pyToJavaParser.SubExpressionContext(self, pyToJavaParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 74
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 75
                        self.match(pyToJavaParser.SUB)
                        self.state = 76
                        self.expression(4)
                        pass

             
                self.state = 81
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[9] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         




