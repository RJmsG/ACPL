output = []
end = False
aput = []
ac = ''
fncs = []
ignore = []
var = ['ac']
tpe = ['int']
dt = ['str', 'int', 'dec']
args = []

def clargs(am):
  for i in range(am):
    del args[0]
    
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

def varset(tp, name, args):
  if len(args) == 1:
        if len(args[0]) == 1:
          output.append(f'{tp} {name} = {strp(args[0])};')
        else:
          output.append(f'{tp} {name}[] = {strp(" ".join(args))};')
      elif len(args) == 0:
        output.append(f'{tp} {name}[] = {strp(" ".join(args))};')
      else:
        output.append(f'{tp} {name}[ac];')

def dynvarset(tp, name, args):
  output.append(f'{tp}* {name};')
  output.append(f'{name} = ({tp}*)malloc(ac * sizeof({tp}));')
  output.append(f'if({name}==NULL)' + ' {printf("FAILED TO ALLOCATED MEMORY");} else {int i = 0;')
  if len(args) > 0:
    c = 0
    for i in ' '.join(args):
      c += 1
      output.append(f'i++;{name}[i] = \'{i}\';')
  output.append('}')

def endmain():
  output.append('return 0;')
  output.append('}')
  end = True