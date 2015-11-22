
# ../calculator/parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.5'

_lr_method = 'LALR'

_lr_signature = '9642D1381EC116B4D0F471C2E7AFDAD3'
    
_lr_action_items = {'FUNCTION_1':([0,1,3,6,9,13,14,15,16,17,],[1,1,1,1,1,1,1,1,1,1,]),'!':([2,5,7,10,11,12,18,19,20,21,22,23,24,25,26,],[-13,12,-14,-11,12,-8,12,12,-12,-6,12,12,12,12,-10,]),'(':([0,1,3,6,9,13,14,15,16,17,],[3,9,3,3,3,3,3,3,3,3,]),'-':([0,1,2,3,5,6,7,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[6,6,-13,6,16,6,-14,6,-11,16,-8,6,6,6,6,6,-7,16,-12,-6,-4,-2,-3,-5,-10,]),'*':([2,5,7,10,11,12,18,19,20,21,22,23,24,25,26,],[-13,14,-14,-11,14,-8,-7,14,-12,-6,-4,14,14,-5,-10,]),'^':([2,5,7,10,11,12,18,19,20,21,22,23,24,25,26,],[-13,13,-14,13,13,-8,13,13,-12,13,13,13,13,13,-10,]),'NUMBER':([0,1,3,6,9,13,14,15,16,17,],[2,2,2,2,2,2,2,2,2,2,]),'IDENTIFIER':([0,1,3,6,9,13,14,15,16,17,],[7,7,7,7,7,7,7,7,7,7,]),')':([2,7,10,11,12,18,19,20,21,22,23,24,25,26,],[-13,-14,-11,20,-8,-7,26,-12,-6,-4,-2,-3,-5,-10,]),'/':([2,5,7,10,11,12,18,19,20,21,22,23,24,25,26,],[-13,17,-14,-11,17,-8,-7,17,-12,-6,-4,17,17,-5,-10,]),'+':([2,5,7,10,11,12,18,19,20,21,22,23,24,25,26,],[-13,15,-14,-11,15,-8,-7,15,-12,-6,-4,-2,-3,-5,-10,]),'$end':([0,2,4,5,7,8,10,12,18,20,21,22,23,24,25,26,],[-15,-13,-9,-1,-14,0,-11,-8,-7,-12,-6,-4,-2,-3,-5,-10,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,1,3,6,9,13,14,15,16,17,],[5,10,11,18,19,21,22,23,24,25,]),'statement':([0,],[8,]),'empty':([0,],[4,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> expression','statement',1,'p_statement_expression','calcparse.py',28),
  ('expression -> expression + expression','expression',3,'p_expression_binop','calcparse.py',32),
  ('expression -> expression - expression','expression',3,'p_expression_binop','calcparse.py',33),
  ('expression -> expression * expression','expression',3,'p_expression_binop','calcparse.py',34),
  ('expression -> expression / expression','expression',3,'p_expression_binop','calcparse.py',35),
  ('expression -> expression ^ expression','expression',3,'p_expression_binop','calcparse.py',36),
  ('expression -> - expression','expression',2,'p_expression_negative','calcparse.py',46),
  ('expression -> expression !','expression',2,'p_expression_postfix','calcparse.py',50),
  ('statement -> empty','statement',1,'p_statement_empty','calcparse.py',54),
  ('expression -> FUNCTION_1 ( expression )','expression',4,'p_expression_function_1_paren','calcparse.py',58),
  ('expression -> FUNCTION_1 expression','expression',2,'p_expression_function_1','calcparse.py',62),
  ('expression -> ( expression )','expression',3,'p_expression_parenthesis','calcparse.py',66),
  ('expression -> NUMBER','expression',1,'p_expression_number','calcparse.py',70),
  ('expression -> IDENTIFIER','expression',1,'p_expression_identifier','calcparse.py',74),
  ('empty -> <empty>','empty',0,'p_empty','calcparse.py',140),
]
