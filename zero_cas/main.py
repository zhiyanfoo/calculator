from orders import OrderToken

def remove_ini_whitespace(line):
    i = 0
    while(line[i] == " "):
        i += 1
    return line[i:]



class app:
    def __init__(self, input_method, exit_method):
        self.raw_calc_input = list()
        self.calc_input = list()
        self.corresponding_output = list()
        self.input_method = input_method
        self.exit_method = exit_method 

    def run(self):
        while True:
            inp = self.input_method()


    def get_raw(self, inp):
        inp_no_ini_space = remove_ini_whitespace(inp)
        # if inp_no_ini_space[0] == "@":


            


