import sys
sys.path.append("../calculator")
from main import App
from calcparse import calcparser

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

def check_parser(data, expected, capsys):
    assert expected == calcparser.parse(data)
    out, err = capsys.readouterr()
    assert err == ""


def check_multiline_calc(data, expected, capsys):
    output = DataOutputMethod()
    app = App(DataInputMethod(data), output)
    app.run()
    assert output.output == expected
    out, err = capsys.readouterr()
    assert err == ''

