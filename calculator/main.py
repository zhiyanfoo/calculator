from orders import OrderToken
# from calcparse import calcparser
from simplify import simplify

class App:
    def __init__(self, input_method, output_method):
        self.input_method = input_method
        self.raw_calc_input = list()
        self.processed_calc_input = list()
        self.calc_output = list()
        self.decimal = True
        self.keywords = {
                "exit" : ((0,), None), 
                "integers" : ((0,), self.integer_on),
                "decimal": ((0,), self.decimal_on),
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
                if order.value == 'exit':
                    break
            else:
                self.raw_calc_input.append(inp)
                self.processed_calc_input.append(self.preprocess(inp))
                self.calc_output.append(simplify(calcparser.parse(self.processed_calc_input[-1])))

    def preprocess(self, raw_line):
        return raw_line

    def integer_on(self):
        self.decimal = False

    def decimal_on(self):
        self.decimal = True

    def printall(self):
        self.keywords['print'][1](self.calc_output, range(0, len(self.calc_output)))

    def insert(self):
        pass

    def remove(self):
        pass

    def replace(self):
        pass



            


