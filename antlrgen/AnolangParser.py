# Generated from ./antlrgen/Anolang.g4 by ANTLR 4.13.2
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
        4,1,44,282,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,1,0,5,0,60,8,0,10,0,12,0,63,9,0,1,0,1,0,1,1,
        1,1,3,1,69,8,1,1,1,1,1,1,1,5,1,74,8,1,10,1,12,1,77,9,1,5,1,79,8,
        1,10,1,12,1,82,9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,91,8,1,10,1,12,
        1,94,9,1,3,1,96,8,1,1,1,1,1,1,1,3,1,101,8,1,1,2,1,2,3,2,105,8,2,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,
        122,8,3,1,4,1,4,1,5,1,5,1,5,1,6,1,6,5,6,131,8,6,10,6,12,6,134,9,
        6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,3,7,143,8,7,1,7,1,7,1,8,1,8,1,8,1,
        8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,
        11,1,11,1,11,1,11,3,11,168,8,11,1,12,1,12,1,12,1,12,1,12,1,13,1,
        13,1,13,1,13,5,13,179,8,13,10,13,12,13,182,9,13,1,13,1,13,1,14,1,
        14,1,14,3,14,189,8,14,1,14,1,14,1,14,3,14,194,8,14,5,14,196,8,14,
        10,14,12,14,199,9,14,1,14,1,14,1,15,1,15,1,15,1,15,3,15,207,8,15,
        1,16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,18,1,18,1,18,
        1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,3,19,241,8,19,1,20,1,20,1,20,3,20,
        246,8,20,1,20,1,20,1,21,1,21,1,21,5,21,253,8,21,10,21,12,21,256,
        9,21,1,22,1,22,3,22,260,8,22,1,23,1,23,1,24,1,24,1,25,1,25,1,26,
        1,26,1,26,1,26,1,26,1,26,1,26,1,26,3,26,276,8,26,1,27,1,27,1,28,
        1,28,1,28,0,0,29,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,50,52,54,56,0,4,1,0,20,21,1,0,22,23,3,0,18,
        18,22,22,24,36,1,0,40,42,293,0,61,1,0,0,0,2,100,1,0,0,0,4,104,1,
        0,0,0,6,121,1,0,0,0,8,123,1,0,0,0,10,125,1,0,0,0,12,128,1,0,0,0,
        14,137,1,0,0,0,16,146,1,0,0,0,18,150,1,0,0,0,20,154,1,0,0,0,22,160,
        1,0,0,0,24,169,1,0,0,0,26,174,1,0,0,0,28,185,1,0,0,0,30,206,1,0,
        0,0,32,208,1,0,0,0,34,214,1,0,0,0,36,218,1,0,0,0,38,240,1,0,0,0,
        40,242,1,0,0,0,42,249,1,0,0,0,44,257,1,0,0,0,46,261,1,0,0,0,48,263,
        1,0,0,0,50,265,1,0,0,0,52,275,1,0,0,0,54,277,1,0,0,0,56,279,1,0,
        0,0,58,60,3,2,1,0,59,58,1,0,0,0,60,63,1,0,0,0,61,59,1,0,0,0,61,62,
        1,0,0,0,62,64,1,0,0,0,63,61,1,0,0,0,64,65,5,0,0,1,65,1,1,0,0,0,66,
        68,3,56,28,0,67,69,3,54,27,0,68,67,1,0,0,0,68,69,1,0,0,0,69,80,1,
        0,0,0,70,75,3,4,2,0,71,72,5,1,0,0,72,74,3,4,2,0,73,71,1,0,0,0,74,
        77,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,
        0,78,70,1,0,0,0,79,82,1,0,0,0,80,78,1,0,0,0,80,81,1,0,0,0,81,83,
        1,0,0,0,82,80,1,0,0,0,83,84,5,2,0,0,84,101,1,0,0,0,85,86,3,56,28,
        0,86,95,5,3,0,0,87,92,3,56,28,0,88,89,5,1,0,0,89,91,3,56,28,0,90,
        88,1,0,0,0,91,94,1,0,0,0,92,90,1,0,0,0,92,93,1,0,0,0,93,96,1,0,0,
        0,94,92,1,0,0,0,95,87,1,0,0,0,95,96,1,0,0,0,96,97,1,0,0,0,97,98,
        5,4,0,0,98,99,3,6,3,0,99,101,1,0,0,0,100,66,1,0,0,0,100,85,1,0,0,
        0,101,3,1,0,0,0,102,105,3,54,27,0,103,105,3,56,28,0,104,102,1,0,
        0,0,104,103,1,0,0,0,105,5,1,0,0,0,106,122,3,26,13,0,107,122,3,28,
        14,0,108,109,3,56,28,0,109,110,5,5,0,0,110,111,3,6,3,0,111,122,1,
        0,0,0,112,122,3,24,12,0,113,122,3,12,6,0,114,122,3,22,11,0,115,122,
        3,20,10,0,116,122,3,18,9,0,117,122,3,16,8,0,118,122,3,14,7,0,119,
        122,3,10,5,0,120,122,3,8,4,0,121,106,1,0,0,0,121,107,1,0,0,0,121,
        108,1,0,0,0,121,112,1,0,0,0,121,113,1,0,0,0,121,114,1,0,0,0,121,
        115,1,0,0,0,121,116,1,0,0,0,121,117,1,0,0,0,121,118,1,0,0,0,121,
        119,1,0,0,0,121,120,1,0,0,0,122,7,1,0,0,0,123,124,5,2,0,0,124,9,
        1,0,0,0,125,126,3,30,15,0,126,127,5,2,0,0,127,11,1,0,0,0,128,132,
        5,6,0,0,129,131,3,6,3,0,130,129,1,0,0,0,131,134,1,0,0,0,132,130,
        1,0,0,0,132,133,1,0,0,0,133,135,1,0,0,0,134,132,1,0,0,0,135,136,
        5,7,0,0,136,13,1,0,0,0,137,142,5,8,0,0,138,139,5,3,0,0,139,140,3,
        30,15,0,140,141,5,4,0,0,141,143,1,0,0,0,142,138,1,0,0,0,142,143,
        1,0,0,0,143,144,1,0,0,0,144,145,5,2,0,0,145,15,1,0,0,0,146,147,5,
        9,0,0,147,148,3,30,15,0,148,149,5,2,0,0,149,17,1,0,0,0,150,151,5,
        10,0,0,151,152,3,30,15,0,152,153,3,6,3,0,153,19,1,0,0,0,154,155,
        5,11,0,0,155,156,5,3,0,0,156,157,3,30,15,0,157,158,5,4,0,0,158,159,
        3,6,3,0,159,21,1,0,0,0,160,161,5,12,0,0,161,162,5,3,0,0,162,163,
        3,30,15,0,163,164,5,4,0,0,164,167,3,6,3,0,165,166,5,13,0,0,166,168,
        3,6,3,0,167,165,1,0,0,0,167,168,1,0,0,0,168,23,1,0,0,0,169,170,5,
        14,0,0,170,171,3,54,27,0,171,172,5,5,0,0,172,173,3,6,3,0,173,25,
        1,0,0,0,174,175,5,15,0,0,175,180,3,56,28,0,176,177,5,1,0,0,177,179,
        3,56,28,0,178,176,1,0,0,0,179,182,1,0,0,0,180,178,1,0,0,0,180,181,
        1,0,0,0,181,183,1,0,0,0,182,180,1,0,0,0,183,184,5,2,0,0,184,27,1,
        0,0,0,185,186,5,16,0,0,186,188,3,56,28,0,187,189,3,54,27,0,188,187,
        1,0,0,0,188,189,1,0,0,0,189,197,1,0,0,0,190,191,5,1,0,0,191,193,
        3,56,28,0,192,194,3,54,27,0,193,192,1,0,0,0,193,194,1,0,0,0,194,
        196,1,0,0,0,195,190,1,0,0,0,196,199,1,0,0,0,197,195,1,0,0,0,197,
        198,1,0,0,0,198,200,1,0,0,0,199,197,1,0,0,0,200,201,5,2,0,0,201,
        29,1,0,0,0,202,207,3,38,19,0,203,207,3,34,17,0,204,207,3,32,16,0,
        205,207,3,36,18,0,206,202,1,0,0,0,206,203,1,0,0,0,206,204,1,0,0,
        0,206,205,1,0,0,0,207,31,1,0,0,0,208,209,3,38,19,0,209,210,5,17,
        0,0,210,211,3,30,15,0,211,212,5,5,0,0,212,213,3,30,15,0,213,33,1,
        0,0,0,214,215,3,38,19,0,215,216,3,50,25,0,216,217,3,30,15,0,217,
        35,1,0,0,0,218,219,3,56,28,0,219,220,3,44,22,0,220,221,3,30,15,0,
        221,37,1,0,0,0,222,223,5,3,0,0,223,224,3,30,15,0,224,225,5,4,0,0,
        225,241,1,0,0,0,226,241,3,56,28,0,227,241,3,54,27,0,228,229,3,46,
        23,0,229,230,3,56,28,0,230,241,1,0,0,0,231,232,3,56,28,0,232,233,
        3,46,23,0,233,241,1,0,0,0,234,235,3,48,24,0,235,236,3,30,15,0,236,
        241,1,0,0,0,237,238,5,18,0,0,238,241,3,56,28,0,239,241,3,40,20,0,
        240,222,1,0,0,0,240,226,1,0,0,0,240,227,1,0,0,0,240,228,1,0,0,0,
        240,231,1,0,0,0,240,234,1,0,0,0,240,237,1,0,0,0,240,239,1,0,0,0,
        241,39,1,0,0,0,242,243,3,56,28,0,243,245,5,3,0,0,244,246,3,42,21,
        0,245,244,1,0,0,0,245,246,1,0,0,0,246,247,1,0,0,0,247,248,5,4,0,
        0,248,41,1,0,0,0,249,254,3,30,15,0,250,251,5,1,0,0,251,253,3,30,
        15,0,252,250,1,0,0,0,253,256,1,0,0,0,254,252,1,0,0,0,254,255,1,0,
        0,0,255,43,1,0,0,0,256,254,1,0,0,0,257,259,5,19,0,0,258,260,3,50,
        25,0,259,258,1,0,0,0,259,260,1,0,0,0,260,45,1,0,0,0,261,262,7,0,
        0,0,262,47,1,0,0,0,263,264,7,1,0,0,264,49,1,0,0,0,265,266,7,2,0,
        0,266,51,1,0,0,0,267,276,3,56,28,0,268,269,5,35,0,0,269,276,3,30,
        15,0,270,271,3,30,15,0,271,272,5,37,0,0,272,273,3,30,15,0,273,274,
        5,38,0,0,274,276,1,0,0,0,275,267,1,0,0,0,275,268,1,0,0,0,275,270,
        1,0,0,0,276,53,1,0,0,0,277,278,7,3,0,0,278,55,1,0,0,0,279,280,5,
        39,0,0,280,57,1,0,0,0,22,61,68,75,80,92,95,100,104,121,132,142,167,
        180,188,193,197,206,240,245,254,259,275
    ]

class AnolangParser ( Parser ):

    grammarFileName = "Anolang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "';'", "'('", "')'", "':'", "'{'", 
                     "'}'", "'return'", "'goto'", "'switch'", "'while'", 
                     "'if'", "'else'", "'case'", "'extrn'", "'auto'", "'?'", 
                     "'&'", "'='", "'++'", "'--'", "'-'", "'!'", "'|'", 
                     "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'<<'", 
                     "'>>'", "'+'", "'%'", "'*'", "'/'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NAME", "INT", 
                      "STRING1", "STRING2", "BLOCKCOMMENT", "WS" ]

    RULE_ano_program = 0
    RULE_definition = 1
    RULE_ival = 2
    RULE_statement = 3
    RULE_nullstmt = 4
    RULE_expressionstmt = 5
    RULE_blockstmt = 6
    RULE_returnstmt = 7
    RULE_gotostmt = 8
    RULE_switchstmt = 9
    RULE_whilestmt = 10
    RULE_ifstmt = 11
    RULE_casestmt = 12
    RULE_externsmt = 13
    RULE_autosmt = 14
    RULE_rvalue = 15
    RULE_ternary = 16
    RULE_comparison = 17
    RULE_assignment = 18
    RULE_expression = 19
    RULE_functioninvocation = 20
    RULE_functionparameters = 21
    RULE_assign = 22
    RULE_incdec = 23
    RULE_unary = 24
    RULE_binary = 25
    RULE_lvalue = 26
    RULE_constant = 27
    RULE_identity = 28

    ruleNames =  [ "ano_program", "definition", "ival", "statement", "nullstmt", 
                   "expressionstmt", "blockstmt", "returnstmt", "gotostmt", 
                   "switchstmt", "whilestmt", "ifstmt", "casestmt", "externsmt", 
                   "autosmt", "rvalue", "ternary", "comparison", "assignment", 
                   "expression", "functioninvocation", "functionparameters", 
                   "assign", "incdec", "unary", "binary", "lvalue", "constant", 
                   "identity" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    NAME=39
    INT=40
    STRING1=41
    STRING2=42
    BLOCKCOMMENT=43
    WS=44

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Ano_programContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(AnolangParser.EOF, 0)

        def definition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AnolangParser.DefinitionContext)
            else:
                return self.getTypedRuleContext(AnolangParser.DefinitionContext,i)


        def getRuleIndex(self):
            return AnolangParser.RULE_ano_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAno_program" ):
                listener.enterAno_program(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAno_program" ):
                listener.exitAno_program(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAno_program" ):
                return visitor.visitAno_program(self)
            else:
                return visitor.visitChildren(self)




    def ano_program(self):

        localctx = AnolangParser.Ano_programContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_ano_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==39:
                self.state = 58
                self.definition()
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
            self.match(AnolangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identity(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AnolangParser.IdentityContext)
            else:
                return self.getTypedRuleContext(AnolangParser.IdentityContext,i)


        def constant(self):
            return self.getTypedRuleContext(AnolangParser.ConstantContext,0)


        def ival(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AnolangParser.IvalContext)
            else:
                return self.getTypedRuleContext(AnolangParser.IvalContext,i)


        def statement(self):
            return self.getTypedRuleContext(AnolangParser.StatementContext,0)


        def getRuleIndex(self):
            return AnolangParser.RULE_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefinition" ):
                listener.enterDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefinition" ):
                listener.exitDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinition" ):
                return visitor.visitDefinition(self)
            else:
                return visitor.visitChildren(self)




    def definition(self):

        localctx = AnolangParser.DefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_definition)
        self._la = 0 # Token type
        try:
            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.identity()
                self.state = 68
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 67
                    self.constant()


                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8246337208320) != 0):
                    self.state = 70
                    self.ival()
                    self.state = 75
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1:
                        self.state = 71
                        self.match(AnolangParser.T__0)
                        self.state = 72
                        self.ival()
                        self.state = 77
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 82
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 83
                self.match(AnolangParser.T__1)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.identity()
                self.state = 86
                self.match(AnolangParser.T__2)
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==39:
                    self.state = 87
                    self.identity()
                    self.state = 92
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1:
                        self.state = 88
                        self.match(AnolangParser.T__0)
                        self.state = 89
                        self.identity()
                        self.state = 94
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 97
                self.match(AnolangParser.T__3)
                self.state = 98
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IvalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constant(self):
            return self.getTypedRuleContext(AnolangParser.ConstantContext,0)


        def identity(self):
            return self.getTypedRuleContext(AnolangParser.IdentityContext,0)


        def getRuleIndex(self):
            return AnolangParser.RULE_ival

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIval" ):
                listener.enterIval(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIval" ):
                listener.exitIval(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIval" ):
                return visitor.visitIval(self)
            else:
                return visitor.visitChildren(self)




    def ival(self):

        localctx = AnolangParser.IvalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_ival)
        try:
            self.state = 104
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40, 41, 42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.constant()
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                self.identity()
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


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def externsmt(self):
            return self.getTypedRuleContext(AnolangParser.ExternsmtContext,0)


        def autosmt(self):
            return self.getTypedRuleContext(AnolangParser.AutosmtContext,0)


        def identity(self):
            return self.getTypedRuleContext(AnolangParser.IdentityContext,0)


        def statement(self):
            return self.getTypedRuleContext(AnolangParser.StatementContext,0)


        def casestmt(self):
            return self.getTypedRuleContext(AnolangParser.CasestmtContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(AnolangParser.BlockstmtContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(AnolangParser.IfstmtContext,0)


        def whilestmt(self):
            return self.getTypedRuleContext(AnolangParser.WhilestmtContext,0)


        def switchstmt(self):
            return self.getTypedRuleContext(AnolangParser.SwitchstmtContext,0)


        def gotostmt(self):
            return self.getTypedRuleContext(AnolangParser.GotostmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(AnolangParser.ReturnstmtContext,0)


        def expressionstmt(self):
            return self.getTypedRuleContext(AnolangParser.ExpressionstmtContext,0)


        def nullstmt(self):
            return self.getTypedRuleContext(AnolangParser.NullstmtContext,0)


        def getRuleIndex(self):
            return AnolangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = AnolangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 106
                self.externsmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 107
                self.autosmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 108
                self.identity()
                self.state = 109
                self.match(AnolangParser.T__4)
                self.state = 110
                self.statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 112
                self.casestmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 113
                self.blockstmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 114
                self.ifstmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 115
                self.whilestmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 116
                self.switchstmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 117
                self.gotostmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 118
                self.returnstmt()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 119
                self.expressionstmt()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 120
                self.nullstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NullstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AnolangParser.RULE_nullstmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNullstmt" ):
                listener.enterNullstmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNullstmt" ):
                listener.exitNullstmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullstmt" ):
                return visitor.visitNullstmt(self)
            else:
                return visitor.visitChildren(self)




    def nullstmt(self):

        localctx = AnolangParser.NullstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_nullstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(AnolangParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rvalue(self):
            return self.getTypedRuleContext(AnolangParser.RvalueContext,0)


        def getRuleIndex(self):
            return AnolangParser.RULE_expressionstmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionstmt" ):
                listener.enterExpressionstmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionstmt" ):
                listener.exitExpressionstmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionstmt" ):
                return visitor.visitExpressionstmt(self)
            else:
                return visitor.visitChildren(self)




    def expressionstmt(self):

        localctx = AnolangParser.ExpressionstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expressionstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.rvalue()
            self.state = 126
            self.match(AnolangParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AnolangParser.StatementContext)
            else:
                return self.getTypedRuleContext(AnolangParser.StatementContext,i)


        def getRuleIndex(self):
            return AnolangParser.RULE_blockstmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockstmt" ):
                listener.enterBlockstmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockstmt" ):
                listener.exitBlockstmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstmt" ):
                return visitor.visitBlockstmt(self)
            else:
                return visitor.visitChildren(self)




    def blockstmt(self):

        localctx = AnolangParser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_blockstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(AnolangParser.T__5)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8246353321804) != 0):
                self.state = 129
                self.statement()
                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 135
            self.match(AnolangParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rvalue(self):
            return self.getTypedRuleContext(AnolangParser.RvalueContext,0)


        def getRuleIndex(self):
            return AnolangParser.RULE_returnstmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnstmt" ):
                listener.enterReturnstmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnstmt" ):
                listener.exitReturnstmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstmt" ):
                return visitor.visitReturnstmt(self)
            else:
                return visitor.visitChildren(self)




    def returnstmt(self):

        localctx = AnolangParser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_returnstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(AnolangParser.T__7)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 138
                self.match(AnolangParser.T__2)
                self.state = 139
                self.rvalue()
                self.state = 140
                self.match(AnolangParser.T__3)


            self.state = 144
            self.match(AnolangParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GotostmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rvalue(self):
            return self.getTypedRuleContext(AnolangParser.RvalueContext,0)


        def getRuleIndex(self):
            return AnolangParser.RULE_gotostmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGotostmt" ):
                listener.enterGotostmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGotostmt" ):
                listener.exitGotostmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGotostmt" ):
                return visitor.visitGotostmt(self)
            else:
                return visitor.visitChildren(self)




    def gotostmt(self):

        localctx = AnolangParser.GotostmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_gotostmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(AnolangParser.T__8)
            self.state = 147
            self.rvalue()
            self.state = 148
            self.match(AnolangParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rvalue(self):
            return self.getTypedRuleContext(AnolangParser.RvalueContext,0)


        def statement(self):
            return self.getTypedRuleContext(AnolangParser.StatementContext,0)


        def getRuleIndex(self):
            return AnolangParser.RULE_switchstmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchstmt" ):
                listener.enterSwitchstmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchstmt" ):
                listener.exitSwitchstmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitchstmt" ):
                return visitor.visitSwitchstmt(self)
            else:
                return visitor.visitChildren(self)




    def switchstmt(self):

        localctx = AnolangParser.SwitchstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_switchstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(AnolangParser.T__9)
            self.state = 151
            self.rvalue()
            self.state = 152
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhilestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rvalue(self):
            return self.getTypedRuleContext(AnolangParser.RvalueContext,0)


        def statement(self):
            return self.getTypedRuleContext(AnolangParser.StatementContext,0)


        def getRuleIndex(self):
            return AnolangParser.RULE_whilestmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhilestmt" ):
                listener.enterWhilestmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhilestmt" ):
                listener.exitWhilestmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhilestmt" ):
                return visitor.visitWhilestmt(self)
            else:
                return visitor.visitChildren(self)




    def whilestmt(self):

        localctx = AnolangParser.WhilestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_whilestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(AnolangParser.T__10)
            self.state = 155
            self.match(AnolangParser.T__2)
            self.state = 156
            self.rvalue()
            self.state = 157
            self.match(AnolangParser.T__3)
            self.state = 158
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rvalue(self):
            return self.getTypedRuleContext(AnolangParser.RvalueContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AnolangParser.StatementContext)
            else:
                return self.getTypedRuleContext(AnolangParser.StatementContext,i)


        def getRuleIndex(self):
            return AnolangParser.RULE_ifstmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfstmt" ):
                listener.enterIfstmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfstmt" ):
                listener.exitIfstmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = AnolangParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_ifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(AnolangParser.T__11)
            self.state = 161
            self.match(AnolangParser.T__2)
            self.state = 162
            self.rvalue()
            self.state = 163
            self.match(AnolangParser.T__3)
            self.state = 164
            self.statement()
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 165
                self.match(AnolangParser.T__12)
                self.state = 166
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CasestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constant(self):
            return self.getTypedRuleContext(AnolangParser.ConstantContext,0)


        def statement(self):
            return self.getTypedRuleContext(AnolangParser.StatementContext,0)


        def getRuleIndex(self):
            return AnolangParser.RULE_casestmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCasestmt" ):
                listener.enterCasestmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCasestmt" ):
                listener.exitCasestmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCasestmt" ):
                return visitor.visitCasestmt(self)
            else:
                return visitor.visitChildren(self)




    def casestmt(self):

        localctx = AnolangParser.CasestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_casestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(AnolangParser.T__13)
            self.state = 170
            self.constant()
            self.state = 171
            self.match(AnolangParser.T__4)
            self.state = 172
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExternsmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identity(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AnolangParser.IdentityContext)
            else:
                return self.getTypedRuleContext(AnolangParser.IdentityContext,i)


        def getRuleIndex(self):
            return AnolangParser.RULE_externsmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExternsmt" ):
                listener.enterExternsmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExternsmt" ):
                listener.exitExternsmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExternsmt" ):
                return visitor.visitExternsmt(self)
            else:
                return visitor.visitChildren(self)




    def externsmt(self):

        localctx = AnolangParser.ExternsmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_externsmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(AnolangParser.T__14)
            self.state = 175
            self.identity()
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 176
                self.match(AnolangParser.T__0)
                self.state = 177
                self.identity()
                self.state = 182
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 183
            self.match(AnolangParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AutosmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identity(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AnolangParser.IdentityContext)
            else:
                return self.getTypedRuleContext(AnolangParser.IdentityContext,i)


        def constant(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AnolangParser.ConstantContext)
            else:
                return self.getTypedRuleContext(AnolangParser.ConstantContext,i)


        def getRuleIndex(self):
            return AnolangParser.RULE_autosmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAutosmt" ):
                listener.enterAutosmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAutosmt" ):
                listener.exitAutosmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAutosmt" ):
                return visitor.visitAutosmt(self)
            else:
                return visitor.visitChildren(self)




    def autosmt(self):

        localctx = AnolangParser.AutosmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_autosmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(AnolangParser.T__15)
            self.state = 186
            self.identity()
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 7696581394432) != 0):
                self.state = 187
                self.constant()


            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 190
                self.match(AnolangParser.T__0)
                self.state = 191
                self.identity()
                self.state = 193
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 7696581394432) != 0):
                    self.state = 192
                    self.constant()


                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 200
            self.match(AnolangParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(AnolangParser.ExpressionContext,0)


        def comparison(self):
            return self.getTypedRuleContext(AnolangParser.ComparisonContext,0)


        def ternary(self):
            return self.getTypedRuleContext(AnolangParser.TernaryContext,0)


        def assignment(self):
            return self.getTypedRuleContext(AnolangParser.AssignmentContext,0)


        def getRuleIndex(self):
            return AnolangParser.RULE_rvalue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRvalue" ):
                listener.enterRvalue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRvalue" ):
                listener.exitRvalue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRvalue" ):
                return visitor.visitRvalue(self)
            else:
                return visitor.visitChildren(self)




    def rvalue(self):

        localctx = AnolangParser.RvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_rvalue)
        try:
            self.state = 206
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.comparison()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 204
                self.ternary()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 205
                self.assignment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TernaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(AnolangParser.ExpressionContext,0)


        def rvalue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AnolangParser.RvalueContext)
            else:
                return self.getTypedRuleContext(AnolangParser.RvalueContext,i)


        def getRuleIndex(self):
            return AnolangParser.RULE_ternary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTernary" ):
                listener.enterTernary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTernary" ):
                listener.exitTernary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTernary" ):
                return visitor.visitTernary(self)
            else:
                return visitor.visitChildren(self)




    def ternary(self):

        localctx = AnolangParser.TernaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_ternary)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.expression()
            self.state = 209
            self.match(AnolangParser.T__16)
            self.state = 210
            self.rvalue()
            self.state = 211
            self.match(AnolangParser.T__4)
            self.state = 212
            self.rvalue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(AnolangParser.ExpressionContext,0)


        def binary(self):
            return self.getTypedRuleContext(AnolangParser.BinaryContext,0)


        def rvalue(self):
            return self.getTypedRuleContext(AnolangParser.RvalueContext,0)


        def getRuleIndex(self):
            return AnolangParser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)




    def comparison(self):

        localctx = AnolangParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_comparison)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.expression()
            self.state = 215
            self.binary()
            self.state = 216
            self.rvalue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identity(self):
            return self.getTypedRuleContext(AnolangParser.IdentityContext,0)


        def assign(self):
            return self.getTypedRuleContext(AnolangParser.AssignContext,0)


        def rvalue(self):
            return self.getTypedRuleContext(AnolangParser.RvalueContext,0)


        def getRuleIndex(self):
            return AnolangParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = AnolangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.identity()
            self.state = 219
            self.assign()
            self.state = 220
            self.rvalue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rvalue(self):
            return self.getTypedRuleContext(AnolangParser.RvalueContext,0)


        def identity(self):
            return self.getTypedRuleContext(AnolangParser.IdentityContext,0)


        def constant(self):
            return self.getTypedRuleContext(AnolangParser.ConstantContext,0)


        def incdec(self):
            return self.getTypedRuleContext(AnolangParser.IncdecContext,0)


        def unary(self):
            return self.getTypedRuleContext(AnolangParser.UnaryContext,0)


        def functioninvocation(self):
            return self.getTypedRuleContext(AnolangParser.FunctioninvocationContext,0)


        def getRuleIndex(self):
            return AnolangParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = AnolangParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expression)
        try:
            self.state = 240
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                self.match(AnolangParser.T__2)
                self.state = 223
                self.rvalue()
                self.state = 224
                self.match(AnolangParser.T__3)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.identity()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 227
                self.constant()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 228
                self.incdec()
                self.state = 229
                self.identity()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 231
                self.identity()
                self.state = 232
                self.incdec()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 234
                self.unary()
                self.state = 235
                self.rvalue()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 237
                self.match(AnolangParser.T__17)
                self.state = 238
                self.identity()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 239
                self.functioninvocation()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctioninvocationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identity(self):
            return self.getTypedRuleContext(AnolangParser.IdentityContext,0)


        def functionparameters(self):
            return self.getTypedRuleContext(AnolangParser.FunctionparametersContext,0)


        def getRuleIndex(self):
            return AnolangParser.RULE_functioninvocation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctioninvocation" ):
                listener.enterFunctioninvocation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctioninvocation" ):
                listener.exitFunctioninvocation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctioninvocation" ):
                return visitor.visitFunctioninvocation(self)
            else:
                return visitor.visitChildren(self)




    def functioninvocation(self):

        localctx = AnolangParser.FunctioninvocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_functioninvocation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.identity()
            self.state = 243
            self.match(AnolangParser.T__2)
            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8246353199112) != 0):
                self.state = 244
                self.functionparameters()


            self.state = 247
            self.match(AnolangParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionparametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rvalue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AnolangParser.RvalueContext)
            else:
                return self.getTypedRuleContext(AnolangParser.RvalueContext,i)


        def getRuleIndex(self):
            return AnolangParser.RULE_functionparameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionparameters" ):
                listener.enterFunctionparameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionparameters" ):
                listener.exitFunctionparameters(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionparameters" ):
                return visitor.visitFunctionparameters(self)
            else:
                return visitor.visitChildren(self)




    def functionparameters(self):

        localctx = AnolangParser.FunctionparametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_functionparameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.rvalue()
            self.state = 254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 250
                self.match(AnolangParser.T__0)
                self.state = 251
                self.rvalue()
                self.state = 256
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def binary(self):
            return self.getTypedRuleContext(AnolangParser.BinaryContext,0)


        def getRuleIndex(self):
            return AnolangParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = AnolangParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(AnolangParser.T__18)
            self.state = 259
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 258
                self.binary()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IncdecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AnolangParser.RULE_incdec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncdec" ):
                listener.enterIncdec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncdec" ):
                listener.exitIncdec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIncdec" ):
                return visitor.visitIncdec(self)
            else:
                return visitor.visitChildren(self)




    def incdec(self):

        localctx = AnolangParser.IncdecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_incdec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            _la = self._input.LA(1)
            if not(_la==20 or _la==21):
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


    class UnaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AnolangParser.RULE_unary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary" ):
                listener.enterUnary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary" ):
                listener.exitUnary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary" ):
                return visitor.visitUnary(self)
            else:
                return visitor.visitChildren(self)




    def unary(self):

        localctx = AnolangParser.UnaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_unary)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            _la = self._input.LA(1)
            if not(_la==22 or _la==23):
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


    class BinaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AnolangParser.RULE_binary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinary" ):
                listener.enterBinary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinary" ):
                listener.exitBinary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinary" ):
                return visitor.visitBinary(self)
            else:
                return visitor.visitChildren(self)




    def binary(self):

        localctx = AnolangParser.BinaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_binary)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 137426632704) != 0)):
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


    class LvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identity(self):
            return self.getTypedRuleContext(AnolangParser.IdentityContext,0)


        def rvalue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AnolangParser.RvalueContext)
            else:
                return self.getTypedRuleContext(AnolangParser.RvalueContext,i)


        def getRuleIndex(self):
            return AnolangParser.RULE_lvalue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLvalue" ):
                listener.enterLvalue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLvalue" ):
                listener.exitLvalue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLvalue" ):
                return visitor.visitLvalue(self)
            else:
                return visitor.visitChildren(self)




    def lvalue(self):

        localctx = AnolangParser.LvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_lvalue)
        try:
            self.state = 275
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.identity()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
                self.match(AnolangParser.T__34)
                self.state = 269
                self.rvalue()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 270
                self.rvalue()
                self.state = 271
                self.match(AnolangParser.T__36)
                self.state = 272
                self.rvalue()
                self.state = 273
                self.match(AnolangParser.T__37)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(AnolangParser.INT, 0)

        def STRING1(self):
            return self.getToken(AnolangParser.STRING1, 0)

        def STRING2(self):
            return self.getToken(AnolangParser.STRING2, 0)

        def getRuleIndex(self):
            return AnolangParser.RULE_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant" ):
                listener.enterConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant" ):
                listener.exitConstant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstant" ):
                return visitor.visitConstant(self)
            else:
                return visitor.visitChildren(self)




    def constant(self):

        localctx = AnolangParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7696581394432) != 0)):
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


    class IdentityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(AnolangParser.NAME, 0)

        def getRuleIndex(self):
            return AnolangParser.RULE_identity

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentity" ):
                listener.enterIdentity(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentity" ):
                listener.exitIdentity(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentity" ):
                return visitor.visitIdentity(self)
            else:
                return visitor.visitChildren(self)




    def identity(self):

        localctx = AnolangParser.IdentityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_identity)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(AnolangParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





