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

([a-zA-Z]|_)[\w_]*


valid variables
* a, Z
* _A_1
* x_force
* a1
* c12
* x_long_var

invalid
* 1a
* a100 (max two numbers can be appended to the first letter)
* ab (considered as two variables)
