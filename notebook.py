data = [
    "3 + 7",
    " 3 ^ 2",
    "  @exit"
    ]

class DataInputMethod:
    def __init__(self, data):
        self.data = data
        self.count = -1

    def __call__(self):
        self.count += 1
        return(data[self.count])
        
input_method = DataInputMethod(data)
print(input_method())
print(input_method())
print(input_method())
