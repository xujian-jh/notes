# [Python 3.7.4]

## 1. [Install python3]

```bash
dnf install python3
```

## 2. Using the Python Interpreter

Since the best way to learn a language is to use it, the tutorial invites you to play with the Python interpreter as you read.

### 2.1 Invoking the Interpreter

The Python interpreter is usually installed as /usr/local/bin/python3.7 on those machines where it is available; putting /usr/local/bin in your Unix shell’s search path makes it possible to start it by typing the command:

```bash
python3.7
```

- Interactive Mode
  - for the next command it prompts with the primary prompt, usually three greater-than signs (>>>)
  - for continuation lines it prompts with the secondary prompt, by default three dots (...)
    - type a blank line; this is used to end a multi-line command.
  - Comments in Python start with the hash character, #, and extend to the end of the physical line.
    - A comment may appear at the start of a line or following whitespace or code, but not within a string literal. A hash character within a string literal is just a hash character. Since comments are to clarify code and are not interpreted by Python, they may be omitted when typing in examples.

### 2.2 Exit the interpreter

If that doesn’t work, you can exit the interpreter by typing the following command:

```bash
quit()
```

## 3. Introduction to Python

### 3.1 Numbers

Expression syntax is straightforward: the operators `+`, `-`, `*`and `/` work just like in most other languages (for example, Pascal or C); parentheses (()) can be used for grouping.

```bash
>>> 2 + 2
4
>>> 50 - 5*6
20
>>> (50 - 5*6) / 4
5.0
>>> 8 / 5  # division always returns a floating point number
1.6
```

Division (/) always returns a float. To do floor division and get an integer result (discarding any fractional result) you can use the `//` operator; to calculate the remainder you can use `%`

```bash
>>> 17 / 3  # classic division returns a float
5.666666666666667
>>>
>>> 17 // 3  # floor division discards the fractional part
5
>>> 17 % 3  # the % operator returns the remainder of the division
2
```

With Python, it is possible to use the `**` operator to calculate powers

```bash
>>>
>>> 5 ** 2  # 5 squared
25
>>> 2 ** 7  # 2 to the power of 7
128
```

The equal sign (=) is used to assign a value to a variable. In interactive mode, the last printed expression is assigned to the variable `_`.

```bash
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06
```

### 3.2 Strings

They can be enclosed in single quotes ('...') or double quotes ("...") with the same result. `\` can be used to escape quotes.

```bash
>>> 'spam eggs'  # single quotes
'spam eggs'
>>> 'doesn\'t'  # use \' to escape the single quote...
"doesn't"
>>> "doesn't"  # ...or use double quotes instead
"doesn't"
>>> '"Yes," they said.'
'"Yes," they said.'
>>> "\"Yes,\" they said."
'"Yes," they said.'
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
```

If you don’t want characters prefaced by `\` to be interpreted as special characters, you can use raw strings by adding an `r` before the first quote

```bash
>>> print('C:\some\name')  # here \n means newline!
C:\some
ame
>>> print(r'C:\some\name')  # note the r before the quote
C:\some\name
```

String literals can span multiple lines.

- One way is using triple-quotes: """...""" or '''...'''.
- End of lines are automatically included in the string, but it’s possible to prevent this by adding a `\` at the end of the line.

```bash
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
```

Strings can be concatenated (glued together) with the `+` operator, and repeated with `*`

```bash
>>> 3 * 'un' + 'ium'
'unununium'
```

Strings can be indexed (subscripted), with the first character having index 0.

```bash
>>> word = 'Python'
>>> word[0]  # character in position 0
'P'
>>> word[5]  # character in position 5
'n'
```

Indices may also be negative numbers, to start counting from the right:

```bash
>>> word[-1]  # last character
'n'
>>> word[-2]  # second-last character
'o'
>>> word[-6]
'P'
```

```bash
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
```

While indexing is used to obtain individual characters, slicing allows you to obtain substring

```bash
>>> word[0:2]  # characters from position 0 (included) to 2 (excluded)
'Py'
>>> word[2:5]  # characters from position 2 (included) to 5 (excluded)
'tho'
```

This makes sure that `s[:i] + s[i:]` is always equal to `s`

- an omitted first index defaults to zero,
- an omitted second index defaults to the size of the string being sliced

```bash
>>> word[:2] + word[2:]
'Python'
>>> word[:4] + word[4:]
'Python'
```

Python strings cannot be changed — they are `immutable`. Therefore, assigning to an indexed position in the string results in an error.

### 3.3 Lists

- lists can be indexed and sliced
- lists are a `mutable` type

```bash
>>> cubes = [1, 8, 27, 65, 125]  # something's wrong here
>>> 4 ** 3  # the cube of 4 is 64, not 65!
64
>>> cubes[3] = 64  # replace the wrong value
>>> cubes
[1, 8, 27, 64, 125]
```

- You can also add new items at the end of the list, by using the `append()` method

```bash
>>> cubes.append(216)  # add the cube of 6
>>> cubes.append(7 ** 3)  # and the cube of 7
>>> cubes
[1, 8, 27, 64, 125, 216, 343]
```

- Assignment to slices is also possible, and this can even change the size of the list or clear it entirely

```bash
>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> # replace some values
>>> letters[2:5] = ['C', 'D', 'E']
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> # now remove them
>>> letters[2:5] = []
>>> letters
['a', 'b', 'f', 'g']
>>> # clear the list by replacing all the elements with an empty list
>>> letters[:] = []
>>> letters
[]
```

- It is possible to nest lists (create lists containing other lists)

```bash
>>> a = ['a', 'b', 'c']
>>> n = [1, 2, 3]
>>> x = [a, n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'
```

## 4. More Control Flow Tools

### 4.1. if Statements

```bash
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

- There can be zero or more elif parts, and the else part is optional.
  - The keyword ‘elif’ is short for ‘else if’, and is useful to avoid excessive indentation.

### 4.2. for Statements

```bash
>>> # Measure some strings:
... words = ['cat', 'window', 'defenestrate']
>>> for w in words:
...     print(w, len(w))
...
cat 3
window 6
defenestrate 12
```

If you need to modify the sequence you are iterating over while inside the loop (for example to duplicate selected items), it is recommended that you first make a copy.

```bash
>>> for w in words[:]:  # Loop over a slice copy of the entire list.
...     if len(w) > 6:
...         words.insert(0, w)
...
>>> words
['defenestrate', 'cat', 'window', 'defenestrate']
```

### 4.3. The built-in function `range()`

In many ways the object returned by range() behaves as if it is a list, but in fact it isn’t. It is an object which returns the successive items of the desired sequence when you iterate over it, but it doesn’t really make the list, thus saving space.

```bash
>>> for i in range(5):
...     print(i)
...
0
1
2
3
4
```

The given end point is never part of the generated sequence

```bash
range(5, 10)
   5, 6, 7, 8, 9

range(0, 10, 3)
   0, 3, 6, 9

range(-10, -100, -30)
  -10, -40, -70
```

To iterate over the indices of a sequence, you can combine range() and len() as follows:

```bash
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

### 4.4. Loop statements

The `break` statement, like in C, breaks out of the innermost enclosing `for` or `while` loop.

Loop statements may have an `else`
clause; it is executed when the loop terminates through exhaustion of the list (with `for`) or when the condition becomes false (with `while`)

```bash
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

- Look closely: the else clause belongs to the for loop, not the if statement.

The `continue` statement, also borrowed from C, continues with the next iteration of the loop

```bash
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

### 4.5. `pass` Statements

It can be used when a statement is required syntactically but the program requires no action.

### 4.6. The keyword `def` introduces a function definition

```bash
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

It is simple to write a function that returns a list of the numbers of the Fibonacci series, instead of printing it

```bash
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

### 4.7. More on Defining Functions

#### 4.7.1. Default Argument Values

```bash
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

- giving only the mandatory argument: ask_ok('Do you really want to quit?')
- giving one of the optional arguments: ask_ok('OK to overwrite the file?', 2)
- giving all arguments: ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

#### 4.7.2. Keyword Arguments

ask_ok(reminder='Come on, only yes or no!', prompt='OK to overwrite the file?',  retries=2)

- All the keyword arguments passed must match one of the arguments accepted by the function, and their order is not important.

#### 4.7.3. Arbitrary Argument Lists

```bash
>>> def concat(*args, sep="/"):
...     return sep.join(args)
...
>>> concat("earth", "mars", "venus")
'earth/mars/venus'
>>> concat("earth", "mars", "venus", sep=".")
'earth.mars.venus'
```

- Before the variable number of arguments, zero or more normal arguments may occur.
- Normally, these variadic arguments will be last in the list of formal parameters, because they scoop up all remaining input arguments that are passed to the function.
- Any formal parameters which occur after the *args parameter are ‘keyword-only’ arguments, meaning that they can only be used as keywords rather than positional arguments.

#### 4.7.4. Unpacking Argument Lists

If they are not available separately, write the function call with the `*` operator to unpack the arguments out of a list or tuple:

```bash
>>> list(range(3, 9))            # normal call with separate arguments
[3, 4, 5, 6, 7, 8]
>>> args = [3, 9]
>>> list(range(*args))            # call with arguments unpacked from a list
[3, 4, 5, 6, 7, 8]
```

In the same fashion, dictionaries can deliver keyword arguments with the `**` operator:

```bash
>>> def parrot(voltage, state='a stiff', action='voom'):
...     print("-- This parrot wouldn't", action, end=' ')
...     print("if you put", voltage, "volts through it.", end=' ')
...     print("E's", state, "!")
...
>>> d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
>>> parrot(**d)
-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !
```

#### 4.7.5. Lambda Expressions

Small anonymous functions can be created with the lambda keyword.

```bash
>>> def make_incrementor(n):
...     return lambda x: x + n
...
>>> f = make_incrementor(42)
>>> f(0)
42
>>> f(1)
43
```

Another use is to pass a small function as an argument:

```bash
>>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
>>> pairs.sort(key=lambda pair: pair[1])     # 依据第二个参数排序
>>> pairs
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
```

#### 4.7.6. Documentation Strings

- The first line should always be a short, concise summary of the object’s purpose.
  - For brevity, it should not explicitly state the object’s name or type
  - his line should begin with a capital letter and end with a period.
- If there are more lines in the documentation string, the second line should be blank, visually separating the summary from the rest of the description.
  - The Python parser does not strip indentation from multi-line string literals in Python, so tools that process documentation have to strip indentation if desired.

```bash
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

#### 4.7.7. Function Annotations

Annotations are stored in the `__annotations__` attribute of the function as a dictionary and have no effect on any other part of the function.

```bash
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

#### 4.8. Intermezzo: Coding Style

- Use 4-space indentation, and no tabs.
- Wrap lines so that they don’t exceed 79 characters.
- Use blank lines to separate functions and classes, and larger blocks of code inside functions.
- When possible, put comments on a line of their own.
- Use docstrings.
- Use spaces around operators and after commas, but not directly inside bracketing constructs: a = f(1, 2) + g(3, 4).
- Name your classes and functions consistently; the convention is to use UpperCamelCase for classes and lowercase_with_underscores for functions and methods.
- Python’s default, UTF-8, or even plain ASCII work best in any case.

---

[Python 3.7.4]:https://docs.python.org/3/

[Install python3]:https://apps.fedoraproject.org/packages/python3
