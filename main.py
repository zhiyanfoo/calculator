from parser import Parser
from rewrite import simplify
from evaluater import Evaluater
    
def input_mode():
    evaluater = Evaluater()
    while True:
        inp = input()
        parsed = Parser(inp)
        if parsed.is_valid:
            simplified_exp_tree = simplify(parsed.exp_tree)
            # default command options
            insert_pos = len(Evaluater.exp_list)
            is_numeric = False
            if "replace" in parsed.commands:
                insert_pos = parsed.commands["replace"]
            if "numeric" in parsed.commands:
                is_numeric = True
            evaluater.insert(simplified_exp_tree, insert_pos)
            if "printall" in parsed.commands:
                print(evaluater.return_all(), is_numeric)
            else:
                print(evaluater.return_normal(), is_numeric)
            if "quit" in parsed.commands:
                exit(0)
        else:
            print("Syntax Error")
            print(inp)
