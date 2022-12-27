lines = []
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
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

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
  output.append(f'{tp}* {name} = strdup({args});')

def endmain():
  output.append('return 0;')
  output.append('}')
  end = True

def valid(arg):
  v = arg.split('.')
  if v[0] in var:
    return True
  else:
    return False

def varf(arg):
  v = arg.split('.')
  if len(v) == 2:
    a = v[1][1]
    if a in letters:
      return 'f'
    elif a in numbers:
      return 'i'
    else:
      return '?'
  else:
    return 'v'

def vstrp(args):
  a = ' '.join(args)
  if a[0] == '"':
    return a
  elif a[0] in letters:
    return a
  elif a[0] in numbers:
    return a
  elif valid(a):
    b = varf(a)
    if b == 'i':
      return a.split(".")[0] + "[" + a.split(".")[1] + "]"
    else:
      pass
      
def linef(args):
  c=0
  b = []
  for i in args:
    c+=1
    a=[]
    for o in range(len(i)):
      if not o > len(i)-2:
        a.append(i[o])
      elif c == len(args):
        a.append(i[o])
    b += ''.join(a)
  return b