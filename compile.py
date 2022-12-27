from compilemod import *


def comln(inp):
  args = inp.split(' ')
  ina = args[0]
  if ina == 'vlen':
    tp = args[1]
    name = args[2]
    clargs(3)
    var.append(name)
    tpe.append(tp)
    varset(tp, name, args)
    args = ['']
  elif ina in dt:
    tp = args[0]
    name = args[1]
    clargs(2)
    var.append(name)
    tpe.append('~' + tp)
    dynvarset(tp, name, args)
    args = ['']
  elif ina == 'func':
    name = args[1]
    clargs(2)
    output.insert(0, f'void {name}({" ".join(args)});')
    endmain()
    output.append(f'void {name}({" ".join(args)})')
    fncs.append(name)
    args = [args[len(args) - 1]]
  elif ina == ':':
    output.append('{')
  elif ina == ';':
    output.append('}')
  elif ina == 'on':
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
  elif ina == 'or':
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
  elif ina == '!on':
    output.append('else')
  elif ina in fncs:
    name = args[0]
    del args[0]
    output.append(f'{name}({strp(" ".join(args))});')
    args = ['']
  elif ina == 'sac':
    output.append(f'ac = {args[1]};')
  elif valid(ina):
    del args[0]
    output.append(f'{vstrp[ina]} = {vstrp(args)}')
    args = []
    """""
    if tpe[var.index(name)][0] == '~' or tpe[var.index(args[0])][0] == '~':
      output.append('for(i=0;i<ac;++i) {' + f'{name}[i] = {args[0]}[i];' + '}')
    else:
      output.append(f'{name} = {strp(" ".join(args))}')
    args = ['']
    """""
  elif ina == '#':
    pass
  elif ina=='type':
    output.insert(0, "struct")
  elif ina == 'outln':
    del args[0]
    output.append(f'puts({" ".join(args)});')
    args = ['']
  elif ina == 'in':
    var.append(args[1])
    tpe.append('str')
    output.append(f'char {args[1]}[{args[2]}];')
    output.append(f'scanf("%{args[2]}s", {args[1]});')
  elif ina == 'outvar':
    t = tpe[var.index(args[1])]
    if t[0] == '~':
      output.append('for(i=0;i<ac;++i) {printf("' + tproc(t) + '", ' + args[1] + '[i]);}')
    else:
      output.append(f'printf("{tproc(t)}", {args[1]});')
  elif ina == "import":
    file = open(args[1]  + ".acpl", "r")
    l = file.readlines()
    for i in l:
      lines.append(i)
    file.close()
  elif ina == "include":
    file = open(args[1] + ".c", "r")
    output.append(file.readline())
    file.close()
  else:
    if not ina in ['',' ']:
      print(f'Error while compiling: Input "{ina}"" is foreign to the compiler.')
