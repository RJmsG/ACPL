"""
ACPL DB4 A22'1 Transpiler
"""
output = []
aput = []
ac = ''
fncs = []
ignore = []
var = []
tpe = []
dt = ['str', 'int', 'dec']

def strp(inp):
  a = ''
  for i in inp:
    if i == ':':
      a += '('
    elif i == ';':
      a += ')'
    elif i == '!':
      a += '(int)'
    elif i == '*':
      a += '(float)'
    else:
      a += i
  return a

def comln(inp):
  global ac
  global dt
  global tpe
  args = inp.split(' ')
  if args[0] in dt:
    tp = args[0]
    name = args[1]
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
    output.append('ac = {args[1]};')
  elif args[0] in var:
    name = args[0]
    del args[0]
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
  elif args[0] == 'outs':
    output.append(f'printf("%s", {args[1]});')
  elif args[0] == 'outi':
    output.append(f'printf("%d", {args[1]});')
  else:
    if not args[0] == '':
      print(f'Error while compiling: "{args[0]}" is not an included variable or function.')

def compilef(file):
  global output
  print(f'Compiling "{file}.acpl"...')
  f1 = open((file + '.acpl'), 'r')
  lines = f1.readlines()
  output.append('#include <stdio.h>')
  output.append('#include <stdlib.h>')
  output.append('#include <string.h>')
  output.append('int main() {')
  output.append('int ac = 1;')
  for i in lines:
    a = []
    for o in range(len(i)):
      if not o > (len(i) - 2):
        a.append(i[o])
    i = ''.join(a)
    comln(i)
  output.append('return 0;')
  output.append('}')
  output += aput
  print('DONE!')
