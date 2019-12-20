# [8. Errors and Exceptions]

## 8.1. Syntax Errors

Syntax errors, also known as parsing errors.

```s
>>> while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
                   ^
SyntaxError: invalid syntax
```

- File name and line number are printed so you know where to look in case the input came from a script.
  - The parser repeats the offending line and displays a little ‘arrow’ pointing at the earliest point in the line where the error was detected.
- `SyntaxError: invalid syntax`

## 8.2. Exceptions

Even if a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it.

```s
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't convert 'int' object to str implicitly
```

- `Traceback (most recent call last)`
  - File name and line number are printed so you know where to look in case the input came from a script.
- The last line of the error message indicates what happened.
  - Standard exception names are built-in identifiers (not reserved keywords).

## 8.3. Handling Exceptions

```s
>>> while True:
...     try:
...         x = int(input("Please enter a number: "))
...         break
...     except ValueError:
...         print("Oops!  That was no valid number.  Try again...")
...
```

## 8.4. Raising Exceptions

The `raise` statement allows the programmer to force a specified exception to occur.

```s
>>> raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere
```

## 8.5. User-defined Exceptions

- Exceptions should typically be derived from the Exception class, either directly or indirectly.
  - Most exceptions are defined with names that end in “Error”, similar to the naming of the standard exceptions.

```s
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message
```

## 8.6. Defining Clean-up Actions

```s
>>> def divide(x, y):
...     try:
...         result = x / y
...     except ZeroDivisionError:
...         print("division by zero!")
...     else:
...         print("result is", result)
...     finally:
...         print("executing finally clause")
...
>>> divide(2, 1)
result is 2.0
executing finally clause
>>> divide(2, 0)
division by zero!
executing finally clause
>>> divide("2", "1")
executing finally clause
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in divide
TypeError: unsupported operand type(s) for /: 'str' and 'str'
```

- the `finally` clause is executed in any event.
  - In real world applications, the `finally` clause is useful for releasing external resources (such as files or network connections), regardless of whether the use of the resource was successful.
- the `finally` clause will execute as the last task before the `try` statement completes.
  - If an exception occurs which does not match the exception named in the `except` clause, it is passed on to outer `try` statements.

## 8.7. Predefined Clean-up Actions

- The `with` statement allows objects like files to be used in a way that ensures they are always cleaned up promptly and correctly.
  - After the statement is executed, the file f is always closed, even if a problem was encountered while processing the lines.

```s
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```

---

[8. Errors and Exceptions]:https://docs.python.org/3.7/tutorial/errors.html
