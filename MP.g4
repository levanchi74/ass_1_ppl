/* Name:Vũ Văn Huynh
   MSSV:1511328
*/
grammar MP;

@lexer::header {
from lexererr import *
}

options{
  language=Python3;
}

/*****************************************************PARSER******************************************************************/
program: decl+ EOF; 

decl: vardel 
    | funcdel
    | procedel
    ; 
// ----------------------------------------------------variable declaration------------------
vardel: VAR var_decla+
      ;
var_decla: ID(CM ID)* COLON return_type SM
         ; 
return_type: primitive_type 
          | array_type
          ;
primitive_type: BOOLEANTYPE 
              | INTTYPE
              | REALTYPE 
              | STRINGTYPE
              ;
array_type: ARRAY LSB ('-'?INTLIT|expression) DD ('-'?INTLIT|expression) RSB OF primitive_type
          ;
//-----------------------------------------------------------function declaration-----------------
funcdel: FUNCTION ID LB para_lists? RB COLON return_type SM vardel? compound_statement
       ;
compound_statement: BEGIN statement* END
                  ;
para_lists:para_decla(SM para_decla)*
          ;
para_decla: ID(CM ID)* COLON return_type
          ;
//----------------------------------Satement
statement:  assignment_statement
          | if_statement
          | for_statement
          | while_statement
          | break_statement
          | continue_statement
          | return_statement
          | call_statement
          | compound_statement
          | with_statement
          ;
assignment_statement: ((index_exp|ID) ASSIGN)+ expression SM
                    ;
if_statement : IF  expression  THEN statement (ELSE statement)?
       ;
for_statement: FOR ID ASSIGN expression (TO|DOWNTO) expression DO statement
       ;
while_statement: WHILE expression DO statement
               ;  
break_statement: BREAK SM
         ;
continue_statement: CONTINUE SM
          ;
return_statement: RETURN expression? SM
                ;
call_statement: ID LB list_exp? RB SM
              ;  
list_exp: expression(CM expression)*;
                  
with_statement: WITH  var_decla+ DO statement 
              ;         
//-----------------------------------------Procedure declaration--------------------------------------------
procedel: PROCEDURE ID LB para_lists? RB SM vardel? compound_statement 
        ;
//-----------------------------------------Expression------------------------------------------------------
expression: expression (AND THEN|OR ELSE) expr1
          | expr1
          ;
expr1: expr2 (NOTEQUAL | EQUAL | LESSOREQUAL | LESS | GREATEROREQUAL | GREATER) expr2 
     | expr2
     ;
expr2: expr2 (ADD | SUB | OR) expr3
     | expr3
     ;
expr3: expr3 (MUL | DIVISION | DIV | MOD | AND) expr4
     | expr4
     ;
expr4: (SUB | NOT) expr4
     | expr5
     ;
expr5: LB expression RB| index_exp | funcall | literal | ID ;
//elem_array:ID LSB expression RSB;
funcall :  ID LB list_exp? RB ;
literal: INTLIT | FLOATLIT | STRINGLIT | BOOLEANLIT;
index_exp: (ID|funcall|INTLIT) LSB expression RSB;
/*****************************************************TOKEN**********************************************************************/
LINE_COMMENT: ('//'~[\n\r]*) -> skip ; 
TRA_BLOCK_COMMENT: '(*' .*? '*)'    -> skip; 
BLOCK_COMMENT:'{' .*? '}'    -> skip;
//----------------------Token Set------------------------------------
BOOLEANLIT: TRUE|FALSE;

BREAK:B R E A K ;
CONTINUE:C O N T I N U E;
FOR : F O R ;
TO: T O;
DOWNTO:D O W N T O;
DO: D O;
IF : I F;
THEN:T H E N;
ELSE : E L S E;
RETURN: R E T U R N;
WHILE: W H I L E;
WITH:W I T H;
BEGIN:B E G I N;
END:E N D;
FUNCTION:F U N C T I O N;
PROCEDURE:P R O C E D U R E;
VAR: V A R;
TRUE:T R U E;
FALSE:F A L S E; 
ARRAY:A R R A Y;
OF:O F; 
REALTYPE:R E A L;
BOOLEANTYPE:B O O L E A N;
INTTYPE: I N T E G E R;
STRINGTYPE: S T R I N G;
NOT:N O T;
AND:A N D;
OR:O R;
DIV:D I V;
MOD:M O D;
//----------------------------Case-insensive-----------
fragment A:('a'|'A');
fragment B:('b'|'B');
fragment C:('c'|'C');
fragment D:('d'|'D');
fragment E:('e'|'E');
fragment F:('f'|'F');
fragment G:('g'|'G');
fragment H:('h'|'H');
fragment I:('i'|'I');
fragment J:('j'|'J');
fragment K:('k'|'K');
fragment L:('l'|'L');
fragment M:('m'|'M');
fragment N:('n'|'N');
fragment O:('o'|'O');
fragment P:('p'|'P');
fragment Q:('q'|'Q');
fragment R:('r'|'R');
fragment S:('s'|'S');
fragment T:('t'|'T');
fragment U:('u'|'U');
fragment V:('v'|'V');
fragment W:('w'|'W');
fragment X:('x'|'X');
fragment Y:('y'|'Y');
fragment Z:('z'|'Z');
//----------Operator-----------------------------
ASSIGN :':=';
ADD:'+';
MUL:'*';
NOTEQUAL:'<>';
LESSOREQUAL:'<=';
GREATEROREQUAL:'>=';
SUB:'-';
DIVISION: '/';
EQUAL: '=';
LESS: '<';
GREATER: '>';
//------------separators-------------------------
LSB: '[' ;
RSB: ']' ;
COLON:':';
LB: '(';
RB: ')';
SM: ';' ;
DD:'..';
CM: ',';

INTLIT:[0-9]+;

fragment LETTER:[a-zA-Z];
fragment CASE1:([0-9]+[e|E]'-'?[0-9]+);
fragment CASE2:([0-9]*'.'[0-9]+[e|E]'-'?[0-9]+);
fragment CASE3:([0-9]*'.'[0-9]+);
fragment CASE4:([0-9]+'.'[0-9]*);
FLOATLIT:(CASE1|CASE2|CASE3|CASE4);
ID:('_'|LETTER)('_'|LETTER|[0-9])*;
WS : [ \t\r\n\f]+ -> skip ; // skip spaces, tabs, newlines
//-----------------------------------------------------------------------
//Unclose String
UNCLOSE_STRING: '"'(ESCAPE|~[\r\n"\\])*
{ 
  raise UncloseString(self.text[1:])
};

ERR: .*?'\\'('b'|'f'|'r'|'n'|'t'|'\''|'"'|'\\' ).*?
{
  raise ErrorToken('\\')
};

STRINGLIT: '"' (ESCAPE|~[\r\n"\\])* '"'
{ 
 temp=Lexer.text.fget(self)
 temp1=(temp[1:len(temp)-1])
 Lexer.text.fset(self,temp1)
}; 

ESCAPE: '\\'
        (   'b'    {Lexer.text.fset(self,"\b")}
        |   'f'    {Lexer.text.fset(self,"\f")}
        |   'r'    {Lexer.text.fset(self,"\r")}
        |   'n'    {Lexer.text.fset(self,"\n")}
        |   't'    {Lexer.text.fset(self,"\t")}
        |   '\''   {Lexer.text.fset(self,"\'")}
        |   '"'    {Lexer.text.fset(self,"\"")}
        |   '\\'   {Lexer.text.fset(self,"\\")}
        );


fragment ILL: ('\\')~('b'|'f'|'r'|'n'|'"'|'\''|'\\'|'t');
ILLEGAL_ESCAPE: '"' .*?  ILL .*? '"' 
{    
 temp=Lexer.text.fget(self) 
 temp1=temp.find('\\')
 raise IllegalEscape(self.text[1:temp1+2])
};
ERROR_CHAR:.
{
 raise ErrorToken(self.text)
};

