grammar pyToJava;

// Lexer rules
DEF : 'def' ;
RETURN : 'return' ;
PRINT : 'print' ;
MUL : '*' ;
SUB : '-' ;
LPAREN : '(' ;
RPAREN : ')' ;
COLON : ':' ;
COMMA : ',' ;
ID : [a-zA-Z_][a-zA-Z_0-9]* ;
INT : [0-9]+ ;
WS : [ \t\r\n]+ -> skip ; 

// Parser rules
program : functionDefinition statement EOF ;

functionDefinition : DEF ID LPAREN parameters? RPAREN COLON block ;

parameters : parameter (COMMA parameter)* ;
parameter : ID ;

block : statement+ ;

statement : assignment
          | returnStatement
          | printStatement
          ;

assignment : ID '=' expression ;

returnStatement : RETURN expression ;

printStatement : PRINT LPAREN expression RPAREN ;

expression : expression MUL expression # MulExpression
           | expression SUB expression # SubExpression
           | ID                         # IdExpression
           | INT                        # IntExpression
           ;

