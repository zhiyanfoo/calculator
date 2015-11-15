
# ../calculator/parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.5'

_lr_method = 'LALR'

_lr_signature = '458FCD9A3AD71885B1C1576571F10EB3'
    
_lr_action_items = {'IDENTIFIER':([0,3,4,8,15,17,21,22,23,24,25,27,29,],[1,16,16,16,16,16,16,16,16,16,16,16,16,]),'FUNCTION_1':([0,3,4,8,15,17,21,22,23,24,25,27,29,],[3,3,3,26,3,3,3,3,3,3,3,3,3,]),'LPAREN':([0,3,4,8,15,17,21,22,23,24,25,27,29,],[4,17,4,27,4,4,17,17,4,4,4,4,17,]),'FACTORIAL':([1,3,7,9,10,16,18,26,30,33,41,42,],[-25,-27,-26,-24,30,-25,-26,-27,-22,-23,-23,-23,]),'RPAREN':([3,5,9,10,11,12,13,16,18,19,20,26,28,30,32,33,34,35,36,37,39,40,41,42,],[-27,-7,-24,-21,-11,-15,-17,-25,-26,-13,33,-27,-14,-20,41,-8,-10,-9,-6,-5,42,-19,-12,-16,]),'ASSIGN':([1,7,],[15,25,]),'DIVIDE':([1,3,5,7,9,10,11,12,13,16,18,19,26,28,30,33,34,35,36,37,40,41,42,],[-25,-27,21,-26,-24,-21,-11,-15,-17,-25,-26,-13,-27,-14,-20,-8,-10,-9,21,21,-19,-12,-16,]),'EXPONENT':([1,3,7,9,10,16,18,26,30,33,41,42,],[-25,-27,-26,-24,29,-25,-26,-27,-22,-23,-23,-23,]),'FUNCTION_0':([0,3,4,8,15,17,21,22,23,24,25,27,29,],[7,18,18,18,18,18,18,18,18,18,18,18,18,]),'MINUS':([0,1,3,4,5,6,7,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[8,-25,8,8,-7,23,-26,-24,-21,-11,-15,-17,8,-25,8,-26,-13,23,8,8,8,8,8,-27,8,-14,8,-20,23,23,-8,-10,-9,-6,-5,23,23,-19,-12,-16,]),'NUMBER':([0,3,4,8,15,17,21,22,23,24,25,27,29,],[9,9,9,9,9,9,9,9,9,9,9,9,9,]),'$end':([0,1,2,3,5,6,7,9,10,11,12,13,14,16,18,19,26,28,30,31,33,34,35,36,37,38,40,41,42,],[-28,-25,-4,-27,-7,-3,-26,-24,-21,-11,-15,-17,0,-25,-26,-13,-27,-14,-20,-1,-8,-10,-9,-6,-5,-2,-19,-12,-16,]),'PLUS':([1,3,5,6,7,9,10,11,12,13,16,18,19,20,26,28,30,31,32,33,34,35,36,37,38,39,40,41,42,],[-25,-27,-7,24,-26,-24,-21,-11,-15,-17,-25,-26,-13,24,-27,-14,-20,24,24,-8,-10,-9,-6,-5,24,24,-19,-12,-16,]),'TIMES':([1,3,5,7,9,10,11,12,13,16,18,19,26,28,30,33,34,35,36,37,40,41,42,],[-25,-27,22,-26,-24,-21,-11,-15,-17,-25,-26,-13,-27,-14,-20,-8,-10,-9,22,22,-19,-12,-16,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'empty':([0,],[2,]),'factorial':([0,3,4,8,15,17,21,22,23,24,25,27,29,],[10,10,10,10,10,10,10,10,10,10,10,10,10,]),'term':([0,3,4,15,17,21,22,23,24,25,27,29,],[11,19,11,11,11,34,35,11,11,11,11,40,]),'factor':([0,4,15,17,23,24,25,27,],[5,5,5,5,36,37,5,5,]),'unary':([0,3,4,8,15,17,21,22,23,24,25,27,29,],[12,12,12,28,12,12,12,12,12,12,12,12,12,]),'expression':([0,4,15,17,25,27,],[6,20,31,32,38,39,]),'exponential':([0,3,4,8,15,17,21,22,23,24,25,27,29,],[13,13,13,13,13,13,13,13,13,13,13,13,13,]),'statement':([0,],[14,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> IDENTIFIER ASSIGN expression','statement',3,'p_assign_expression','calcparse.py',10),
  ('statement -> FUNCTION_0 ASSIGN expression','statement',3,'p_define_function','calcparse.py',15),
  ('statement -> expression','statement',1,'p_statement','calcparse.py',20),
  ('statement -> empty','statement',1,'p_statement_empty','calcparse.py',24),
  ('expression -> expression PLUS factor','expression',3,'p_expression_plus','calcparse.py',28),
  ('expression -> expression MINUS factor','expression',3,'p_expression_minus','calcparse.py',32),
  ('expression -> factor','expression',1,'p_expression_factor','calcparse.py',36),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_parenthesis','calcparse.py',40),
  ('factor -> factor TIMES term','factor',3,'p_factor_multiplication','calcparse.py',44),
  ('factor -> factor DIVIDE term','factor',3,'p_factor_divide','calcparse.py',48),
  ('factor -> term','factor',1,'p_factor_term','calcparse.py',52),
  ('term -> LPAREN expression RPAREN','term',3,'p_term_parenthesis','calcparse.py',56),
  ('term -> FUNCTION_1 term','term',2,'p_term_function_unary','calcparse.py',61),
  ('term -> MINUS unary','term',2,'p_term_negative_unary','calcparse.py',66),
  ('term -> unary','term',1,'p_term_unary','calcparse.py',70),
  ('unary -> LPAREN expression RPAREN','unary',3,'p_unary_parenthesis','calcparse.py',74),
  ('unary -> exponential','unary',1,'p_unary_exponential','calcparse.py',78),
  ('exponential -> LPAREN expression RPAREN','exponential',3,'p_exponential_parenthesis','calcparse.py',82),
  ('exponential -> factorial EXPONENT term','exponential',3,'p_exponential_exponential','calcparse.py',86),
  ('exponential -> factorial FACTORIAL','exponential',2,'p_real_factorial','calcparse.py',90),
  ('exponential -> factorial','exponential',1,'p_exponential_factorial','calcparse.py',94),
  ('factorial -> factorial FACTORIAL','factorial',2,'p_repeat_factorial','calcparse.py',98),
  ('factorial -> LPAREN expression RPAREN','factorial',3,'p_factorial_parenthesis','calcparse.py',102),
  ('factorial -> NUMBER','factorial',1,'p_to_number','calcparse.py',106),
  ('factorial -> IDENTIFIER','factorial',1,'p_to_variable','calcparse.py',110),
  ('factorial -> FUNCTION_0','factorial',1,'p_to_function_0','calcparse.py',114),
  ('factorial -> FUNCTION_1','factorial',1,'p_to_function_1','calcparse.py',118),
  ('empty -> <empty>','empty',0,'p_empty','calcparse.py',122),
]