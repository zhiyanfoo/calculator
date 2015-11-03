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

Identifier regex : ( letter | underscore ) ( underscore ( letter | underscore | digit)+ | digit+ )?

[a-zA-Z_](_[a-zA-Z0-9_]+|[0-9]+)?


valid variables
* a, Z
* x_force
* a1
* c12
* x_long_var

**functions**

Function regex : ( letter | underscore ) ( letter | digit | underscore )*
[a-zA-Z_][a-zA-Z0-9]*


Internal representation : \{\$[a-zA-Z_][a-zA-Z0-9_]*\$\}
