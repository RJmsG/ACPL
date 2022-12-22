from compile import *
import os, subprocess
from platform import system

files_c, file, cls = [], "", 0 #set to 1 for clear screen
command = ["gcc", "-std=c17", "-Wall"]

lib = ['<stdio.h>', '<stdlib.h>', '<string.h>']

def compilef(file, path='', extra_libs=[], mtype='int', libs=lib, savefile=True, execute=False): # NOTE: execute is a work-in-progress. It does not work as of now.
  global output
  libs += extra_libs
  print(f'Compiling "{file}.acpl"...')
  f1 = open((file + '.acpl'), 'r')
  lines = f1.readlines()
  for i in libs:
    output.append('#include' + i)
  output.append(f'{mtype} main() '+'{')
  output.append('int ac = 1;')
  c = 0
  for i in lines:
    c += 1
    a = []
    for o in range(len(i)):
      if not o > (len(i) - 2):
        a.append(i[o])
      elif c == len(lines):
        a.append(i[o])
    i = ''.join(a)
    comln(i)
  if not mtype == 'void':
    output.append('return 0;')
  output.append('}')
  output += aput
  print('Finished generating code!')
  print('Creating new file in chosen directory...')
  if savefile:
    with open(f'{path}{file}.c', 'x') as f2:
      for i in output:
        f2.write("%s\n" % i)
    f2.close()
  try:
        subprocess.run([*command, "-o", file[:-2], file + '.c'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True)
  except subprocess.CalledProcessError as suberror:
        print(suberror.stdout.decode("utf-8"))
  print('DONE!')
  if execute:
     exit_code = subprocess.run(file[:-2]).returncode
     print(f"\n-----------------------------------\nProcess terminated with exit code {exit_code}") 