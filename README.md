# ACPL

ACPL is a new lanugae I've been working on.
It's a compiled language that is designed to be fast but also easy to use.

### What does "ACPL" stand for?
ACPL, Ironically, stands for Axe's Complicated Programming Language.
I was gonna call it ASPL, but the name stuck.

## More information
ACPL's latest version is 1.2, it is mainained by Me(RJmsG).

### Whats new in 1.2?
A few small changes have been added:

1) Embedded GCC
2) Default option to download the generated C code

### Goals for ACPL:

1) support for dynamic arrays
2) full port to the C language
3) switch to llvm
4) Support for C & Python based libraries

### How do I use it?

To get started using the compiler, first make sure you have a file to compile.
Here's an example:

```
#compilewhatever.py
import main
main.compilef('helloworld.acpl')
```
These are all the args and their purposes:

```
compilef(file (tells name of file), path (file's location), extra_libs (include extra libraries from the c dynamic library), mtype (set the data typoe for the main() function), libs (set the full list of libs to whatever you want), savefile=True (option to save the output as a .c file), execute=False (option to execute the compiled gcc output(doesn't work)))
```
All of them but "file" are optional.


#### I am currently looking for other's help to make ACPL better
If you can, join the project and spread the word!
