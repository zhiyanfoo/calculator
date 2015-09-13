def remove_ini_whitespace(string):
    i = 0
    while(string[i] == " "):
        i += 1
    return string[i:]

def run():
    while True:
        inp = input("> ")
        stripped_inp = remove_ini_whitespace(inp)
        

    


