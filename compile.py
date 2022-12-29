from compilemod import *
import compilemod as cmod


def comln(inp):
  args = inp.split(' ')
  ina = args[0]
  if ina == 'vlen':
    tp = args[1]
    name = args[2]
    args = clargs(3,args)
    var.append(name)
    tpe.append(tp)
    varset(tp, name, args)
    args = ['']
  elif ina in dt:
    tp = args[0]
    name = args[1]
    args=clargs(2,args)
    var.append(name)
    tpe.append('~' + tp)
    dynvarset(tp, name, args)
    args = ['']
  elif ina == 'func':
    fncs.append(args[1])
    name = args[1]
    print(args)
    args=clargs(2,args)
    print(args)
    nout(f'void {name}({" ".join(args)}) '+'{')
    cmod.bg = False
    cmod.fd += 1
    args = [args[len(args) - 1]]
  elif ina == 'vfunc':
    fncs.append(args[1])
  elif ina == ':':
    oapp('{')
    cmod.fd += 1
  elif ina == '!':
    oapp('}')
    cmod.fd -= 1
  elif ina == 'on':
    if args[2] == '=':
      if tpe[var.index(args[1])] == 'str':
        oapp(f'if (strcmp({args[1]},{args[3]})==0)')
      else:
        oapp(f'if ({args[1]} == {args[3]})')
    elif args[2] == '>':
      oapp(f'if ({args[1]} > {args[3]})')
    elif args[2] == '<':
      oapp(f'if ({args[1]} < {args[3]})')
    elif args[2] == '!':
      oapp(f'if ({args[1]} != {args[3]})')
  elif ina == 'or':
    if args[2] == '=':
      if tpe(var.index(args[1])) == 'str':
        oapp(f'else if (strcmp({args[1]},{args[3]})==0)')
      else:
        oapp(f'else if ({args[1]} == {args[3]})')
    elif args[2] == '>':
      oapp(f'else if ({args[1]} > {args[3]})')
    elif args[2] == '<':
      oapp(f'else if ({args[1]} < {args[3]})')
    elif args[2] == '!':
      oapp(f'else if ({args[1]} != {args[3]})')
  elif ina == '!on':
    oapp('else')
  elif ina in fncs:
    name = args[0]
    del args[0]
    oapp(f'{name}({strp(" ".join(args))});')
    args = []
  elif ina == 'sac':
    oapp(f'ac = {args[1]};')
  elif valid(ina):
    del args[0]
    oapp(f'{vstrp[ina]} = {vstrp(args)}')
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
  elif ina == 'import':
    file = open(args[1]  + ".acpl", "r")
    l = file.readlines()
    print(l)
    a = linef(l)
    print(a)
    for i in a:
      comln(i)
    file.close()
  elif ina == "cinc":
    nout(f"#include <{args[1][0:len(args[1])]}>")
  else:
    if not ina in ['',' ']:
      print(f'Error while compiling: Input "{ina}" is foreign to the compiler.')
