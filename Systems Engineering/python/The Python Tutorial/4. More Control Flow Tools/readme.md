# [4. More Control Flow Tools]

## 4.1. `if` Statements

```s
>>> x = int(input("Please enter an integer: "))
Please enter an integer: 42
>>> if x < 0:
...     x = 0
...     print('Negative changed to zero')
... elif x == 0:
...     print('Zero')
... elif x == 1:
...     print('Single')
... else:
...     print('More')
...
More
```

- There can be zero or more `elif` parts, and the `else` part is optional.
- The keyword `elif` is short for `else if`, and is useful to avoid excessive indentation.

## 4.2. `for` Statements

Python’s `for` statement iterates over the items of any sequence (a `list` or a `string`), in the order that they appear in the sequence.

```s
>>> words = ['cat', 'window', 'defenestrate']
>>> for w in words:
...      print(w, len(w))
...
cat 3
window 6
defenestrate 12
```

## 4.3. The `range()` Function

- If you do need to iterate over a sequence of numbers, the built-in function `range()` comes in handy.
  - The range start defaults zero. It is possible to let the range start at another number.
  - The given end point is never part of the generated sequence.
  - The range step defaults one. It is possible to specify a different increment (even negative; sometimes this is called the ‘step’).
  - It is an object which returns the successive items of the desired sequence when you iterate over it, but it doesn’t really make the list, thus saving space.
    - The function `list()` creates lists from iterables.

```s
>>> for i in range(5):
...     print(i)
...
0
1
2
3
4
>>> range(5, 10)
5, 6, 7, 8, 9
>>> range(0, 10, 3)
0, 3, 6, 9
>>> range(-10, -100, -30)
-10, -40, -70
>>> list(range(5))
[0, 1, 2, 3, 4]
```

To iterate over the indices of a sequence, you can combine range() and len() as follows:

```s
>>> a = ['Mary', 'had', 'a', 'little', 'lamb']
>>> for i in range(len(a)):
...     print(i, a[i])
...
0 Mary
1 had
2 a
3 little
4 lamb
```

## 4.4. `break` and `continue` Statements, and `else` Clauses on Loops

- The `break` statement, like in C, breaks out of the innermost enclosing `for` or `while` loop.
  - Loop statements may have an `else` clause; it is executed when the loop terminates through exhaustion of the list (with `for`) or when the condition becomes false (with `while`), but not when the loop is terminated by a `break` statement.
- The continue statement, also borrowed from C, continues with the next iteration of the loop.

```s
>>> for n in range(2, 10):
...     for x in range(2, n):
...         if n % x == 0:
...             print(n, 'equals', x, '*', n//x)
...             break
...     else:
...         # loop fell through without finding a factor
...         print(n, 'is a prime number')
...
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
```

(Look closely: the `else` clause belongs to the `for` loop, not the `if` statement.)

```s
>>> for num in range(2, 10):
...     if num % 2 == 0:
...         print("Found an even number", num)
...         continue
...     print("Found a number", num)
Found an even number 2
Found a number 3
Found an even number 4
Found a number 5
Found an even number 6
Found a number 7
Found an even number 8
Found a number 9
```

## 4.5. `pass` Statements

- The `pass` statement does nothing. It can be used when a statement is required syntactically but the program requires no action.
  - This is commonly used for creating minimal classes.
  - Another place pass can be used is as a place-holder for a function or conditional body when you are working on new code, allowing you to keep thinking at a more abstract level.

```s
>>> class MyEmptyClass:
...     pass
...
```

```s
>>> def initlog(*args):
...     pass   # Remember to implement this!
...
```

## 4.6. Defining Functions

```s
>>> def fib(n):    # write Fibonacci series up to n
...     """Print a Fibonacci series up to n."""
...     a, b = 0, 1
...     while a < n:
...         print(a, end=' ')
...         a, b = b, a+b
...     print()
...
>>> # Now call the function we just defined:
... fib(2000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
```

```s
>>> def fib2(n):  # return Fibonacci series up to n
...     """Return a list containing the Fibonacci series up to n."""
...     result = []
...     a, b = 0, 1
...     while a < n:
...         result.append(a)    # see below
...         a, b = b, a+b
...     return result
...
>>> f100 = fib2(100)    # call it
>>> f100                # write the result
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```

- The keyword `def` introduces a function definition.
  - It must be followed by the function name and the parenthesized list of formal parameters.
- The statements that form the body of the function start at the next line, and must be indented.
  - The execution of a function introduces a new symbol table used for the local variables of the function. More precisely, all variable assignments in a function store the value in the local symbol table; whereas variable references first look in the local symbol table, then in the local symbol tables of enclosing functions, then in the global symbol table, and finally in the table of built-in names. Thus, global variables and variables of enclosing functions cannot be directly assigned a value within a function (unless, for global variables, named in a `global` statement, or, for variables of enclosing functions, named in a `nonlocal` statement), although they may be referenced.

## 4.7. More on Defining Functions

### 4.7.1. Default Argument Values

```s
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
```

- giving only the mandatory argument: `ask_ok('Do you really want to quit?')`
- giving one of the optional arguments: `ask_ok('OK to overwrite the file?', 2)`
- or even giving all arguments: `ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')`

### 4.7.2. Keyword Arguments

Functions can also be called using keyword arguments of the form `kwarg=value`.

### 4.7.3. Arbitrary Argument Lists

- Normally, these variadic arguments will be last in the list of formal parameters, because they scoop up all remaining input arguments that are passed to the function.
  - Any formal parameters which occur after the `*args` parameter are ‘keyword-only’ arguments, meaning that they can only be used as keywords rather than positional arguments.

```s
>>> def concat(*args, sep="/"):
...     return sep.join(args)
...
>>> concat("earth", "mars", "venus")
'earth/mars/venus'
>>> concat("earth", "mars", "venus", sep=".")
'earth.mars.venus'
```

### 4.7.4. Unpacking Argument Lists

If they are not available separately, write the function call with the `*` operator to unpack the arguments out of a list or tuple:

```s
>>> list(range(3, 6))            # normal call with separate arguments
[3, 4, 5]
>>> args = [3, 6]
>>> list(range(*args))            # call with arguments unpacked from a list
[3, 4, 5]
```

In the same fashion, dictionaries can deliver keyword arguments with the ** operator:

```s
>>> def parrot(voltage, state='a stiff', action='voom'):
...     print("-- This parrot wouldn't", action, end=' ')
...     print("if you put", voltage, "volts through it.", end=' ')
...     print("E's", state, "!")
...
>>> d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
>>> parrot(**d)
-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !
```

### 4.7.5. Lambda Expressions

- Small anonymous functions can be created with the `lambda` keyword.
  - Lambda functions can be used wherever function objects are required.
  - They are syntactically restricted to a single expression.
  - Like nested function definitions, lambda functions can reference variables from the containing scope.

```s
>>> def make_incrementor(n):
...     return lambda x: x + n
...
>>> f = make_incrementor(42)
>>> f(0)
42
>>> f(1)
43
```

The above example uses a lambda expression to return a function. Another use is to pass a small function as an argument:

```s
>>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
>>> pairs.sort(key=lambda pair: pair[1])
>>> pairs
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
```

### 4.7.6. Documentation Strings

- The first line should always be a short, concise summary of the object’s purpose.
- If there are more lines in the documentation string, the second line should be blank, visually separating the summary from the rest of the description.
- The first non-blank line after the first line of the string determines the amount of indentation for the entire documentation string (to 8 spaces, normally).

```s
>>> def my_function():
...     """Do nothing, but document it.
...
...     No, really, it doesn't do anything.
...     """
...     pass
...
>>> print(my_function.__doc__)
Do nothing, but document it.

    No, really, it doesn't do anything.
```

### 4.7.7. Function Annotations

Annotations are stored in the `__annotations__` attribute of the function as a dictionary and have no effect on any other part of the function.

```s
>>> def f(ham: str, eggs: str = 'eggs') -> str:
...     print("Annotations:", f.__annotations__)
...     print("Arguments:", ham, eggs)
...     return ham + ' and ' + eggs
...
>>> f('spam')
Annotations: {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
Arguments: spam eggs
'spam and eggs'
```

### 4.8. Intermezzo: Coding Style

- Use 4-space indentation, and no tabs.
  - 4 spaces are a good compromise between small indentation (allows greater nesting depth) and large indentation (easier to read).
  - Tabs introduce confusion, and are best left out.
- Wrap lines so that they don’t exceed 79 characters.
  - This helps users with small displays and makes it possible to have several code files side-by-side on larger displays.
- Use blank lines to separate functions and classes, and larger blocks of code inside functions.
- When possible, put comments on a line of their own.
- Use docstrings.
- Use spaces around operators and after commas, but not directly inside bracketing constructs: `a = f(1, 2) + g(3, 4)`.
- Name your classes and functions consistently;
  - the convention is to use `UpperCamelCase` for classes and `lowercase_with_underscores` for functions and methods.
  - Always use `self` as the name for the first method argument.
- Don’t use fancy encodings if your code is meant to be used in international environments.
  - Python’s default, UTF-8, or even plain ASCII work best in any case.
  - Likewise, don’t use non-ASCII characters in identifiers.

---

[4. More Control Flow Tools]:https://docs.python.org/3.7/tutorial/controlflow.html
