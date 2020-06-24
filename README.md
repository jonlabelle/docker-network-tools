# Docker Network Tools

[![Docker Pulls](https://img.shields.io/docker/pulls/jonlabelle/network-tools.svg)][dockerhub]

> Minimal Docker image ([alpine:latest](https://hub.docker.com/_/alpine)) with various network tools pre-installed.

## Installed Network Tools

- [`curl`](https://curl.haxx.se) - Command line tool and library for transferring data with URLs.
- [`fping`](https://fping.org) - A grep-like utility that allows you to search for network packets on an interface.
- [`ipcalc`](http://jodies.de/ipcalc) - Network IP calculator.
- [`iperf`](https://sourceforge.net/projects/iperf2/) - A tool to measure IP bandwidth using UDP or TCP.
- [`jq`](https://stedolan.github.io/jq/) - A lightweight and flexible command line JSON processor.
- [`macchanger`](https://github.com/alobbs/macchanger) - A utility for viewing/manipulating the MAC address of network interfaces.
- [`netcat`](https://packages.debian.org/sid/netcat-openbsd) - The TCP/IP swiss army knife (OpenBSD variant).
- [`ngrep`](https://github.com/jpr5/ngrep/) - A grep-like utility that allows you to search for network packets on an interface.
- [`nload`](http://www.roland-riegel.de/nload/) - Console network traffic and bandwidth monitor.
- [`nmap`](https://nmap.org/) - Network Security Scanner.
- [`tcpdump`](https://www.tcpdump.org) - Dump and analyze traffic on a network.
- [`wget`](https://www.gnu.org/software/wget/wget.html) - A network utility to retrieve files from the web.
- [bind-tools](https://www.isc.org/dns-tools/) - The ISC DNS tools.
    - `arpaname` - Translate IP addresses to the corresponding ARPA names.
    - `delv` - DNS lookup and validation utility.
    - `dig` - DNS lookup utility.
    - `dnstap-read` - Print dnstap data in human-readable form.
    - `host` - DNS lookup utility.
    - `mdig` - DNS pipelined lookup utility.
    - `named-rrchecker` - Syntax checker for individual DNS resource records.
    - `nslookup` - Query Internet name servers interactively.
    - `nsupdate` - Dynamic DNS update utility.
    - `ddns-confgen` - DDNS key generation tool.
    - `named-checkzone` - Zone file validity checking or converting tool.
    - `named-compilezone` - Zone file validity checking or converting tool (similar to `named-checkzone`, but it always dumps the zone contents to a specified file in a specified format).
    - `named-journalprint` - Print zone journal in human-readable form.
    - `rndc-confgen` - RNDC key generation tool.
    - `tsig-keygen` - DDNS key generation tool.
- [iputils](https://github.com/iputils/iputils/) - IP Configuration Utilities (and Ping).
    - `arping` - Send ARP REQUEST to a neighbor host.
    - `clockdiff` - Measure clock difference between hosts.
    - `ninfod` - Respond to IPv6 Node Information Queries.
    - `ping` - Send IP4 ICMP ECHO_REQUEST to network hosts.
    - `ping6` - Send IP6 ICMP ECHO_REQUEST to network hosts.
    - `rarpd` - Reverse Address Resolution Protocol(RARP) daemon.
    - `rdisc` - Network router discovery daemon.
    - `tftpd` - IPv4 Trivial File Transfer Protocol client.
    - `tracepath` - Traces path to a IP4 network host discovering MTU along this path.
    - `tracepath6` - Traces path to a IP6 network host discovering MTU along this path.
    - `traceroute6` - Print the route packets trace to IP6 network host.
- [net-tools](https://sourceforge.net/projects/net-tools/) - Linux networking base tools.
    - `netstat` - Print network connections, routing tables, interface statistics, masquerade connections, and multicast memberships.
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
