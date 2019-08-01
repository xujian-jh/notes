# [Command line quick tips: More about permissions]

## Symbolic and octal

- r = 4
- w = 2
- x = 1

Now you can express any combination with a single octal value.

For instance, read and write permission, but no execute permission, would have a value of 6. Read and execute permission only would have a value of 5. A file’s rwxr-xr-x symbolic permission has an octal value of 755.

You can use octal values to set file permissions with the chmod command similarly to symbolic values.

```bash
chmod u=rw,g=r,o=r myfile1
```

```bash
chmod 644 myfile1
```

## Special permission bits

- setuid (or suid) = 4
  - forceing `Execute (x)` , the permission of the user
  - A good example of setuid is the /bin/passwd utility, which allows a user to set or change passwords. This utility must be able to write to files no user should be allowed to change.
- setgid (or sgid) = 2
  - forceing `Execute (x)` , the permissions of the group
- sticky bit (or delete inhibit) = 1
  - prevent `Execute (x)` , the permission of non-owner users.
  - The sticky bit set on a directory will prevent a user from deleting files in that directory owned by other users.

1. The way to set these bits with chmod in octal mode is to add a value prefix, such as `4755` to add setuid to an executable file.
2. In symbolic mode, the u and g can be used to set or remove setuid and setgid, such as `u+s`,`g+s`. The sticky bit is set using `o+t`.

### Sharing and special permissions

```bash
drwxrwx---. 2 root finance 4096 Jul  6 15:35 finance
```

1. One problem with this directory is that users dwayne and jill, who are both members of the finance group, can delete each other’s files. That’s not optimal for a shared space. It might be useful in some situations, but probably not when dealing with financial records!
2. Another problem is that files in this directory may not be truly shared, because they will be owned by the default groups of dwayne and jill — most likely the user private groups also named dwayne and jill.

#### Solution

A better way to solve this is to set both setgid and the sticky bit on the folder. This will do two things — cause files created in the folder to be owned by the finance group automatically, and prevent dwayne and jill from deleting each other’s files.

- In symbolic mode

```bash
sudo chmod u+rwx,g+rwxs,o+t finance
```

- In octal mode

```bash
sudo chmod 3770 finance
```

The long listing now shows the new special permissions applied. The sticky bit appears as T and not t because the folder is not searchable for users outside the finance group.

```bash
drwxrws--T. 2 root finance 4096 Jul  6 15:35 finance
```

---

[Command line quick tips: More about permissions]:https://fedoramagazine.org/command-line-quick-tips-more-about-permissions/
