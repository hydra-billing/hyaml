grammar Hyaml;

prog: expr;
expr:
	parens
	| expr callChain
	| expr subscription
	| expr MULT_DIV_OP expr
	| expr SIGN expr
	| expr COMP_OP expr
	| NOT expr
	| expr AND expr
	| expr OR expr
	| listLiteral
	| dictLiteral
	| VAR
	| SIGN? NUMBER
	| STRING
	| TRUE
	| FALSE;

callChain: attributeOrDispatch+;

NEWLINE: [\r\n]+;
TRUE: 'true';
FALSE: 'false';
AND: 'and';
OR: 'or';
NOT: 'not';
SIGN: [-+];
NUMBER: DIGIT+ ('.' DIGIT+)?;
MULT_DIV_OP: [/*%];
COMP_OP: '>=' | '<=' | '<' | '>' | '==' | '!=';
VAR: '$' LETTER (LETTER | DIGIT)*;
ID_SYMBOL: [-:_];
ID: LETTER ((LETTER | DIGIT | ID_SYMBOL)* (LETTER | DIGIT))?;
LETTER: [a-zA-Z];
DIGIT: [0-9];
STRING: ('\'' ~'\''* '\'') | ('"' ~'"'* '"');
WS: [ \t\r]+ -> skip;
SAFE_ACCESS: '?.';
ACCESS: '.';
PRED: '?';

attributeOrDispatch: (SAFE_ACCESS | ACCESS) ID (PRED? args)?;

exprList: expr (',' expr)*;

args: '(' exprList? ')';

subscription: '[' expr ']';

listLiteral: '[' exprList? ']';

keyValuePair: ID ':' expr;

keyValuePairs: keyValuePair (',' keyValuePair)*;

dictLiteral: '{' keyValuePairs? '}';

parens: '(' expr ')';

