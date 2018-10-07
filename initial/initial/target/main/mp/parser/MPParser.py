# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3:")
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5")
        buf.write("\3\2\2\2\5\3\3\2\2\2\2")
        return buf.getvalue()


class MPParser ( Parser ):

    grammarFileName = "MP.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'+'", "'*'", "'<>'", "'<'", "'<='", "'-'", 
                     "'/'", "'='", "'>'", "'>='", "<INVALID>", "<INVALID>", 
                     "'['", "']'", "':'", "'('", "')'", "';'", "'..'", "','" ]

    symbolicNames = [ "<INVALID>", "TRADI_CMT", "BLOCK_CMT", "LINE_CMT", 
                      "BREAK", "CONTINUE", "FOR", "TO", "DOWNTO", "DO", 
                      "IF", "THEN", "ELSE", "RETURN", "WHILE", "BEGIN", 
                      "END", "FUNCTION", "PROCEDURE", "VAR", "TRUE", "FALSE", 
                      "ARRAY", "OF", "REAL", "BOOLEAN", "INTEGER", "STRING", 
                      "NOT", "AND", "OR", "DIV", "MOD", "ADD", "MUL", "NOTEQUAL", 
                      "LESSTHAN", "LESSEQUAL", "SUB", "DIVISION", "EQUA", 
                      "GREATERTHAN", "GREATEREQUAL", "ID", "WS", "LSB", 
                      "RSB", "COLON", "LB", "RB", "SEMI", "DD", "COMMA", 
                      "INTLIT", "FLOATLIT", "BOOLEANLIT", "STRLIT" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    TRADI_CMT=1
    BLOCK_CMT=2
    LINE_CMT=3
    BREAK=4
    CONTINUE=5
    FOR=6
    TO=7
    DOWNTO=8
    DO=9
    IF=10
    THEN=11
    ELSE=12
    RETURN=13
    WHILE=14
    BEGIN=15
    END=16
    FUNCTION=17
    PROCEDURE=18
    VAR=19
    TRUE=20
    FALSE=21
    ARRAY=22
    OF=23
    REAL=24
    BOOLEAN=25
    INTEGER=26
    STRING=27
    NOT=28
    AND=29
    OR=30
    DIV=31
    MOD=32
    ADD=33
    MUL=34
    NOTEQUAL=35
    LESSTHAN=36
    LESSEQUAL=37
    SUB=38
    DIVISION=39
    EQUA=40
    GREATERTHAN=41
    GREATEREQUAL=42
    ID=43
    WS=44
    LSB=45
    RSB=46
    COLON=47
    LB=48
    RB=49
    SEMI=50
    DD=51
    COMMA=52
    INTLIT=53
    FLOATLIT=54
    BOOLEANLIT=55
    STRLIT=56

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MPParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MPParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





