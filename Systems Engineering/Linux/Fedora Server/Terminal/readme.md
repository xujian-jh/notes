# [Terminal]

The shell, also known as the “command line interface” or “CLI”“, is the primary method for interacting with remote Linux servers.

Depending on your system’s configuration, the prompt will end with either a dollar sign ($) for regular users and a hash (#) for root. We’re now ready to begin this guide.

Most shell commands follow a similar format. They begin with the name of the command (which we can think of as a verb), then have an optional series of modifiers or flags that specific particular functions (adjectives,) and (if necessary) have some sort of object that the command is to affect.

If you need help figuring out how a command works, generally sending the command with a `--help` flag will provide information on how to use the command.

## File System Navigation

### Use `pwd` to print the working directory

```s
pwd
```

### Use `cd` to navigate directory

- the `~` indicates your home directory
- the `.` (Default) indicates the working or current directory
- the `..` indicates the parent directory

### Use `ls` to list directories

```s
ls -lha
```

- To list all of the files in the current directory, including hidden files (such as those beginning with a `.`) use the `-a` flag for all files.
- To generate a list with more information about the files, the long flag, `-l` may be used.
- You may further modify the long output with an `-h` flag to convert the file size information from raw bytes to human-readable numbers (in KB, MB, GB, etc) for easier comprehension.

### To create a new empty directory, use the make directory command `mkdir`

```s
mkdir ~/website/
mkdir -p ~/website/litchfield/public_www/
```

- Use the `-p` flag to make parent directories as needed

### To remove directories, use the `rmdir` command

- Be aware that this only works if the directory specified is empty.
  - If you want to remove a directory that is non-empty use the `rm -r` command.

### To remove files use the `rm` command

Note that the `rm` command is permanent and cannot be undone.

### Use the `touch` command

- If you want to create a file without writing any content to it you can use the `touch` command.
- You can also safely use `touch` on existing files, which resets the “last edited” value of touched files to the time when the command was issued.

### To copy files use the `cp` command

```s
cp /etc/hosts ~/etc.hosts.backup
cp -R ~/website-files/* ~/website-backups/
```

- Followed by the original file and the location where you want to copy the file to.
- If you need to copy contents of a directory into another directory, you need to use the `-R` flag (case sensitive; for recursive)

### The `mv` command handles all moving and renaming operations on files and directories

```s
mv ~/etc.hosts.backup ~/backup/etc.hosts
```

Its syntax is the same as `cp` (though directory moves are recursive by nature).

## Text Manipulation

Linux, like all UNIX-derived systems uses text files to manage configuration and content.

### Nano Text Editor

If you just need a basic text editor, try the `nano` editor, which comes installed by default on nearly every Linux distribution.

### Redirecting Streams

The shell lets us direct the output from one command to another until we have output that is useful to us.

```s
ls /usr/bin/ | grep ^py.* > ~/python-bins.txt
```

1. Generates a list of the files in `/usr/bin/` (with the `ls /usr/bin/` command.)
2. Sends the output of `ls` to the `grep` command (with the pipe operator, which is `|`.)
3. Searches the output of `ls` with `grep`, which looks for all files that begin with the letters `py` (a common prefix for programs written in the Python programming language.)
4. Sends the output of `grep` to a file located in the current user’s home directory (~/) named python-bins.txt (with the `>` operator.)

- If the file specified at the end of the `>` operator has contents, `>` will overwrite that content.
- To append the output of a command to the end of an existing file use the append operator, which is `>>`.
  - The `echo` command is useful for repeating stated contents directly. This doesn’t see much use as a simple command, but is useful in scripts and when combined with streams.

```s
echo "I received a call on `date`" >> phone-log.txt
```

This will append `I received a call on Fri Jan 22 12:04:23 EST 2010` to the end of the `phone-log.txt` file. `date` will output the current date and time, and the output format of this command is controlled by the system’s locale settings.

### Viewing Text in a Pager

- There’s also a `cat` command that reads the content of a file onto standard output line for line.
  - It may also be used to send the contents of a file to a command that doesn’t provide an option to read directly from files.
- Additionally, the command `tac` sends the contents of a file to standard output (your screen by default) in reverse.
- The most common pagers are `more` and `less`.

## System Monitoring

- The command `ps` lists active processes by Process ID (PID) numbers.
  - You can use the `ps -A` command to list all currently running processes, including inactive processes.
- The `top` command, which is installed by default on all systems, provides a regularly refreshed list of processes and resource utilization information.
- The `df` command, which is native to all systems, provides a metric of your current disk usage including free and unused space.
  - You can use the `df -h` command to list your current space in megabytes and gigabytes, which is easier to read than flat kilobytes.
  - You can also use the command `df -i` to view the number of iNodes your disk has used and remain available. An iNode is how the filesystem keeps track of files, and is directly related to the number of files that can be created.
- The `du` command, also native to all systems, checks which directories are using the most space.
  - use the command `du -h --max-depth 1 /`,  allows you to specify how many directories deep the command should iterate through.

## The shell environment that is common on most contemporary UNIX systems: `bash`

### Tab CompletionPermalink

By default, `bash` provides `tab` completion for commands and executables in your PATH as well as for files and directories.

### GNU Screen

This program may not be installed by default. It is a “terminal multiplexer”.

```s
dnf install screen
```

- Start it with the command `screen` and after hitting return to dismiss the splash screen you will be brought to a terminal inside of screen.
- Screen terminals are assigned a number on creation.
  - `screen 0: root@localhost:~`
- You can use `Control-a Control-c` to create new terminal sessions running inside of screen.
  - The same effect with the command `screen`
  - `screen 1: root@localhost:~`
- You can use `Control-a Control-a` to toggle between your current screen session and your last visited screen session.

- You may reconnect to the screen session with `screen -r`.
  - If you’re running more than one screen session, you can use `screen -ls` to generate a list of the current screen sessions.
  - If you want to connect to an already connected screen session, use the `screen -x` command which is useful for screen sharing and remote collaboration.
  - If you want to connect to a screen that is attached to another session, use the `screen -DRR` command.

### Task Management

- If you append an ampersand (`&`) to the end of a command, the task is sent to the background, and you are provided with a prompt immediately.
- If you append double ampersands (`&&`) to the end of a command, the shell will wait until the preceding command completes successfully before executing the next command.

### Command History

- `bash` saves a history of recently issued commands in a `~/.history/` file.
  - You can access these commands with the `arrow` keys, or with `Control-P`, if you need to go back and use or reuse a past command.

### Emacs Key Bindings

- `Control-a` Cursor to the beginning of the line (`Control-a Control-a` in screen)
- `Control-e` Cursor to the end of the line
- `Control-f` Move cursor forward one character
- `Control-b` Move cursor back one character
- `Alt-f` Move cursor forward one word
- `Alt-b` Move cursor back one word

---

[Terminal]:https://www.linode.com/docs/tools-reference/tools/using-the-terminal/
