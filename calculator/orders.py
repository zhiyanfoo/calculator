import re

class OrderToken:
    def __init__(self, lexemes, keywords):
        self.keywords = keywords
        self.value = self.valid_value(lexemes[0]) 
        self.args = self.valid_args(lexemes[1:])

    def valid_value(self, value):
        if value in self.keywords:
            return value
        else:
            raise ValueError("Invalid order: {0}".format(value))

    def valid_args(self, lexeme_args):
        if len(lexeme_args) not in self.keywords[self.value][0]:
            errmsg = "Order \"{0}\" given invalid number of arguments ({1}), args: \"{2}\"".format(self.value, len(lexeme_args), lexeme_args)
            raise ValueError(errmsg)
        p_list = re.compile(r"^(?:\d+,)*\d$")
        p_range = re.compile(r"^\d*..\d*$")
        args = list()

        for num_arg in lexeme_args:
            if p_list.match(num_arg) is not None:
                parsed_arg = tuple([int(num) for num in num_arg.split(',')])
                args.append(parsed_arg)
            elif p_range.match(num_arg) is not None:
                start_end = [int(num) for num in num_arg.split('..') if num != ""]
                if len(start_end) > 2:
                    errmsg = "\"{0}\" given invalid range\"{1}\"".format(self.value, num_arg)
                    raise ValueError(errmsg)
                for num in start_end:
                    if num < 0:
                        errmsg = "\"{0}\" given invalid range \"{1}\", negative number".format(self.value, num)
                        raise ValueError(errmsg)
                if len(start_end) == 2 and start_end[0] > start_end[1]:
                    errmsg = "\"{0}\" given invalid range \"{1}\", {2} more than {3}".format(self.value, num_arg, start_end[0], start_end[1])
                    raise ValueError(errmsg)
                parsed_arg = tuple(range(start_end[0], start_end[1]+1))
                args.append(parsed_arg)
            else:
                errmsg = "\"{0}\" given invalid argument \"{1}\"".format(self.value, num_arg)
                raise ValueError(errmsg)
        return args

