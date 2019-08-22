# 3.2 [Shell Commands]

## 3.2.1 Simple Commands

- It’s just a sequence of words separated by blanks, terminated by one of the shell’s control operators (see Definitions).
- The first word generally specifies a command to be executed, with the rest of the words being that command’s arguments.
- The return status (see Exit Status) of a simple command  is its exit status as provided by the POSIX 1003.1 waitpid function, or 128+n if the command was terminated by signal n.

## 3.2.2 Pipelines

A pipeline is a sequence of one or more commands separated by one of the control operators ‘|’ or ‘|&’.

```bash
[time [-p]] [!] command1 [ | or |& command2 ] …
```

- The reserved word time causes timing statistics to be printed for the pipeline once it finishes.
  - The statistics currently consist of elapsed (wall-clock) time and user and system time consumed by the command’s execution.
  - The use of time as a reserved word permits the timing of shell builtins, shell functions, and pipelines.
  - An external time command cannot time these easily.
- The -p option changes the output format to that specified by POSIX.
- Each command in a pipeline is executed in its own subshell, which is a separate process (see Command Execution Environment).
  - The output of each command in the pipeline is connected via a pipe to the input of the next command.
  - If ‘|&’ is used, command1’s standard error, in addition to its standard output, is connected to command2’s standard input through the pipe; it is shorthand for 2>&1 |.
- The shell waits for all commands in the pipeline to terminate before returning a value.
  - The exit status of a pipeline is the exit status of the last command in the pipeline, unless the pipefail option is enabled (see The Set Builtin).
  - If pipefail is enabled, the pipeline’s return status is the value of the last (rightmost) command to exit with a non-zero status, or zero if all commands exit successfully.
  - If the reserved word ‘!’ precedes the pipeline, the exit status is the logical negation of the exit status as described above.

## 3.2.3 Lists of Commands

- A list is a sequence of one or more pipelines
  - separated by one of the operators‘&&’ and ‘||’.
    - AND and OR lists have equal precedence.
  - optionally terminated by one of ‘;’, ‘&’, or a newline.
    - If a command is terminated by the control operator ‘&’, the shell executes the command asynchronously in a subshell.

## 3.2.4 Compound Commands

- Compound commands are the shell programming language constructs.
  - Each construct begins with a reserved word or control operator and is terminated by a corresponding reserved word or operator.

### 3.2.4.1 Looping Constructs

- Note that wherever a ‘;’ appears in the description of a command’s syntax, it may be replaced with one or more newlines.
- The break and continue builtins (see Bourne Shell Builtins) may be used to control loop execution.

```bash
until test-commands; do consequent-commands; done
```

- Execute consequent-commands as long as test-commands has an exit status which is not zero. The return status is the exit status of the last command executed in consequent-commands, or zero if none was executed.

```bash
while test-commands; do consequent-commands; done
```

- Execute consequent-commands as long as test-commands has an exit status of zero. The return status is the exit status of the last command executed in consequent-commands, or zero if none was executed.

```bash
for name [ [in [words …] ] ; ] do commands; done
```

- Expand words (see Shell Expansions)

```bash
for (( expr1 ; expr2 ; expr3 )) ; do commands ; done
```

- First, the arithmetic expression is evaluated according to the rules described below (see Shell Arithmetic).

### 3.2.4.2 Conditional Constructs

```bash
if test-commands; then
  consequent-commands;
[elif more-test-commands; then
  more-consequents;]
[else alternate-consequents;]
fi
```

```bash
case word in
    [ [(] pattern [| pattern]…) command-list ;;]…
esac
```

```bash
select name [in words …]; do commands; done
```

### 3.2.4.3 Grouping Commands

```bash
( list )
```

- Placing a list of commands between parentheses causes a subshell environment to be created (see Command Execution Environment), and each of the commands in list to be executed in that subshell.
- Since the list is executed in a subshell, variable assignments do not remain in effect after the subshell completes.

```bash
{ list; }
```

- Placing a list of commands between curly braces causes the list to be executed in the current shell context.
- No subshell is created.
- The semicolon (or newline) following list is required.

## 3.2.5 Coprocesses

- A coprocess is a shell command preceded by the coproc reserved word.
- A coprocess is executed asynchronously in a subshell, as if the command had been terminated with the ‘&’ control operator, with a two-way pipe established between the executing shell and the coprocess.

```bash
coproc [NAME] command [redirections]
```

- This creates a coprocess named NAME.
  - If NAME is not supplied, the default name is COPROC.
- When the coprocess is executed, the shell creates an array variable (see Arrays) named NAME in the context of the executing shell.
  - The standard output of command is connected via a pipe to a file descriptor in the executing shell, and that file descriptor is assigned to NAME[0].
  - The standard input of command is connected via a pipe to a file descriptor in the executing shell, and that file descriptor is assigned to NAME[1].
- The process ID of the shell spawned to execute the coprocess is available as the value of the variable NAME_PID.
  - The wait builtin command may be used to wait for the coprocess to terminate.

## 3.2.6 GNU Parallel

- GNU Parallel, as its name suggests, can be used to build and run commands in parallel.
- You may run the same command with different arguments, whether they are filenames, usernames, hostnames, or lines read from files.
- GNU Parallel provides shorthand references to many of the most common operations (input lines, various portions of the input line, different ways to specify the input source, and so on).
- Parallel can replace xargs or feed commands from its input sources to several different instances of Bash.

```bash
find . -type f -name '*.html' -print | parallel gzip
```

- It is easy to replace xargs to gzip all html files in the current directory and its subdirectories.
- If you need to protect special characters such as newlines in file names, use find’s -print0 option and parallel’s -0 option.

```bash
find . -depth 1 \! -name '.*' -print0 | parallel -0 mv {} destdir
```

- This will run as many mv commands as there are files in the current directory.

```bash
find . -depth 1 \! -name '.*' -print0 | parallel -0 -X mv {} destdir
```

- You can emulate a parallel xargs by adding the -X option

```bash
cat list | parallel "do-something1 {} config-{} ; do-something2 < {}" |
           process-output
```

- GNU Parallel can replace certain common idioms that operate on lines read from a file (in this case, filenames listed one per line)

---

[Shell Commands]:http://www.gnu.org/software/bash/manual/bash.html#Shell-Commands
