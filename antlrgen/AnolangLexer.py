# Generated from ./antlrgen/Anolang.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,44,252,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,1,0,1,0,1,1,1,1,
        1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,
        10,1,10,1,10,1,10,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,13,1,
        13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,
        15,1,15,1,16,1,16,1,17,1,17,1,18,1,18,1,19,1,19,1,19,1,20,1,20,1,
        20,1,21,1,21,1,22,1,22,1,23,1,23,1,24,1,24,1,24,1,25,1,25,1,25,1,
        26,1,26,1,27,1,27,1,27,1,28,1,28,1,29,1,29,1,29,1,30,1,30,1,30,1,
        31,1,31,1,31,1,32,1,32,1,33,1,33,1,34,1,34,1,35,1,35,1,36,1,36,1,
        37,1,37,1,38,1,38,5,38,207,8,38,10,38,12,38,210,9,38,1,39,4,39,213,
        8,39,11,39,12,39,214,1,40,1,40,5,40,219,8,40,10,40,12,40,222,9,40,
        1,40,1,40,1,41,1,41,5,41,228,8,41,10,41,12,41,231,9,41,1,41,1,41,
        1,42,1,42,1,42,1,42,5,42,239,8,42,10,42,12,42,242,9,42,1,42,1,42,
        1,42,1,42,1,42,1,43,1,43,1,43,1,43,1,240,0,44,1,1,3,2,5,3,7,4,9,
        5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,
        33,17,35,18,37,19,39,20,41,21,43,22,45,23,47,24,49,25,51,26,53,27,
        55,28,57,29,59,30,61,31,63,32,65,33,67,34,69,35,71,36,73,37,75,38,
        77,39,79,40,81,41,83,42,85,43,87,44,1,0,6,2,0,65,90,97,122,4,0,48,
        57,65,90,95,95,97,122,1,0,48,57,3,0,10,10,13,13,34,34,3,0,10,10,
        13,13,39,39,3,0,9,10,13,13,32,32,256,0,1,1,0,0,0,0,3,1,0,0,0,0,5,
        1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,
        0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,
        0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,
        0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,
        0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,
        0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,
        0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,
        0,0,0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,0,0,85,1,
        0,0,0,0,87,1,0,0,0,1,89,1,0,0,0,3,91,1,0,0,0,5,93,1,0,0,0,7,95,1,
        0,0,0,9,97,1,0,0,0,11,99,1,0,0,0,13,101,1,0,0,0,15,103,1,0,0,0,17,
        110,1,0,0,0,19,115,1,0,0,0,21,122,1,0,0,0,23,128,1,0,0,0,25,131,
        1,0,0,0,27,136,1,0,0,0,29,141,1,0,0,0,31,147,1,0,0,0,33,152,1,0,
        0,0,35,154,1,0,0,0,37,156,1,0,0,0,39,158,1,0,0,0,41,161,1,0,0,0,
        43,164,1,0,0,0,45,166,1,0,0,0,47,168,1,0,0,0,49,170,1,0,0,0,51,173,
        1,0,0,0,53,176,1,0,0,0,55,178,1,0,0,0,57,181,1,0,0,0,59,183,1,0,
        0,0,61,186,1,0,0,0,63,189,1,0,0,0,65,192,1,0,0,0,67,194,1,0,0,0,
        69,196,1,0,0,0,71,198,1,0,0,0,73,200,1,0,0,0,75,202,1,0,0,0,77,204,
        1,0,0,0,79,212,1,0,0,0,81,216,1,0,0,0,83,225,1,0,0,0,85,234,1,0,
        0,0,87,248,1,0,0,0,89,90,5,44,0,0,90,2,1,0,0,0,91,92,5,59,0,0,92,
        4,1,0,0,0,93,94,5,40,0,0,94,6,1,0,0,0,95,96,5,41,0,0,96,8,1,0,0,
        0,97,98,5,58,0,0,98,10,1,0,0,0,99,100,5,123,0,0,100,12,1,0,0,0,101,
        102,5,125,0,0,102,14,1,0,0,0,103,104,5,114,0,0,104,105,5,101,0,0,
        105,106,5,116,0,0,106,107,5,117,0,0,107,108,5,114,0,0,108,109,5,
        110,0,0,109,16,1,0,0,0,110,111,5,103,0,0,111,112,5,111,0,0,112,113,
        5,116,0,0,113,114,5,111,0,0,114,18,1,0,0,0,115,116,5,115,0,0,116,
        117,5,119,0,0,117,118,5,105,0,0,118,119,5,116,0,0,119,120,5,99,0,
        0,120,121,5,104,0,0,121,20,1,0,0,0,122,123,5,119,0,0,123,124,5,104,
        0,0,124,125,5,105,0,0,125,126,5,108,0,0,126,127,5,101,0,0,127,22,
        1,0,0,0,128,129,5,105,0,0,129,130,5,102,0,0,130,24,1,0,0,0,131,132,
        5,101,0,0,132,133,5,108,0,0,133,134,5,115,0,0,134,135,5,101,0,0,
        135,26,1,0,0,0,136,137,5,99,0,0,137,138,5,97,0,0,138,139,5,115,0,
        0,139,140,5,101,0,0,140,28,1,0,0,0,141,142,5,101,0,0,142,143,5,120,
        0,0,143,144,5,116,0,0,144,145,5,114,0,0,145,146,5,110,0,0,146,30,
        1,0,0,0,147,148,5,97,0,0,148,149,5,117,0,0,149,150,5,116,0,0,150,
        151,5,111,0,0,151,32,1,0,0,0,152,153,5,63,0,0,153,34,1,0,0,0,154,
        155,5,38,0,0,155,36,1,0,0,0,156,157,5,61,0,0,157,38,1,0,0,0,158,
        159,5,43,0,0,159,160,5,43,0,0,160,40,1,0,0,0,161,162,5,45,0,0,162,
        163,5,45,0,0,163,42,1,0,0,0,164,165,5,45,0,0,165,44,1,0,0,0,166,
        167,5,33,0,0,167,46,1,0,0,0,168,169,5,124,0,0,169,48,1,0,0,0,170,
        171,5,61,0,0,171,172,5,61,0,0,172,50,1,0,0,0,173,174,5,33,0,0,174,
        175,5,61,0,0,175,52,1,0,0,0,176,177,5,60,0,0,177,54,1,0,0,0,178,
        179,5,60,0,0,179,180,5,61,0,0,180,56,1,0,0,0,181,182,5,62,0,0,182,
        58,1,0,0,0,183,184,5,62,0,0,184,185,5,61,0,0,185,60,1,0,0,0,186,
        187,5,60,0,0,187,188,5,60,0,0,188,62,1,0,0,0,189,190,5,62,0,0,190,
        191,5,62,0,0,191,64,1,0,0,0,192,193,5,43,0,0,193,66,1,0,0,0,194,
        195,5,37,0,0,195,68,1,0,0,0,196,197,5,42,0,0,197,70,1,0,0,0,198,
        199,5,47,0,0,199,72,1,0,0,0,200,201,5,91,0,0,201,74,1,0,0,0,202,
        203,5,93,0,0,203,76,1,0,0,0,204,208,7,0,0,0,205,207,7,1,0,0,206,
        205,1,0,0,0,207,210,1,0,0,0,208,206,1,0,0,0,208,209,1,0,0,0,209,
        78,1,0,0,0,210,208,1,0,0,0,211,213,7,2,0,0,212,211,1,0,0,0,213,214,
        1,0,0,0,214,212,1,0,0,0,214,215,1,0,0,0,215,80,1,0,0,0,216,220,5,
        34,0,0,217,219,8,3,0,0,218,217,1,0,0,0,219,222,1,0,0,0,220,218,1,
        0,0,0,220,221,1,0,0,0,221,223,1,0,0,0,222,220,1,0,0,0,223,224,5,
        34,0,0,224,82,1,0,0,0,225,229,5,39,0,0,226,228,8,4,0,0,227,226,1,
        0,0,0,228,231,1,0,0,0,229,227,1,0,0,0,229,230,1,0,0,0,230,232,1,
        0,0,0,231,229,1,0,0,0,232,233,5,39,0,0,233,84,1,0,0,0,234,235,5,
        47,0,0,235,236,5,42,0,0,236,240,1,0,0,0,237,239,9,0,0,0,238,237,
        1,0,0,0,239,242,1,0,0,0,240,241,1,0,0,0,240,238,1,0,0,0,241,243,
        1,0,0,0,242,240,1,0,0,0,243,244,5,42,0,0,244,245,5,47,0,0,245,246,
        1,0,0,0,246,247,6,42,0,0,247,86,1,0,0,0,248,249,7,5,0,0,249,250,
        1,0,0,0,250,251,6,43,0,0,251,88,1,0,0,0,6,0,208,214,220,229,240,
        1,6,0,0
    ]

class AnolangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    T__28 = 29
    T__29 = 30
    T__30 = 31
    T__31 = 32
    T__32 = 33
    T__33 = 34
    T__34 = 35
    T__35 = 36
    T__36 = 37
    T__37 = 38
    NAME = 39
    INT = 40
    STRING1 = 41
    STRING2 = 42
    BLOCKCOMMENT = 43
    WS = 44

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "';'", "'('", "')'", "':'", "'{'", "'}'", "'return'", 
            "'goto'", "'switch'", "'while'", "'if'", "'else'", "'case'", 
            "'extrn'", "'auto'", "'?'", "'&'", "'='", "'++'", "'--'", "'-'", 
            "'!'", "'|'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", 
            "'<<'", "'>>'", "'+'", "'%'", "'*'", "'/'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>",
            "NAME", "INT", "STRING1", "STRING2", "BLOCKCOMMENT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "T__28", "T__29", "T__30", "T__31", 
                  "T__32", "T__33", "T__34", "T__35", "T__36", "T__37", 
                  "NAME", "INT", "STRING1", "STRING2", "BLOCKCOMMENT", "WS" ]

    grammarFileName = "Anolang.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


