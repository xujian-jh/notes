# [Accounts]

## Create New Account

To begin, click the Create New Account button. A box appears, requesting basic information such as the full name, username, and password. It also provides the option to lock the account. Click Create to complete the process.

## Account Settings

- Modifying an account
  - To modify an account, go back to the accounts page and select the user you wish to modify. Here, we can change the full name and elevate the user’s role to Server Administrator — this adds user to the wheel group. It also includes options for access and passwords.
  - The Access options allow admins to lock the account. Clicking Never lock account will open the “Account Expiration” box. From here we can choose to Never lock the account, or to lock it on a scheduled date.
- Password management
  - Admins can choose to Set password and Force Change. The first option prompts you to enter a new password. The second option forces users to create a new password the next time they login.
  - Selecting the Never change password option opens a box with two options. The first is Never expire the password. This allows the user to keep their password without the need to change it. The second option is Require Password change every … days. This determines the amount of days a password can be used before it must be changed.
- Adding public keys
  - We can also add public SSH keys from remote computers for password-less authentication. This is equivalent to the ssh-copy-id command. To start, click the Add Public Key (+) button. Finally, copy the public key from a remote machine and paste it into the box.
  - To remove the key, click the remove (-) button to the right of the key.
- Terminating the session and deleting an account
  - Clicking the Terminate Session button immediately disconnects the user.
  - Clicking the Delete button removes the user and offers to delete the user’s files with the account.

## 389 Directory Server

Cockpit has a plugin for managing the 389 Directory Service. To add the 389 Directory Server UI, run the following command using sudo:

```s
sudo dnf install cockpit-389-ds
```

For more information regarding [389 Directory Server], visit their documentation site.

---

[Accounts]:https://fedoramagazine.org/managing-user-accounts-with-cockpit/

[389 Directory Server]:https://directory.fedoraproject.org/index.html
