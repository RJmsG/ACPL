symbols = ["'",'"','!','.','=','+','-','\\','*',',','(',')']

def tokenize(inp):
    arg = []
    a = ''
    for i in inp:
        if i in symbols:
            if not a == '':
                arg.append(a)
                a = ''
            arg.append(i)
        elif not i == ' ':
            a += i
        else:
            arg.append(a)
            a = ''
    for i in arg:
        print(i)