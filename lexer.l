%{
#include "parser.tab.h"
#include <stdlib.h>
%}

%%
[0-9]+(\.[0-9]+)?    { yylval.val = atof(yytext); return NUM; }
"sqrt"               { return SQRT; }
"("                  { return LPAREN; }
")"                  { return RPAREN; }
[ \t]+               { /* ignorar espacios */ }
\n                   { return EOL; }
.                    { /* ignorar otros */ }
%%

int yywrap(void) { return 1; }
