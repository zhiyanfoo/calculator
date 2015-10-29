from orders import OrderToken

def remove_ini_whitespace(line):
    i = 0
    while(line[i] == " "):
        i += 1
    return line[i:]

def keep_getting_input(input_method):
    run = app()
    while True:
        inp = input_method()
        app.get_raw(inp)

class app:
    raw_calc_input = list()
    calc_input = list()
    corresponding_output = list()

    def get_raw(self, inp):
        inp_no_ini_space = remove_ini_whitespace(inp)
        # if inp_no_ini_space[0] == "@":


            


