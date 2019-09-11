# [Command line quick tips: Using pipes to connect tools]

One of the most powerful concepts of Linux is carried on from its predecessor, UNIX. Pipes are key to this concept.

## Standard input and output

- You can think of input flowing freely into a process such as a utility as its standard input (also sometimes called stdin).
- You can think of the free-flowing output of a process as its standard output (also sometimes called stdout).

Often when you run a tool, it outputs to the terminal. Take for instance this simple sequence command using the seq tool:

```s
$ seq 1 6
1
2
3
4
5
6
```

But you could also send it to a file using the `>` character. The shell interpreter uses this character to mean “redirect standard output to a file whose name follows.”

```s
$ seq 1 6 > six.txt
$ cat six.txt
1
2
3
4
5
6
```

You could ask grep to search for a pattern in a file by simply declaring the file name. Technically it’s built to take standard input, and search that.

The shell uses the `<` character similarly to mean “redirect standard input from a file whose name follows.”

```s
$ grep 4 < six.txt
4
```

## Introducing pipes

Now imagine: what if you took the standard output of one tool, and instead of sending it to the terminal, you sent it into another tool’s standard input? This is the essence of the pipe.

Your shell uses the vertical bar character `|` to represent a pipe between two commands.

```s
$ seq 1 6 | grep 4
4
```

---

[Command line quick tips: Using pipes to connect tools]:https://fedoramagazine.org/command-line-quick-tips-using-pipes-to-connect-tools/
