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
            insert_pos = len(exp_list)
            numeric = False
            if "replace" in parsed.commands.keys():
                insert_pos = parsed.commands["replace"]
            if "numeric" in parsed.commands.keys():
                numeric = True
            evaluater.insert(simplified_exp_tree(), insert_pos)
            if "printall" in parsed.commands.keys():
                print(evaluater.return_all(), numeric)
            else:
                print(evaluater.return_normal(), numeric)
            if "quit" in parsed.commands.keys():
                exit(0)
        else:
            print("Syntax Error")
            print(inp)
