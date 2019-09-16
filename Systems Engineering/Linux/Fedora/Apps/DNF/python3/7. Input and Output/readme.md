# 7. [Input and Output]

## 7.1. Fancier Output Formatting

### 7.1.1. Formatted String Literals (also called f-strings for short)

An optional format specifier can follow the expression. This allows greater control over how the value is formatted.

```s
>>> import math
>>> print(f'The value of pi is approximately {math.pi:.3f}.')
The value of pi is approximately 3.142.
```

- The example rounds pi to three places after the decimal.

```s
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
>>> for name, phone in table.items():
...     print(f'{name:10} ==> {phone:10d}')
...
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678
```

- Passing an integer after the ':' will cause that field to be a minimum number of characters wide. This is useful for making columns line up.

```s
>>> animals = 'eels'
>>> print(f'My hovercraft is full of {animals}.')
My hovercraft is full of eels.
>>> print(f'My hovercraft is full of {animals!a}.')
My hovercraft is full of 'eels'.
>>> print(f'My hovercraft is full of {animals!s}.')
My hovercraft is full of eels.
>>> print(f'My hovercraft is full of {animals!r}.')
My hovercraft is full of 'eels'.
```

- Other modifiers can be used to convert the value before it is formatted.
  - `!a` applies ascii()
  - `!s` applies str()
  - `!r` applies repr()

### 7.1.2. The String format() Method

```s
>>> print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs
>>> print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam
```

- The brackets and characters within them (called format fields) are replaced with the objects passed into the str.format() method.
- A number in the brackets can be used to refer to the position of the object passed into the str.format() method.

```s
>>> print('This {food} is {adjective}.'.format(
...       food='spam', adjective='absolutely horrible'))
This spam is absolutely horrible.
```

- If keyword arguments are used in the str.format() method, their values are referred to by using the name of the argument.

```s
>>> print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                       other='Georg'))
The story of Bill, Manfred, and Georg.
```

- Positional and keyword arguments can be arbitrarily combined.

```s
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

- This could be done by passing the table as keyword arguments with the `**` notation.

```s
>>> for x in range(1, 11):
...     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```

- This is particularly useful in combination with the built-in function vars()

### 7.1.3. Manual String Formatting

```s
>>> for x in range(1, 11):
...     print(repr(x).rjust(2), repr(x*x).rjust(3), repr(x*x*x).rjust(4))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```

- The `str.rjust()` method of string objects right-justifies a string in a field of a given width by padding it with spaces on the left.
- There are similar methods `str.ljust()` and `str.center()`.
  - If you really want truncation you can always add a slice operation, as in `x.ljust(n)[:n]`.
- There is another method, str.zfill(), which pads a numeric string on the left with zeros. It understands about plus and minus signs.

```s
>>> '12'.zfill(5)
'00012'
>>> '-3.14'.zfill(7)
'-003.14'
>>> '3.14159265359'.zfill(5)
'3.14159265359'
```

## 7.2. Reading and Writing Files

```s
 open(filename, mode)
```

- The mode argument is optional
  - mode can be 'r' when the file will only be read
    - 'r' will be assumed if it’s omitted.
  - 'w' for only writing (an existing file with the same name will be erased)
  - 'a' opens the file for appending
    - any data written to the file is automatically added to the end
  - 'r+' opens the file for both reading and writing

- Normally, files are opened in text mode, that means, you read and write strings from and to the file, which are encoded in a specific encoding.
  - If encoding is not specified, the default is platform dependent.
    - the default when reading is to convert platform-specific line endings (\n on Unix, \r\n on Windows) to just \n.
  - 'b' appended to the mode opens the file in binary mode

```s
>>> with open('workfile') as f:
...     read_data = f.read()
>>> f.closed
True
```

- It is good practice to use the with keyword when dealing with file objects.
  - The advantage is that the file is properly closed after its suite finishes, even if an exception is raised at some point.
- Using with is also much shorter than writing equivalent try-finally blocks.
- If you’re not using the with keyword, then you should call f.close() to close the file and immediately free up any system resources used by it.

### 7.2.1. Methods of File Objects

#### f.read(size)

- size is an optional numeric argument.
  - When size is omitted or negative, the entire contents of the file will be read and returned; it’s your problem if the file is twice as large as your machine’s memory. Otherwise, at most size characters (in text mode) or size bytes (in binary mode) are read and returned.
- If the end of the file has been reached, f.read() will return an empty string ('').

#### f.readline()

- reads a single line from the file; a newline character (\n) is left at the end of the string, and is only omitted on the last line of the file if the file doesn’t end in a newline.
- if f.readline() returns an empty string, the end of the file has been reached, while a blank line is represented by '\n', a string containing only a single newline.

For reading lines from a file, you can loop over the file object. This is memory efficient, fast, and leads to simple code:

```s
>>> for line in f:
...     print(line, end='')
...
This is the first line of the file.
Second line of the file
```

#### list(f) or f.readlines()

- If you want to read all the lines of a file in a list

#### f.write(string)

```s
>>> f.write('This is a test\n')
15
```

- writes the contents of string to the file, returning the number of characters written.

### 7.2.2. Saving structured data with json

Python allows you to use the popular data interchange format called JSON (JavaScript Object Notation).

---

[Input and Output]:https://docs.python.org/3/tutorial/inputoutput.html
