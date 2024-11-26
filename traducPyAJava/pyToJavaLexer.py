# Generated from pyToJava.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("O\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3")
        buf.write("\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\7\f?\n\f\f\f\16\fB\13")
        buf.write("\f\3\r\6\rE\n\r\r\r\16\rF\3\16\6\16J\n\16\r\16\16\16K")
        buf.write("\3\16\3\16\2\2\17\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\3\2\6\5\2C\\aac|\6\2\62;C\\")
        buf.write("aac|\3\2\62;\5\2\13\f\17\17\"\"\2Q\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\3\35\3\2\2\2\5\37")
        buf.write("\3\2\2\2\7#\3\2\2\2\t*\3\2\2\2\13\60\3\2\2\2\r\62\3\2")
        buf.write("\2\2\17\64\3\2\2\2\21\66\3\2\2\2\238\3\2\2\2\25:\3\2\2")
        buf.write("\2\27<\3\2\2\2\31D\3\2\2\2\33I\3\2\2\2\35\36\7?\2\2\36")
        buf.write("\4\3\2\2\2\37 \7f\2\2 !\7g\2\2!\"\7h\2\2\"\6\3\2\2\2#")
        buf.write("$\7t\2\2$%\7g\2\2%&\7v\2\2&\'\7w\2\2\'(\7t\2\2()\7p\2")
        buf.write("\2)\b\3\2\2\2*+\7r\2\2+,\7t\2\2,-\7k\2\2-.\7p\2\2./\7")
        buf.write("v\2\2/\n\3\2\2\2\60\61\7,\2\2\61\f\3\2\2\2\62\63\7/\2")
        buf.write("\2\63\16\3\2\2\2\64\65\7*\2\2\65\20\3\2\2\2\66\67\7+\2")
        buf.write("\2\67\22\3\2\2\289\7<\2\29\24\3\2\2\2:;\7.\2\2;\26\3\2")
        buf.write("\2\2<@\t\2\2\2=?\t\3\2\2>=\3\2\2\2?B\3\2\2\2@>\3\2\2\2")
        buf.write("@A\3\2\2\2A\30\3\2\2\2B@\3\2\2\2CE\t\4\2\2DC\3\2\2\2E")
        buf.write("F\3\2\2\2FD\3\2\2\2FG\3\2\2\2G\32\3\2\2\2HJ\t\5\2\2IH")
        buf.write("\3\2\2\2JK\3\2\2\2KI\3\2\2\2KL\3\2\2\2LM\3\2\2\2MN\b\16")
        buf.write("\2\2N\34\3\2\2\2\6\2@FK\3\b\2\2")
        return buf.getvalue()


class pyToJavaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    DEF = 2
    RETURN = 3
    PRINT = 4
    MUL = 5
    SUB = 6
    LPAREN = 7
    RPAREN = 8
    COLON = 9
    COMMA = 10
    ID = 11
    INT = 12
    WS = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'def'", "'return'", "'print'", "'*'", "'-'", "'('", 
            "')'", "':'", "','" ]

    symbolicNames = [ "<INVALID>",
            "DEF", "RETURN", "PRINT", "MUL", "SUB", "LPAREN", "RPAREN", 
            "COLON", "COMMA", "ID", "INT", "WS" ]

    ruleNames = [ "T__0", "DEF", "RETURN", "PRINT", "MUL", "SUB", "LPAREN", 
                  "RPAREN", "COLON", "COMMA", "ID", "INT", "WS" ]

    grammarFileName = "pyToJava.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


