# 8. [Errors and Exceptions]

## 8.1. Syntax Errors

also known as parsing errors

```s
>>> while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
                   ^
SyntaxError: invalid syntax
```

- The parser repeats the offending line and displays a little ‘arrow’ pointing at the earliest point in the line where the error was detected.

## 8.2. Exceptions

Errors detected during execution are called exceptions and are not unconditionally fatal: you will soon learn how to handle them in Python programs.

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
Please enter a number: as
Oops!  That was no valid number.  Try again...
Please enter a number: 1
>>>
```

- First, the try clause is executed.
- If no exception occurs, execution of the try statement is finished.
- If an exception occurs during execution of the try clause
  - If its type matches the exception named after the except keyword, the except clause is executed, and then execution continues after the try statement.
  - If an exception occurs which does not match the exception named in the except clause, it is passed on to outer try statements; if no handler is found, it is an unhandled exception and execution stops with a message as shown above.

## 8.4. Raising Exceptions

```s
>>> raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere
```

- The sole argument to raise indicates the exception to be raised.
  - This must be either an exception instance or an exception class (a class that derives from Exception).
    - If an exception class is passed, it will be implicitly instantiated by calling its constructor with no arguments.

```s
raise ValueError  # shorthand for 'raise ValueError()'
```

## 8.5. User-defined Exceptions

Exceptions should typically be derived from the Exception class, either directly or indirectly.

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

- Most exceptions are defined with names that end in “Error”, similar to the naming of the standard exceptions.

## 8.6. Defining Clean-up Actions

In real world applications, the finally clause is useful for releasing external resources (such as files or network connections), regardless of whether the use of the resource was successful.

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

## 8.7. Predefined Clean-up Actions

The with statement allows objects like files to be used in a way that ensures they are always cleaned up promptly and correctly.

```s
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```

---

[Errors and Exceptions]:https://docs.python.org/3/tutorial/errors.html
