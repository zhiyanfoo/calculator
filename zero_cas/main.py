from orders import OrderToken
from calcparse import calcparser

class App:
    def __init__(self, input_method, output_method):
        self.input_method = input_method
        self.raw_calc_input = list()
        self.processed_calc_input = list()
        self.calc_output = list()
        self.numeric = True
        self.keywords = {
                "exit" : ((0,), self.exit), 
                "fractional" : ((0,), self.fractional_on),
                "numeric": ((0,), self.numeric_on),
                "printall": ((0,), self.printall),
                "insert" : ((1,), self.insert),
                "print" : ((0,1), output_method),
                "remove" : ((0,1) , self.remove),
                "replace" : ((1,2), self.replace),
                }

    def run(self):
        while True:
            inp = self.input_method()
            inp_strip = inp.strip()
            if inp_strip[0] == '@':
                inp_split = inp_strip[1:].split()
                order = OrderToken(inp_split, self.keywords)
                should_exit = self.keywords[order.value][1](*order.args)
                if should_exit == True:
                    break
            else:
                self.raw_calc_input.append(inp)
                self.processed_calc_input.append(self.preprocess(inp))
                self.calc_output.append(calcparser.parse(self.processed_calc_input[-1]))

    def preprocess(self, raw_line):
        return raw_line

    def exit(self):
        return True

    def fractional_on(self):
        pass

    def numeric_on(self):
        pass

    def printall(self):
        self.keywords['print'][1](self.calc_output, range(0, len(self.calc_output)))

    def insert(self):
        pass

    def remove(self):
        pass

    def replace(self):
        pass



            


