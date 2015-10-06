**commands**

[ ] optional argument, ( ) mandatory argument
* To issue a command, prepend the line with an @
* print [line number]
* printall
* remove [line number,  range]
* replace ([line number, range], (line number, range)) 
* insert ([line number, range], (line number, range))
* numeric
* fractional
* exit

**variables**

Identifier regex = ( letter | underscore ), {letter | underscore | digit}

[a-zA-Z_][a-zA-Z0-9_]*


valid variables
* a, Z
* sinco
* _A_1
* x_force
* a1
* c12
* x_long_var
