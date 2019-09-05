# [Visual Studio Code]

We currently ship the stable 64-bit VS Code in a yum repository, the following script will install the key and repository:

```bash
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo sh -c 'echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo'
```

Then update the package cache and install the package using dnf (Fedora 22 and above):

```bash
sudo dnf check-update
sudo dnf install code
```

Or on older versions using yum:

```bash
yum check-update
sudo yum install code
```

Due to the manual signing process and the system we use to publish, the yum repo may lag behind and not get the latest version of VS Code immediately.

## Extensions

1. Chinese (Simplified) Language Pack for Visual Studio Code
2. markdownlint
3. Debugger for Chrome

---

[Visual Studio Code]: https://code.visualstudio.com/docs/setup/linux#_rhel-fedora-and-centos-based-distributions
