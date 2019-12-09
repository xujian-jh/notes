# [3. An Informal Introduction to Python]

- Comments in Python start with the hash character, `#`, and extend to the end of the physical line.
  - A comment may appear at the start of a line or following whitespace or code, but not within a string literal.
  - A hash character within a string literal is just a hash character.
  - Since comments are to clarify code and are not interpreted by Python, they may be omitted when typing in examples.

```s
>>> # this is the first comment
... spam = 1  # and this is the second comment
>>>           # ... and now a third!
... text = "# This is not a comment because it's inside quotes."
>>>
```

## 3.1. Numbers

- The operators `+`, `-`, `*` and `/` work just like in most other languages; parentheses `()` can be used for grouping.
  - Division `/` always returns a float.
  - To do floor division and get an integer result (discarding any fractional result) you can use the `//` operator.
  - To calculate the remainder you can use `%`.
  - To use the `**` operator to calculate powers.
    - Since `**` has higher precedence than `-`, `-3**2` will be interpreted as `-(3**2)` and thus result in -9. To avoid this and get 9, you can use `(-3)**2`.

```s
>>> 50 - 5*6
20
>>> (50 - 5*6) / 4
5.0
>>> 17 / 3  # classic division returns a float
5.666666666666667
>>> 17 // 3  # floor division discards the fractional part
5
>>> 17 % 3  # the % operator returns the remainder of the division
2
>>> 5 * 3 + 2  # result * divisor + remainder
17
>>> 5 ** 2  # 5 squared
25
>>> 2 ** 7  # 2 to the power of 7
128
```

- The equal sign `=` is used to assign a value to a variable.
  - Afterwards, no result is displayed before the next interactive prompt.
  - The equal sign (=) is used to assign a value to a variable. Afterwards, no result is displayed before the next interactive prompt.

```S
>>> width = 20
>>> height = 5 * 9
>>> width * height
900
>>> n  # try to access an undefined variable
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined
```

- In interactive mode, the last printed expression is assigned to the variable `_`.
  - This means that when you are using Python as a desk calculator, it is somewhat easier to continue calculations.

```S
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06
```

## 3.2. Strings

Python strings cannot be changed — they are immutable.

- Be enclosed in single quotes `'...'` or double quotes `"..."` with the same result.
  - The only difference between the two is that within single quotes you don’t need to escape `"` (but you have to escape `\'`) and vice versa.
  - `\` can be used to escape quotes.

```S
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

- The `print()` function produces a more readable output, by omitting the enclosing quotes and by printing escaped and special characters.

```s
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
>>> print('"Isn\'t," they said.')
"Isn't," they said.
>>> s = 'First line.\nSecond line.'  # \n means newline
>>> s  # without print(), \n is included in the output
'First line.\nSecond line.'
>>> print(s)  # with print(), \n produces a new line
First line.
Second line.
```

- If you don’t want characters prefaced by `\` to be interpreted as special characters, you can use raw strings by adding an `r` before the first quote

```s
>>> print('C:\some\name')  # here \n means newline!
C:\some
ame
>>> print(r'C:\some\name')  # note the r before the quote
C:\some\name
```

- String literals can span multiple lines.
  - One way is using triple-quotes: `"""..."""` or `'''...'''`.
  - End of lines are automatically included in the string, but it’s possible to prevent this by adding a `\` at the end of the line.

```S
>>> print("""\
... Usage: thingy [OPTIONS]
...      -h                        Display this usage message
...      -H hostname               Hostname to connect to
... """)
...
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
```

- Strings can be concatenated (glued together) with the `+` operator, and repeated with `*`.
  - Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.
    - This only works with two literals though, not with variables or expressions.

```s
>>> 3 * 'un' + 'ium'
'unununium'
>>> 'Py' 'thon'
'Python'
>>> prefix = 'Py'
>>> prefix 'thon'  # can't concatenate a variable and a string literal
  File "<stdin>", line 1
    prefix 'thon'
                ^
SyntaxError: invalid syntax
>>> ('un' * 3) 'ium'
  File "<stdin>", line 1
    ('un' * 3) 'ium'
                   ^
SyntaxError: invalid syntax
>>> prefix + 'thon'
'Python'
```

- One way to remember how slices work is to think of the indices as pointing between characters.
  - Strings can be indexed (subscripted), with the first character having index 0.
  - Indices may also be negative numbers, to start counting from the right.
    - Note that since -0 is the same as 0, negative indices start from -1.
- In addition to indexing, slicing is also supported.
  - Slice indices have useful defaults; an omitted first index defaults to zero, an omitted second index defaults to the size of the string being sliced.

```s
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
```

```s
>>> word = 'Python'
>>> word[0]  # character in position 0
'P'
>>> word[5]  # character in position 5
'n'
>>> word[-1]  # last character
'n'
>>> word[-2]  # second-last character
'o'
>>> word[-6]
'P'
>>> word[0:2]  # characters from position 0 (included) to 2 (excluded)
'Py'
>>> word[2:5]  # characters from position 2 (included) to 5 (excluded)
'tho'
>>> word[:2]   # character from the beginning to position 2 (excluded)
'Py'
>>> word[4:]   # characters from position 4 (included) to the end
'on'
>>> word[-2:]  # characters from the second-last (included) to the end
'on'
```

## 3.3. Lists

Unlike strings, which are immutable, lists are a mutable type.

```s
>>> cubes = [1, 8, 27, 65, 125]  # something's wrong here
>>> 4 ** 3  # the cube of 4 is 64, not 65!
64
>>> cubes[3] = 64  # replace the wrong value
>>> cubes
[1, 8, 27, 64, 125]
>>> cubes.append(216)  # add the cube of 6
>>> cubes.append(7 ** 3)  # and the cube of 7
>>> cubes
[1, 8, 27, 64, 125, 216, 343]
>>> cubes[2:5] = []
>>> cubes
[1, 8, 216, 343]
>>> cubes[:] = []
>>> cubes
[]
```

It is possible to nest lists (create lists containing other lists).

```s
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

---

[3. An Informal Introduction to Python]:https://docs.python.org/3.7/tutorial/introduction.html
