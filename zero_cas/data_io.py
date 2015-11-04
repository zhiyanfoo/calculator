class DataInputMethod:
    def __init__(self, data):
        self.data = data
        self.count = -1

    def __call__(self):
        self.count += 1
        return(self.data[self.count])

class DataOutputMethod:
    def __init__(self):
        self.output = list()

    def __call__(self, calc_output, lines):
        for i in lines:
            self.output.append(calc_output[i])