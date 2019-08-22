# 3.1 [Shell Syntax]

When the shell reads input, it proceeds through a sequence of operations.

1. If the input indicates the beginning of a comment, the shell ignores the comment symbol (‘#’), and the rest of that line.
2. The shell reads its input and divides the input into words and operators, employing the quoting rules to select which meanings to assign various words and characters.
3. The shell then parses these tokens into commands and other constructs, removes the special meaning of certain words or characters, expands others, redirects input and output as needed, executes the specified command, waits for the command’s exit status, and makes that exit status available for further inspection or processing.

## 3.1.1 Shell Operation

The following is a brief description of the shell’s operation when it reads and executes a command.

1. Reads its input from a file (see Shell Scripts), from a string supplied as an argument to the -c invocation option (see Invoking Bash), or from the user’s terminal.
2. Breaks the input into words and operators, obeying the quoting rules described in Quoting. These tokens are separated by metacharacters. Alias expansion is performed by this step (see Aliases).
3. Parses the tokens into simple and compound commands (see Shell Commands).
4. Performs the various shell expansions (see Shell Expansions), breaking the expanded tokens into lists of filenames (see Filename Expansion) and commands and arguments.
5. Performs any necessary redirections (see Redirections) and removes the redirection operators and their operands from the argument list.
6. Executes the command (see Executing Commands).
7. Optionally waits for the command to complete and collects its exit status (see Exit Status).

## 3.1.2 Quoting

- Escape Character: How to remove the special meaning from a single character.
  - A non-quoted backslash ‘\’ is the Bash escape character.
  - It preserves the literal value of the next character that follows, with the exception of newline.
  - If a \newline pair appears, and the backslash itself is not quoted, the \newline is treated as a line continuation (that is, it is removed from the input stream and effectively ignored).
- Single Quotes: How to inhibit all interpretation of a sequence of characters.
  - Enclosing characters in single quotes preserves the literal value of each character within the quotes.
  - A single quote may not occur between single quotes, even when preceded by a backslash.
- Double Quotes: How to suppress most of the interpretation of a sequence of characters.
  - Enclosing characters in double quotes (‘"’) preserves the literal value of all characters within the quotes, with the exception of ‘$’, ‘`’, ‘\’, and, when history expansion is enabled, ‘!’.
  - A double quote may be quoted within double quotes by preceding it with a backslash.
  - The backslash retains its special meaning only when followed by one of the following characters: ‘$’, ‘`’, ‘"’, ‘\’, or newline. Within double quotes, backslashes that are followed by one of these characters are removed. Backslashes preceding characters without a special meaning are left unmodified.
  - The special parameters ‘*’ and ‘@’ have special meaning when in double quotes (see Shell Parameter Expansion).
- ANSI-C Quoting: How to expand ANSI-C sequences in quoted strings.
  - \a
alert (bell)
  - \b
backspace
  - \e
  - \E
an escape character (not ANSI C)
  - \f
form feed
  - \n
newline
  - \r
carriage return
  - \t
horizontal tab
  - \v
vertical tab
  - \\
backslash
  - \'
single quote
  - \"
double quote
  - \?
question mark
  - \nnn
the eight-bit character whose value is the octal value nnn (one to three octal digits)
  - \xHH
the eight-bit character whose value is the hexadecimal value HH (one or two hex digits)
  - \uHHHH
the Unicode (ISO/IEC 10646) character whose value is the hexadecimal value HHHH (one to four hex digits)
  - \UHHHHHHHH
the Unicode (ISO/IEC 10646) character whose value is the hexadecimal value HHHHHHHH (one to eight hex digits)
  - \cx
a control-x character
- Locale Translation: How to translate strings into different languages.
  - A double-quoted string preceded by a dollar sign (‘$’) will cause the string to be translated according to the current locale.
  - If the current locale is C or POSIX, the dollar sign is ignored. If the string is translated and replaced, the replacement is double-quoted.

Each of the shell metacharacters (see Definitions) has special meaning to the shell and must be quoted if it is to represent itself.

## 3.1.3 Comments

In a non-interactive shell, or an interactive shell in which the interactive_comments option to the shopt builtin is enabled (see The Shopt Builtin), a word beginning with ‘#’ causes that word and all remaining characters on that line to be ignored.

---

[Shell Syntax]:http://www.gnu.org/software/bash/manual/bash.html#Shell-Syntax
