# [6. Modules]

- A module is a file containing Python definitions and statements.
  - The file name is the module name with the suffix `.py` appended.
  - Within a module, the module’s name (as a string) is available as the value of the global variable `__name__`.
- Definitions from a module can be imported into other modules or into the main module(the collection of variables that you have access to in a script executed at the top level and in calculator mode).

For instance, use your favorite text editor to create a file called `fibo.py` in the current directory with the following contents:

```s
# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
```

Now enter the Python interpreter:

- `import` the module name.
- Using the module name you can access the functions.

```s
>>> import fibo
>>> fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.fib2(100)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> fibo.__name__
'fibo'
```

## 6.1. More on Modules

- If the module name is followed by `as`, then the name following `as` is bound directly to the imported module.
  - This is effectively importing the module in the same way that `import fibo` will do, with the only difference of it being available `as fib`.

```s
>>> import fibo as fib
>>> fib.fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

- There is a variant of the `import` statement:
  - that imports names from a module directly into the importing module’s symbol table.
  - all names that a module defines by `import *`.
    - This imports all names except those beginning with an underscore (_).

```s
>>> from fibo import fib, fib2
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

```s
>>> from fibo import *
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

This is effectively importing the module in the same way that import fibo will do, with the only difference of it being available as fib.

It can also be used when utilising from with similar effects:

```s
>>> from fibo import fib as fibonacci
>>> fibonacci(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

- For efficiency reasons, each module is only imported once per interpreter session.
  - if you change your modules, you must restart the interpreter.
  - if it’s just one module you want to test interactively, use `import importlib` or `importlib.reload(modulename)`.

### 6.1.3. “Compiled” Python files

To speed up loading modules, Python caches the compiled version of each module in the `__pycache__` directory under the name `module.version.pyc`, where the version encodes the format of the compiled file; it generally contains the Python version number.

## 6.2. Standard Modules

- One particular module deserves some attention: `sys`, which is built into every Python interpreter.
  - The variables `sys.ps1` and `sys.ps2` define the strings used as primary and secondary prompts.
  - The variable `sys.path` is a list of strings that determines the interpreter’s search path for modules.
    - It is initialized to a default path taken from the environment variable PYTHONPATH, or from a built-in default if PYTHONPATH is not set.
    - You can modify it using standard list operations.
- the `winreg` module is only provided on Windows systems.

```s
>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
>>> sys.ps1 = 'C> '
C> print('Yuck!')
Yuck!
C>
```

```s
>>> import sys
>>> sys.path.append('/ufs/guido/lib/python')
```

## 6.3. The `dir()` Function

The built-in function `dir()` is used to find out which names a module defines. It returns a sorted list of strings.

```s
>>> import fibo
>>> dir(fibo)
['__name__', 'fib', 'fib2']
```

Without arguments, `dir()` lists the names you have defined currently.

- Note that it lists all types of names: variables, modules, functions, etc.
- `dir()` does not list the names of built-in functions and variables.
  - If you want a list of those, they are defined in the standard module `builtins`.

```s
>>> a = [1, 2, 3, 4, 5]
>>> import fibo
>>> fib = fibo.fib
>>> dir()
['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']
```

```s
>>> import builtins
>>> dir(builtins)  
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning',
 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning',
 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False',
 'FileExistsError', 'FileNotFoundError', 'FloatingPointError',
 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError',
 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError',
 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError',
 'MemoryError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented',
 'NotImplementedError', 'OSError', 'OverflowError',
 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError',
 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning',
 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError',
 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError',
 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError',
 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning',
 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__build_class__',
 '__debug__', '__doc__', '__import__', '__name__', '__package__', 'abs',
 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable',
 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits',
 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit',
 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr',
 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass',
 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview',
 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property',
 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice',
 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars',
 'zip']
```

## 6.4. Packages

- Packages are a way of structuring Python’s module namespace by using “dotted module names”.
  - Here’s a possible structure for your package (expressed in terms of a hierarchical filesystem).

```s
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```

### 6.4.2. Intra-package References

These imports use leading dots to indicate the current (`.`) and parent (`..`) packages involved in the relative import.

```s
from . import echo
from .. import formats
from ..filters import equalizer
```

- Note that relative imports are based on the name of the current module.
- Since the name of the main module is always `__main__`, modules intended for use as the main module of a Python application must always use absolute imports.

---

[6. Modules]:https://docs.python.org/3.7/tutorial/modules.html
