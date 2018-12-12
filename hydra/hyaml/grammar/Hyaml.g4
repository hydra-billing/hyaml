grammar Hyaml;

prog: expr;
expr:
	expr MULT_DIV_OP expr
	| expr ADD_SUB_OP expr
	| expr COMP_OP expr
	| NOT expr
	| expr AND expr
	| expr OR expr
	| expr callChain
	| expr subscription
	| parens
	| listLiteral
	| VAR
	| EMPTY_HASH
	| NUMBER
	| STRING
	| TRUE
	| FALSE;

link: methodCall | attribute;

callChain: link+;

NEWLINE: [\r\n]+;
TRUE: 'true';
FALSE: 'false';
AND: 'and';
OR: 'or';
NOT: 'not';
NUMBER:
	{self._input.LT(1) != self.NUMBER} [-+]? DIGIT+ ('.' DIGIT+)?;
MULT_DIV_OP: [/*];
ADD_SUB_OP: [-+];
COMP_OP: '>=' | '<=' | '<' | '>' | '==';
VAR: '$' LETTER (LETTER | DIGIT)*;
ID: LETTER (LETTER | DIGIT | '-' | ':' | '_')*;
LETTER: [a-zA-Z];
DIGIT: [0-9];
EMPTY_HASH: '{}';
PRED: '?';
STRING: ('\'' ~'\''+ '\'') | ('"' ~'"'+ '"');
WS: [ \t\r]+ -> skip;

methodCall: '.' ID PRED? arguments;

attribute: '.' ID;

exprList: expr (',' expr)*;

arguments: '(' exprList? ')';

subscription: '[' expr ']';

listLiteral: '[' exprList? ']';

parens: '(' expr ')';

