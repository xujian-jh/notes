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
- End of lines are automatically included in the string, but it’s possible to prevent this by adding a \ at the end of the line.

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

###

---

[Python 3.7.4]:https://docs.python.org/3/

[Install python3]:https://apps.fedoraproject.org/packages/python3
