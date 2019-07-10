# [Command line quick tips: Permissions]

## Permission basics

Any file or folder on Fedora has three sets of permissions assigned.

1. The first set is for the user who owns the file or folder.
2. The second is for the group that owns it.
3. The third set is for everyone else who’s not the user who owns the file, or in the group that owns the file.Sometimes this is called the world.

Each set of permissions comes in three flavors.

1. Read (r).
2. Write (w).
3. Execute (x).

## File permissions

1. Read (r): the file content can be read
2. Write (w): the file content can be changed
3. Execute (x): the file can be executed — this is used primarily for programs or scripts that are meant to be run directly

You can see the three sets of these permissions when you do a long listing of any file. Try this with the /etc/services file on your system:

```bash
$ ls -l /etc/services
-rw-r--r--. 1 root root 692241 Apr  9 03:47 /etc/services
```

- The dash at the far left shows this is a regular file.
  - Note the d at the far left. It shows this is a directory, or folder.

1. The user owner is root. `rw-` The user owner has read and write access to the file.
2. The group owner is the root group. `r--` Anyone in the group root can only read the file.
3. And finally,  `r--` Anyone in the world can only read the file.

## Folder (directory) permissions

1. Read (r): the folder contents can be read (such as the ls command)
2. Write (w): the folder contents can be changed (files can be created or erased in this folder)
3. Execute (x): the folder can be searched, although its contents cannot be read.

Take a look at the /etc/grub.d folder for example:

```bash
$ ls -ld /etc/grub.d
drwx------. 2 root root 4096 May 23 16:28 /etc/grub.d
```

- Note the d at the far left. It shows this is a directory, or folder.

1. The user owner is root. `rwx` The user owner can read, change, and cd into this folder.
2. The group owner is the root group. `---` Anyone in the group root `Permission denied`.
3. And finally,  `---` Anyone in the world `Permission denied`.

### Your private folder

Now, notice how no one, other than you as the owner, can access anything in this folder. This is intentional! You wouldn’t want others to be able to read your private content on a shared system.

```bash
$ ls -ld $HOME
drwx------. 221 paul paul 28672 Jul  3 14:03 /home/paul
```

### Making a shared folder

Make a folder for sharing, and set it to be owned by the finance group

```bash
$ sudo mkdir -p /home/shared/finance
$ sudo chgrp finance /home/shared/finance
$ ls -ld /home/shared/finance
drwxr-xr-x. 2 root finance 4096 Jul  6 15:35 finance
```

By default the new folder has these permissions. Notice how it can be read or searched by anyone, even if they can’t create or erase files in it.

```bash
$ sudo chmod g+w,o-rx /home/shared/finance
$ ls -ld /home/shared/finance
drwxrwx---. 2 root finance 4096 Jul  6 15:35 finance
```

Next, use the `chmod` command to change the mode (permissions) of the shared folder.

1. `u` would change the user owner’s permissions
2. `g` to change the owning group’s permissions
3. `o` to change other users’ permissions

---

[Command line quick tips: Permissions]:https://fedoramagazine.org/command-line-quick-tips-permissions/
