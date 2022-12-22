import acplmod

print('ACPL A22\'3 compiler UI 0.2 (acpl Beta 1.3.0 Build 2)\n(For more information, go type \'help\' or go to the GitHub repository at https://github.com/RJmsG/ACPL)')

while True:
    i = input('ACPL>').split(' ')
    if i[0] == 'compile':
        file = i[1]
        sf = True
        exec = False
        mt = 'int'
        p = ''
        el = []
        compile = True
        if len(i) > 2:
            del i[0];del i[0]
            while len(i) > 0:
                if i[0] == '&savefile':
                    sf = False
                    del i[0]
                elif i[0] == '&execute':
                    exec = True
                    del i[0]
                elif i[0] == '?mtype':
                    mt = i[1]
                    del i[0];del i[0]
                elif i[0] == '?path':
                    p = i[1]
                    del i[0];del i[0]
                elif i[0] == '+lib':
                    el.append(i[1])
                    del i[0];del i[0]
                else:
                    print('Error: Unidintified or more than requiered args detected!')
                    compile = False
        if compile:
            acplmod.compilef(savefile=sf, execute=exec, file=file, path=p, extra_libs=el, mtype=mt)
    elif i[0] == 'help':
        print('Commands: compile, quit')
    elif i[0] == 'quit':
        quit()
    else:
        print(i[0], 'is not a real usable command. Please refer to \'help\'')