# Docker Network Tools

[![Docker Pulls](https://img.shields.io/docker/pulls/jonlabelle/network-tools.svg)][dockerhub]

> Minimal Docker image ([alpine:latest](https://hub.docker.com/_/alpine)) with various network tools pre-installed.

- [fping](https://fping.org) - A grep-like utility that allows you to search for network packets on an interface.
- [macchanger](https://github.com/alobbs/macchanger) - An utility for viewing/manipulating the MAC address of network interfaces.
- [netcat](https://packages.debian.org/sid/netcat-openbsd) - The TCP/IP swiss army knife (OpenBSD variant).
- [ngrep](https://github.com/jpr5/ngrep/) - A grep-like utility that allows you to search for network packets on an interface.
- [nmap](https://nmap.org/) - Network Security Scanner.
- [net-tools](https://sourceforge.net/projects/net-tools/) - Linux networking base tools.
    - `netstat` - Print network connections, routing tables, interface statistics, masquerade connections, and multicast memberships
    - `ypdomainname` - Show or set the system's NIS/YP domain name.
    - `dnsdomainname` - Show the system's DNS domain name.
    - `route` - Show / manipulate the IP routing table.
    - `nisdomainname` - Show or set system's NIS/YP domain name.
    - `domainname` - Show or set the system's NIS/YP domain name.
    - `hostname` - Show or set the system's host name.
    - `ifconfig` - Configure a network interface.
    - `arp` - Manipulate the system ARP cache.
    - `ipmaddr` - Adds, deletes, and displays multicast addresses.
    - `rarp` - Manipulate the system RARP table.
    - `slattach` - Attach a network interface to a serial line.
    - `nameif` - Name network interfaces based on MAC addresses.
    - `iptunnel` - Creates, deletes, and displays configured tunnels.
    - `plipconfig` - Fine tune PLIP device parameters.

## Resources

- [jonlabelle/network-tools](https://hub.docker.com/r/jonlabelle/network-tools) on Docker Hub
- [Dockerfile](https://github.com/jonlabelle/docker-network-tools/blob/master/Dockerfile) on GitHub

## Usage

To launch an interactive shell (`bin/sh`) terminal session, and start using the network tools:

```bash
docker run -it jonlabelle/network-tools
```

## Also see

- [jonlabelle/nmap](https://hub.docker.com/r/jonlabelle/nmap) - Minimal Docker image with Nmap Network Security Scanner pre-installed.

[dockerhub]: https://hub.docker.com/r/jonlabelle/network-tools
