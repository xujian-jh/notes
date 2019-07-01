# command

## Not root user command `$`

- Check the current kernel version

```s
uname -r
```

### The SSH keys

- Query the SSH keys

```s
ls -al ~/.ssh
```

- Generate the SSH keys
  - `ssh-keygen`
  - `-t rsa` [-t dsa | ecdsa | ed25519 | rsa]
  - `-C your_email@example.com` [-C comment]

```s
ssh-keygen -t rsa -C your_email@example.com
```

- Get id_rsa.pub

```s
cat ~/.ssh/id_rsa.pub
```

## Change user from `$` to `#`

- Enter root by password

```s
su - root
```

- Forced entry to root user without password

```s
sudo su - root
```

## The root user command `#`

- The root user views all password Settings

```s
more /etc/passwd
```

- The root user change password

```s
passwd
```

- The root user log-off

```s
exit
```
