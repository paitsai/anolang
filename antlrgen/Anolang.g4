// 基於貝爾實驗室B語言改進而來的Anolang


grammar Anolang;

ano_program
    : definition* EOF
    ;


//一個Anolng的代碼至少需要有一個函數體或者變量的定義

definition
    : identity constant? (ival (',' ival)*)* ';'
    | identity '(' (identity (',' identity)*)? ')' statement
    ;

ival
    : constant
    | identity
    ;

statement
    : externsmt
    | autosmt
    | identity ':' statement
    | casestmt
    | blockstmt
    | ifstmt
    | whilestmt
    | switchstmt
    | gotostmt
    | returnstmt
    | expressionstmt
    | nullstmt
    ;

nullstmt
    : ';'
    ;

expressionstmt
    : rvalue ';'
    ;

blockstmt
    : '{' statement* '}'
    ;

returnstmt
    : 'return' ('(' rvalue ')')? ';'
    ;

gotostmt
    : 'goto' rvalue ';'
    ;

switchstmt
    : 'switch' rvalue statement
    ;

whilestmt
    : 'while' '(' rvalue ')' statement
    ;

ifstmt
    : 'if' '(' rvalue ')' statement ('else' statement)?
    ;

casestmt
    : 'case' constant ':' statement
    ;

externsmt
    : 'extrn' identity (',' identity)* ';'
    ;

autosmt
    : 'auto' identity constant? (',' identity constant?)* ';'
    ;

rvalue
    : expression
    | comparison
    | ternary
    | assignment
    ;

ternary
    : expression '?' rvalue ':' rvalue
    ;

comparison
    : expression binary rvalue
    ;

assignment
    : identity assign rvalue
    ;

expression
    : '(' rvalue ')'
    | identity
    | constant
    | incdec identity
    | identity incdec
    | unary rvalue
    | '&' identity
    | functioninvocation
    ;

functioninvocation
    : identity '(' functionparameters? ')'
    ;

functionparameters
    : rvalue (',' rvalue)*
    ;

assign
    : '=' binary?
    ;

incdec
    : '++'
    | '--'
    ;

unary
    : '-'
    | '!'
    ;

binary
    : '|'
    | '&'
    | '=='
    | '!='
    | '<'
    | '<='
    | '>'
    | '>='
    | '<<'
    | '>>'
    | '-'
    | '+'
    | '%'
    | '*'
    | '/'
    ;

lvalue
    : identity
    | '*' rvalue
    | rvalue '[' rvalue ']'
    ;

constant
    : INT
    | STRING1
    | STRING2
    ;

identity
    : NAME
    ;

NAME
    : [a-zA-Z] [a-zA-Z0-9_]*
    ;

INT
    : [0-9]+
    ;

STRING1
    : '"' ~ ["\r\n]* '"'
    ;

STRING2
    : '\'' ~ ['\r\n]* '\''
    ;

BLOCKCOMMENT
    : '/*' .*? '*/' -> skip
    ;

WS
    : [ \t\r\n] -> skip
    ;