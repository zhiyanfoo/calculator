import re

class OrderToken:
    #keywords : number of arguements they can have
    keywords = {
            "fractional" : (0,),
            "numeric": (0,),  
            "printall": (0,),
            "insert" : (1,),
            "print" : (0,1), 
            "remove" : (0,1) , 
            "replace" : (1,2), 
            }

    def __init__(self, lexemes):
        self.value = self.valid_value(lexemes[0]) 
        self.args = self.valid_args(lexemes[1:])

    def valid_value(self, value):
        if value in self.keywords:
            return value
        else:
            raise ValueError("Invalid order: {0}".format(value))

    def valid_args(self, args):
        if len(args) not in self.keywords[self.value]:
            errmsg = "Order \"{0}\" given invalid number of arguments ({1}), args: \"{2}\"".format(self.value, len(args), args)
            raise ValueError(errmsg)
        # p_list = re.compile(r"(?:\d+,)*\d")
        # # p_range = re.compile(r"\d*..\d*")

        # for num_arg in args:
        #     if p_list.match(num_arg) == None:
        #         errmsg = "\"{0}\" given invalid argument \"{1}\"".format(self.value, num_arg)
        #         raise ValueError(errmsg)
        # # return args






