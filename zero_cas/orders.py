import re

def calc_exit():
    exit(0)
def fractional():
    pass
def numeric():
    pass
def printall():
    pass
def insert():
    pass
def calc_print():
    pass
def remove():
    pass
def replace():
    pass

# keywords : number of arguements they can have
keywords = {
        "exit" : ((0,), calc_exit), 
        "fractional" : ((0,), fractional),
        "numeric": ((0,), numeric),
        "printall": ((0,), printall),
        "insert" : ((1,), insert),
        "print" : ((0,1), calc_print),
        "remove" : ((0,1) , remove),
        "replace" : ((1,2), replace),
        }

def perform_order(raw_order_input):
    pass



class OrderToken:

    def __init__(self, lexemes):
        self.value = self.valid_value(lexemes[0]) 
        self.args, self.args_type = self.valid_args(lexemes[1:])

    def valid_value(self, value):
        if value in keywords:
            return value
        else:
            raise ValueError("Invalid order: {0}".format(value))

    def valid_args(self, lexeme_args):
        if len(lexeme_args) not in keywords[self.value][0]:
            errmsg = "Order \"{0}\" given invalid number of arguments ({1}), args: \"{2}\"".format(self.value, len(lexeme_args), lexeme_args)
            raise ValueError(errmsg)
        p_list = re.compile(r"^(?:\d+,)*\d$")
        p_range = re.compile(r"^\d*..\d*$")
        args = list()
        args_type = list()

        for num_arg in lexeme_args:
            if p_list.match(num_arg) is not None:
                args_type.append("list")
                parsed_arg = tuple([int(num) for num in num_arg.split(',')])
                args.append(parsed_arg)
            elif p_range.match(num_arg) is not None:
                args_type.append("range")
                parsed_arg = tuple([int(num) for num in num_arg.split('..') if num != ""])
                if len(parsed_arg) > 2:
                    errmsg = "\"{0}\" given invalid range\"{1}\"".format(self.value, num_arg)
                    raise ValueError(errmsg)
                for num in parsed_arg:
                    if num < 0:
                        errmsg = "\"{0}\" given invalid range \"{1}\", negative number".format(self.value, num)
                        raise ValueError(errmsg)
                if len(parsed_arg) == 2 and parsed_arg[0] > parsed_arg[1]:
                    errmsg = "\"{0}\" given invalid range \"{1}\", {2} more than {3}".format(self.value, num_arg, parsed_arg[0], parsed_arg[1])
                    raise ValueError(errmsg)
                args.append(parsed_arg)
            else:
                errmsg = "\"{0}\" given invalid argument \"{1}\"".format(self.value, num_arg)
                raise ValueError(errmsg)
        return args, args_type

