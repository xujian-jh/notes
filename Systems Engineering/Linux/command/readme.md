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

## Change git port( 22 to 443)

```bash
[sword@localhost ~]$ cd .ssh
[sword@localhost .ssh]$ ls
config  id_rsa  id_rsa.pub  known_hosts
[sword@localhost .ssh]$ vi config
[sword@localhost .ssh]$ cat config

Host github.com  
User xujian-jh  
Hostname ssh.github.com  
PreferredAuthentications publickey  
IdentityFile ~/.ssh/id_rsa  
Port 443
[sword@localhost .ssh]$ ssh -T git@github.com
Bad owner or permissions on /home/sword/.ssh/config
[sword@localhost .ssh]$ chmod 600 *
[sword@localhost .ssh]$ ssh -T git@github.com
The authenticity of host '[ssh.github.com]:443 ([192.30.253.123]:443)' can't be established.
RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[ssh.github.com]:443,[192.30.253.123]:443' (RSA) to the list of known hosts.
Hi xujian-jh! You've successfully authenticated, but GitHub does not provide shell access.
[sword@localhost .ssh]$
```
