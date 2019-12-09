# [2. Using the Python Interpreter]

## 2.1. Invoking the Interpreter

```s
$ python
Python 3.7.5 (default, Oct 17 2019, 12:16:48)
[GCC 9.2.1 20190827 (Red Hat 9.2.1-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

- Interactive Mode
  - for the next command with the primary prompt, usually three greater-than signs (>>>).
  - for continuation lines it prompts with the secondary prompt, by default three dots (...).
    - Note that a secondary prompt on a line by itself in an example means you must type a blank line; this is used to end a multi-line command.

```s
>>> the_world_is_flat = True
>>> if the_world_is_flat:
...     print("Be careful not to fall off!")
...
Be careful not to fall off!
```

- Typing an end-of-file character (`Control-D` on Unix, `Control-Z` on Windows) at the primary prompt causes the interpreter to exit with a zero exit status.
  - If that doesn’t work, you can exit the interpreter by typing the following command: `quit()`.

## 2.2. The Interpreter and Its Environment

By default, Python source files are treated as encoded in UTF-8.

---

[2. Using the Python Interpreter]:https://docs.python.org/3.7/tutorial/interpreter.html
