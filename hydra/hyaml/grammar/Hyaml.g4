grammar Hyaml;

prog: expr;
expr:
	expr MULT_DIV_OP expr
	| expr SIGN expr
	| expr COMP_OP expr
	| NOT expr
	| expr AND expr
	| expr OR expr
	| expr callChain
	| expr subscription
	| parens
	| listLiteral
	| dictLiteral
	| VAR
	| SIGN? NUMBER
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
SIGN: [-+];
NUMBER: DIGIT+ ('.' DIGIT+)?;
MULT_DIV_OP: [/*%];
COMP_OP: '>=' | '<=' | '<' | '>' | '==';
VAR: '$' LETTER (LETTER | DIGIT)*;
ID_SYMBOL: [-:_];
ID: LETTER ((LETTER | DIGIT | ID_SYMBOL)* (LETTER | DIGIT))?;
LETTER: [a-zA-Z];
DIGIT: [0-9];
PRED: '?';
STRING: ('\'' ~'\''+ '\'') | ('"' ~'"'+ '"');
WS: [ \t\r]+ -> skip;

methodCall: '.' ID PRED? arguments;

attribute: '.' ID;

exprList: expr (',' expr)*;

arguments: '(' exprList? ')';

subscription: '[' expr ']';

listLiteral: '[' exprList? ']';

keyValuePair: ID ':' expr;

keyValuePairs: keyValuePair (',' keyValuePair)*;

dictLiteral: '{' keyValuePairs? '}';

parens: '(' expr ')';

