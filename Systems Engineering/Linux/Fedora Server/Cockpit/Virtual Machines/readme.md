# [Virtual Machines]

## Installing software

The required software prerequisites are `libvirt`, `cockpit` and `cockpit-machines`. To install them on Fedora 31, run the following command from a terminal using sudo:

```s
sudo dnf install libvirt cockpit cockpit-machines
```

Cockpit is also included as part of the “Headless Management” package group. This group is useful for a Fedora based server that you only access through a network. In that case, to install it, use this command:

```s
sudo dnf groupinstall "Headless Management"
```

## Setting up Cockpit services

The libvirtd service runs the virtual machines, while Cockpit has a socket activated service to let you access the Web GUI:

```s
sudo systemctl enable libvirtd --now
sudo systemctl enable cockpit.socket --now
```

Optionally, if you want to access and manage your machine from another device on your network, you need to expose the service to the network. To do this, add a new rule in your firewall configuration:

```s
sudo firewall-cmd --zone=public --add-service=cockpit --permanent
sudo firewall-cmd --reload
```

To confirm the services are running and no issues occurred, check the status of the services:

```s
sudo systemctl status libvirtd
sudo systemctl status cockpit.socket
```

At this point everything should be working. The Cockpit web GUI should be available at `https://localhost:9090` or `https://127.0.0.1:9090`. Or, enter the local network IP in a web browser on any other device connected to the same network. (Without SSL certificates setup, you may need to allow a connection from your browser.)

## Creating and installing a machine

Select Virtual Machines and then select Create VM to build a new box. The console gives you several options:

- Download an OS using Cockpit’s built in library
- Use install media already downloaded on the system you’re managing
- Point to a URL for an OS installation tree
- Boot media over the network via the PXE protocol

Enter all the necessary parameters. Then select Create to power up the new virtual machine.

---

[Virtual Machines]:https://fedoramagazine.org/create-virtual-machines-with-cockpit-in-fedora/
