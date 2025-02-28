# Generated from PytoJava.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("O\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\5\6\5\60\n\5\r\5\16\5\61\3\6\3")
        buf.write("\6\7\6\66\n\6\f\6\16\69\13\6\3\7\3\7\3\b\3\b\3\t\3\t\3")
        buf.write("\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\6\16J\n\16\r\16")
        buf.write("\16\16K\3\16\3\16\2\2\17\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\3\2\6\3\2\62;\4\2C\\")
        buf.write("c|\5\2\62;C\\c|\5\2\13\f\17\17\"\"\2Q\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\3\35\3\2\2\2")
        buf.write("\5!\3\2\2\2\7(\3\2\2\2\t/\3\2\2\2\13\63\3\2\2\2\r:\3\2")
        buf.write("\2\2\17<\3\2\2\2\21>\3\2\2\2\23@\3\2\2\2\25B\3\2\2\2\27")
        buf.write("D\3\2\2\2\31F\3\2\2\2\33I\3\2\2\2\35\36\7f\2\2\36\37\7")
        buf.write("g\2\2\37 \7h\2\2 \4\3\2\2\2!\"\7t\2\2\"#\7g\2\2#$\7v\2")
        buf.write("\2$%\7w\2\2%&\7t\2\2&\'\7p\2\2\'\6\3\2\2\2()\7r\2\2)*")
        buf.write("\7t\2\2*+\7k\2\2+,\7p\2\2,-\7v\2\2-\b\3\2\2\2.\60\t\2")
        buf.write("\2\2/.\3\2\2\2\60\61\3\2\2\2\61/\3\2\2\2\61\62\3\2\2\2")
        buf.write("\62\n\3\2\2\2\63\67\t\3\2\2\64\66\t\4\2\2\65\64\3\2\2")
        buf.write("\2\669\3\2\2\2\67\65\3\2\2\2\678\3\2\2\28\f\3\2\2\29\67")
        buf.write("\3\2\2\2:;\7/\2\2;\16\3\2\2\2<=\7,\2\2=\20\3\2\2\2>?\7")
        buf.write("?\2\2?\22\3\2\2\2@A\7*\2\2A\24\3\2\2\2BC\7+\2\2C\26\3")
        buf.write("\2\2\2DE\7<\2\2E\30\3\2\2\2FG\7.\2\2G\32\3\2\2\2HJ\t\5")
        buf.write("\2\2IH\3\2\2\2JK\3\2\2\2KI\3\2\2\2KL\3\2\2\2LM\3\2\2\2")
        buf.write("MN\b\16\2\2N\34\3\2\2\2\6\2\61\67K\3\b\2\2")
        return buf.getvalue()


class PytoJavaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    DEF = 1
    RETURN = 2
    PRINT = 3
    NUMBER = 4
    IDENT = 5
    MINUS = 6
    MULTIPLY = 7
    ASSIGN = 8
    LPAREN = 9
    RPAREN = 10
    COLON = 11
    COMMA = 12
    WS = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'def'", "'return'", "'print'", "'-'", "'*'", "'='", "'('", 
            "')'", "':'", "','" ]

    symbolicNames = [ "<INVALID>",
            "DEF", "RETURN", "PRINT", "NUMBER", "IDENT", "MINUS", "MULTIPLY", 
            "ASSIGN", "LPAREN", "RPAREN", "COLON", "COMMA", "WS" ]

    ruleNames = [ "DEF", "RETURN", "PRINT", "NUMBER", "IDENT", "MINUS", 
                  "MULTIPLY", "ASSIGN", "LPAREN", "RPAREN", "COLON", "COMMA", 
                  "WS" ]

    grammarFileName = "PytoJava.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


