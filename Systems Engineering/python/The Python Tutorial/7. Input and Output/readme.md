# [7. Input and Output]

## 7.1. Fancier Output Formatting

### 7.1.1. Formatted String Literals (also called f-strings for short)

let you include the value of Python expressions inside a string by prefixing the string with `f` or `F` and writing expressions as `{expression}`.

- An optional format specifier can follow the expression.
  - Passing an `integer` after the '`:`' will cause that field to be a minimum number of characters wide.
  - Passing an `float` after the '`:`' will cause that field to be a minimum number of characters wide.
- Other modifiers can be used to convert the value before it is formatted.
  - '`!a`' applies `ascii()`
  - '`!s`' applies `str()`
  - '`!r`' applies `repr()`

```s
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
>>> for name, phone in table.items():
...     print(f'{name:10} ==> {phone:10d}')
...
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678
>>> import math
>>> print(f'The value of pi is approximately {math.pi:.3f}.')
The value of pi is approximately 3.142.
>>> animals = 'eels'
>>> print(f'My hovercraft is full of {animals}.')
My hovercraft is full of eels.
>>> print(f'My hovercraft is full of {animals!r}.')
My hovercraft is full of 'eels'.
```

### 7.1.2. The String `str.format()` Method

- A number in the brackets can be used to refer to the position of the object.
  - Numbers starting from 0 by default.
- If keyword arguments are used in the `str.format()` method, their values are referred to by using the name of the argument.
  - by passing the table as keyword arguments with the ‘`**`’ notation.

```s
>>> print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam
>>> print('{} and {}'.format('spam', 'eggs'))
spam and eggs
>>> print('This {food} is {adjective}.'.format(adjective='absolutely horrible', food='spam'))
This spam is absolutely horrible.
>>> print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
This spam is absolutely horrible.
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

### 7.1.3. Manual String Formatting

- The `str.rjust()` method of string objects right-justifies a string in a field of a given width by padding it with spaces on the left.
- `str.ljust()`.
- `str.center()`.
- There is another method, `str.zfill()`, which pads a numeric string on the left with zeros. It understands about plus and minus signs.

```s
>>> for x in range(1, 11):
...      print(repr(x).ljust(2), repr(x*x).ljust(3), repr(x*x*x).ljust(4))
...
1  1   1
2  4   8
3  9   27
4  16  64
5  25  125
6  36  216
7  49  343
8  64  512
9  81  729
10 100 1000
>>> '12'.zfill(5)
'00012'
>>> '-3.14'.zfill(7)
'-003.14'
>>> '3.14159265359'.zfill(5)
'3.14159265359'
```

## 7.2. Reading and Writing Files

 `open(filename, mode)`

- The first argument is a string containing the filename.
- The second argument is another string containing a few characters describing the way in which the file will be used.
  - '`r`' when the file will only be read.
    - '`r`' will be assumed if it’s omitted.
  - '`w`' for only writing.
  - '`a`' opens the file for appending; any data written to the file is automatically added to the end.
  - '`r+`' opens the file for both reading and writing.
  - Normally, files are opened in text mode.
    - In text mode, the default when reading is to convert platform-specific line endings (`\n` on Unix, `\r\n` on Windows) to just `\n`.
    - '`b`' appended to the mode opens the file in binary mode.
- It is good practice to use the `with` keyword when dealing with file objects.
  - The advantage is that the file is properly closed after its suite finishes, even if an exception is raised at some point.
  - Using `with` is also much shorter than writing equivalent `try-finally` blocks.
- If you’re not using the `with` keyword, then you should call `f.close()` to close the file and immediately free up any system resources used by it.
  - If you don’t explicitly close a file, Python’s garbage collector will eventually destroy the object and close the open file for you, but the file may stay open for a while.

### 7.2.1. Methods of File Objects

---

[7. Input and Output]:https://docs.python.org/3.7/tutorial/inputoutput.html
