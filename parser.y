%{
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int yylex(void);
int yyerror(const char *s);
%}

%union {
    double val;
}

%token <val> NUM
%token SQRT LPAREN RPAREN EOL
%type <val> expr

%%

input:
    /* vacío */
  | input line
  ;

line:
    expr EOL   { printf("= %f\n", $1); }
  | EOL
  ;

expr:
    NUM
      { $$ = $1; }
  | SQRT LPAREN expr RPAREN
      { $$ = sqrt($3); }
  ;

%%

int main(void) {
    return yyparse();
}

int yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
    return 0;
}
