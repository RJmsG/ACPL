output = []
aput = []
ac = ''
fncs = []
ignore = []
var = ['ac']
tpe = ['int']
dt = ['str', 'int', 'dec']

def tproc(inp):
  if inp == 'str':
    return '%s'
  elif inp == 'int':
    return '%d'
  elif inp == 'float':
    return '%f'
  elif inp == '~str':
    return '%c'
  elif inp == '~int':
    return '%d'
  elif inp == '~float':
    return '%f'

def strp(inp):
  a = ''
  for i in inp:
    if i == ':':
      a += '('
    elif i == ';':
      a += ')'
    elif i == '!':
      a += '(int)'
    elif i == '^':
      a += '(float)'
    else:
      a += i
  return a

def comln(inp):
  global ac
  global dt
  global tpe
  args = inp.split(' ')
  if args[0] == 'vlen':
    tp = args[1]
    name = args[2]
    del args[0]
    del args[0]
    del args[0]
    var.append(name)
    tpe.append(tp)
    if tp == 'str':
      if len(args) == 1:
        if len(args[0]) == 1:
          output.append(f'char {name} = {strp(args[0])};')
        else:
          output.append(f'char {name}[] = {strp(" ".join(args))};')
      elif len(args) == 0:
        output.append(f'char {name}[] = {strp(" ".join(args))};')
      else:
        output.append(f'char {name}[ac];')
    elif tp == 'int':
      if len(args) == 1:
        if len(args[0]) == 1:
          output.append(f'int {name} = {args[0]};')
        else:
          output.append(f'int {name}[] = {strp(" ".join(args))};')
      elif len(args) == 0:
        output.append(f'int {name}[] = {strp(" ".join(args))};')
      else:
        output.append(f'int {name}[ac];')
    elif tp == 'dec':
      if len(args) == 1:
        if len(args[0]) == 1:
          output.append(f'float {name} = {args[0]};')
        else:
          output.append(f'float {name}[] = {strp(" ".join(args))};')
      elif len(args) == 0:
        output.append(f'float {name}[] = {strp(" ".join(args))};')
      else:
        output.append(f'float {name}[ac];')
    args = ['']
  elif args[0] in dt:
    tp = args[0]
    name = args[1]
    del args[0]
    del args[0]
    var.append(name)
    tpe.append('~' + tp)
    if tp == 'str':
      output.append(f'char* {name};')
      output.append(f'{name} = (char*)malloc(ac * sizeof(char));')
      output.append(f'if({name}==NULL)' + ' {printf("FAILED TO ALLOCATED MEMORY");} else {int i = 0;')
      if len(args) > 0:
        c = 0
        for i in ' '.join(args):
          c += 1
          output.append(f'i++;{name}[i] = \'{i}\';')
      output.append('}')
    elif tp == 'int':
      output.append(f'int* {name};')
      output.append(f'{name} = (int*)malloc(ac * sizeof(int));')
      output.append(f'if({name}==NULL)' + ' {printf("FAILED TO ALLOCATED MEMORY");} else {int i = 0;')
      if len(args) > 0:
        c = 0
        for i in args:
          c += 1
          output.append(f'i++;{name}[i] = {i};')
      output.append('}')
    elif tp == 'dec':
      output.append(f'float* {name};')
      output.append(f'{name} = (float*)malloc(ac * sizeof(float));')
      output.append(f'if({name}==NULL)' + ' {printf("FAILED TO ALLOCATED MEMORY");} else {int i = 0;')
      if len(args) > 0:
        c = 0
        for i in args:
          c += 1
          output.append(f'i++;{name}[i] = {i};')
      output.append('}')
    args = ['']
  elif args[0] == 'func':
    name = args[1]
    del args[0]
    del args[0]
    output.insert(0, f'void {name}({" ".join(args)});')
    aput.append(f'void {name}({" ".join(args)})')
    fncs.append(name)
    args = [args[len(args) - 1]]
  elif args[0] == ':':
    output.append('{')
  elif args[0] == ';':
    output.append('}')
  elif args[0] == 'on':
    if args[2] == '=':
      if tpe[var.index(args[1])] == 'str':
        output.append(f'if (strcmp({args[1]},{args[3]})==0)')
      else:
        output.append(f'if ({args[1]} == {args[3]})')
    elif args[2] == '>':
      output.append(f'if ({args[1]} > {args[3]})')
    elif args[2] == '<':
      output.append(f'if ({args[1]} < {args[3]})')
    elif args[2] == '!':
      output.append(f'if ({args[1]} != {args[3]})')
  elif args[0] == 'or':
    if args[2] == '=':
      if tpe(var.index(args[1])) == 'str':
        output.append(f'else if (strcmp({args[1]},{args[3]})==0)')
      else:
        output.append(f'else if ({args[1]} == {args[3]})')
    elif args[2] == '>':
      output.append(f'else if ({args[1]} > {args[3]})')
    elif args[2] == '<':
      output.append(f'else if ({args[1]} < {args[3]})')
    elif args[2] == '!':
      output.append(f'else if ({args[1]} != {args[3]})')
  elif args[0] == '!on':
    output.append('else')
  elif args[0] in fncs:
    name = args[0]
    del args[0]
    output.append(f'{name}({strp(" ".join(args))});')
    args = ['']
  elif args[0] == 'sac':
    output.append(f'ac = {args[1]};')
  elif args[0] in var:
    name = args[0]
    del args[0]
    if tpe[var.index(name)][0] == '~' or tpe[var.index(args[0])][0] == '~':
      output.append('for(i=0;i<ac;++i) {' + f'{name}[i] = {args[0]}[i];' + '}')
    else:
      output.append(f'{name} = {strp(" ".join(args))}')
    args = ['']
  elif args[0] == '#':
    pass
  elif args[0] == 'outln':
    del args[0]
    output.append(f'puts({" ".join(args)});')
    args = ['']
  elif args[0] == 'in':
    var.append(args[1])
    tpe.append('str')
    output.append(f'char {args[1]}[{args[2]}];')
    output.append(f'scanf("%{args[2]}s", {args[1]});')
  elif args[0] == 'outvar':
    t = tpe[var.index(args[1])]
    if t[0] == '~':
      output.append('for(i=0;i<ac;++i) {printf("' + tproc(t) + '", ' + args[1] + '[i]);}')
    else:
      output.append(f'printf("{tproc(t)}", {args[1]});')
  else:
    if not args[0] == '':
      print(f'Error while compiling: "{args[0]}" is not an included variable or function.')