# 6. [Modules]

- A module is a file containing Python definitions and statements.
  - The file name is the module name with the suffix `.py` appended.
  - Within a module, the module’s name (as a string) is available as the value of the global variable `__name__`.

For instance, use your favorite text editor to create a file called fibo.py in the current directory with the following contents:

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

Now enter the Python interpreter and import this module with the following command:

```s
>>> import fibo
```

Using the module name you can access the functions:

```s
>>> fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.fib2(100)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> fibo.__name__
'fibo'
```

## 6.1. More on Modules

There is a variant of the import statement that imports names from a module directly into the importing module’s symbol table.

```s
>>> from fibo import fib, fib2
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

- This does not introduce the module name from which the imports are taken in the local symbol table (so in the example, fibo is not defined).

```s
>>> from fibo import *
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

- This imports all names except those beginning with an underscore (_).
  - In most cases Python programmers do not use this facility since it introduces an unknown set of names into the interpreter, possibly hiding some things you have already defined.
  - Note that in general the practice of importing * from a module or package is frowned upon, since it often causes poorly readable code.

If the module name is followed by `as`, then the name following as is bound directly to the imported module.

```s
>>> from fibo import fib as fibonacci
>>> fibonacci(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

Note For efficiency reasons, each module is only imported once per interpreter session. Therefore, if you change your modules, you must restart the interpreter – or, if it’s just one module you want to test interactively, use importlib.reload(), e.g. `import importlib; importlib.reload(modulename)`.

### 6.1.1. Executing modules as scripts

```s
python fibo.py <arguments>
```

That means that by adding this code at the end of your module:

```s
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```

```s
$ python fibo.py 50
0 1 1 2 3 5 8 13 21 34
```

### 6.1.2. The Module Search Path

sys.path is initialized from these locations:

- The directory containing the input script (or the current directory when no file is specified).
- PYTHONPATH (a list of directory names, with the same syntax as the shell variable PATH).
- The installation-dependent default.

### 6.1.3. “Compiled” Python files

To speed up loading modules, Python caches the compiled version of each module in the `__pycache__` directory under the name module.version.pyc, where the version encodes the format of the compiled file; it generally contains the Python version number.

Python checks the modification date of the source against the compiled version to see if it’s out of date and needs to be recompiled. This is a completely automatic process. Also, the compiled modules are platform-independent, so the same library can be shared among systems with different architectures.

## 6.2. Standard Modules

Some modules are built into the interpreter; these provide access to operations that are not part of the core of the language but are nevertheless built in, either for efficiency or to provide access to operating system primitives such as system calls.

- The set of such modules is a configuration option which also depends on the underlying platform.
  - For example, the `winreg` module is only provided on Windows systems.
  - One particular module deserves some attention: `sys`, which is built into every Python interpreter.

The variables `sys.ps1` and `sys.ps2` define the strings used as primary and secondary prompts

```s
>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
>>> sys.ps1 = 'C> '
C> print('Yuck!')
Yuck!
```

The variable `sys.path` is a list of strings that determines the interpreter’s search path for modules. You can modify it using standard list operations:

```s
>>> import sys
>>> sys.path.append('/ufs/guido/lib/python')
```

## 6.3. The dir() Function

The built-in function dir() is used to find out which names a module defines. It returns a sorted list of strings:

```s
>>> import fibo, sys
>>> dir(fibo)
['__name__', 'fib', 'fib2']
>>> dir(sys)  
['__displayhook__', '__doc__', '__excepthook__', '__loader__', '__name__',
 '__package__', '__stderr__', '__stdin__', '__stdout__',
 '_clear_type_cache', '_current_frames', '_debugmallocstats', '_getframe',
 '_home', '_mercurial', '_xoptions', 'abiflags', 'api_version', 'argv',
 'base_exec_prefix', 'base_prefix', 'builtin_module_names', 'byteorder',
 'call_tracing', 'callstats', 'copyright', 'displayhook',
 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix',
 'executable', 'exit', 'flags', 'float_info', 'float_repr_style',
 'getcheckinterval', 'getdefaultencoding', 'getdlopenflags',
 'getfilesystemencoding', 'getobjects', 'getprofile', 'getrecursionlimit',
 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettotalrefcount',
 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info',
 'intern', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path',
 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'ps1',
 'setcheckinterval', 'setdlopenflags', 'setprofile', 'setrecursionlimit',
 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout',
 'thread_info', 'version', 'version_info', 'warnoptions']
```

Without arguments, dir() lists the names you have defined currently:

```s
>>> a = [1, 2, 3, 4, 5]
>>> import fibo
>>> fib = fibo.fib
>>> dir()
['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']
```

## 6.4. Packages

Packages are a way of structuring Python’s module namespace by using “dotted module names”. For example, the module name A.B designates a submodule named B in a package named A. Just like the use of modules saves the authors of different modules from having to worry about each other’s global variable names, the use of dotted module names saves the authors of multi-module packages like NumPy or Pillow from having to worry about each other’s module names.

---

[Modules]:https://docs.python.org/3/tutorial/modules.html
