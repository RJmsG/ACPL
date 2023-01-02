from . import compilemod as cmod
from .compilemod import *
from .lex import *

def comln(inp):
    args = tokenize(inp)
    i = args[0]
    del args[0]
    if i == 'vlen':
        tp = args[0]
        name = args[1]
        args = clargs(3,args)
        var.append(name)
        tpe.append(tp)
        varset(tp, name, bstrp(args))
        args = []
    elif i in dt:
        tp=args[0]
        name=args[1]
        args=clargs(2,args)
        var.append(name)
        tpe.append('~'+tp)
        dynvarset(tp,name,bstrp(args))
        args=[]