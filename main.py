import acpllib

print('ACPL A23 compiler UI 0.2 (pyacpl Beta 1.3.2)\n(For more information, go type \'help\' or go to the GitHub repository at https://github.com/RJmsG/ACPL)')

while True:
    i = input('ACPL>').split(' ')
    if i[0] == 'compile':
        file = i[1]
        sf = True
        exe = False
        mt = 'int'
        p = ''
        el = []
        comp = True
        if len(i) > 2:
            del i[0];del i[0]
            while len(i) > 0:
                if i[0] == '&savefile':
                    sf = False
                    del i[0]
                elif i[0] == '&execute':
                    exe = True
                    del i[0]
                elif i[0] == '?mtype':
                    mt = i[1]
                    del i[0];del i[0]
                elif i[0] == '?path':
                    p = i[1]
                    del i[0];del i[0]
                else:
                    print('Error: Unidintified or more than requiered args detected!')
                    comp = False
        if comp:
            acpllib.compilef(savefile=sf, execute=exec, file=file, path=p, mtype=mt)
    elif i[0] == 'help':
        print('Commands: compile, quit')
    elif i[0] == 'quit':
        quit()
    else:
        print(i[0], 'is not a real usable command. Please refer to \'help\'')