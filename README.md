# Docker Network Tools

[![cd](https://github.com/jonlabelle/docker-network-tools/actions/workflows/cd.yml/badge.svg)](https://github.com/jonlabelle/docker-network-tools/actions/workflows/cd.yml)
[![Docker Hub pulls](https://img.shields.io/docker/pulls/jonlabelle/network-tools.svg?label=docker%20hub%20pulls)][dockerhub]

> A Docker image with various network tools pre-installed.

## Included tools

- [`ab`](https://httpd.apache.org/docs/current/programs/ab.html) - Apache HTTP server benchmarking tool.
- [`arp-scan`](https://github.com/royhills/arp-scan) - Address Resolution Protocol (ARP) packet scanner.
- [`curl`](https://curl.haxx.se) - Command line tool and library for transferring data with URLs.
- [`drill`](https://nlnetlabs.nl/projects/ldns/) - DNS(SEC) query tool ala dig.
- [`envsubst`](https://github.com/kaniini/envsubst) - Perform variable substitutions on input.
- [`fping`](https://fping.org) - A grep-like utility that allows you to search for network packets on an interface.
- [`git`](https://www.git-scm.com/) - Distributed version control system.
- [`hping3`](https://github.com/antirez/hping) - A ping-like TCP/IP packet assembler/analyzer.
- [`ipcalc`](http://jodies.de/ipcalc) - Network IP calculator.
- [`iperf`](https://sourceforge.net/projects/iperf2/) - A tool to measure IP bandwidth using UDP or TCP.
- [`jq`](https://stedolan.github.io/jq/) - A lightweight and flexible command line JSON processor.
- [`libidn`](https://www.gnu.org/software/libidn) - Encode/Decode library for internationalized domain names.
- [`macchanger`](https://github.com/alobbs/macchanger) - A utility for viewing/manipulating the MAC address of network interfaces.
- [`masscan`](https://github.com/robertdavidgraham/masscan) - Internet-scale port scanner.
- [`mtr`](https://www.bitwizard.nl/mtr/) - Full screen ncurses traceroute tool.
- [`netcat`](https://packages.debian.org/sid/netcat-openbsd) - The TCP/IP swiss army knife (OpenBSD variant).
- [`ngrep`](https://github.com/jpr5/ngrep/) - A grep-like utility that allows you to search for network packets on an interface.
- [`nload`](https://github.com/rolandriegel/nload) - Console network traffic and bandwidth monitor.
- [`nmap`](https://nmap.org/) - Network Security Scanner.
- [`oath-toolkit-oathtool`](https://www.nongnu.org/oath-toolkit/index.html) - A command line tool for generating and validating OTPs (One-Time Passwords).
- [`openssl`](https://www.openssl.org/) - Toolkit for Transport Layer Security (TLS).
- [`socat`](http://www.dest-unreach.org/socat/) - Multipurpose relay for binary protocols.
- [`ssh`](https://www.openssh.com/portable.html) - OpenBSD's SSH client.
- [`tcpdump`](https://www.tcpdump.org) - Dump and analyze traffic on a network.
- [`tshark`](https://www.wireshark.org/) - Network protocol analyzer (Console version).
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
- [findutils](https://www.gnu.org/software/findutils/) - GNU utilities for finding files.
    - `find` - Search for files in a directory hierarchy.
    - `locate` - List files in databases that match a pattern.
    - `updatedb` - Update a file name database.
    - `xargs` - Build and execute command lines from standard input.
- [iproute2](https://wiki.linuxfoundation.org/networking/iproute2) - IP Routing Utilities.
    - `bridge` - Show / manipulate bridge addresses and devices.
    - `ctstat` Unified linux network statistics.
    - `genl` - Generic netlink utility frontend.
    - `ifcfg` - Simplistic script which replaces ifconfig IP management.
    - `ifstat` - Handy utility to read network interface statistics.
    - `lnstat` - Unified linux network statistics.
    - `nstat` - Network statistics tools.
    - `routef` - Flush network routes.
    - `routel` - List routes with pretty output format.
    - `rtacct` - Monitor kernel SNMP counters and network interface statistics.
    - `rtmon` - Listens to and monitors RTnetlink.
    - `rtpr` - Replace backslashes with newlines.
    - `rtstat` - Unified linux network statistics.
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
- [procps](https://gitlab.com/procps-ng/procps) - Utilities for monitoring your system and processes on your system.
    - `free` - Report the amount of free and used memory in the system.
    - `kill` - Send a signal to a process based on PID.
    - `pgrep` - List processes based on name or other attributes.
    - `pkill` - Send a signal to a process based on name or other attributes.
    - `pmap` - Report memory map of a process.
    - `ps` - Report information of processes.
    - `pwdx` - Report current directory of a process.
    - `skill` - Obsolete version of pgrep/pkill.
    - `slabtop` - Display kernel slab cache information in real time.
    - `snice` - Renice a process.
    - `sysctl` - Read or Write kernel parameters at run-time.
    - `tload` - Graphical representation of system load average.
    - `top` - Dynamic real-time view of running processes.
    - `uptime` - Display how long the system has been running.
    - `vmstat` - Report virtual memory statistics.
    - `w` - Report logged in users and what they are doing.
    - `watch` - Execute a program periodically, showing output full-screen.
- [python3](https://www.python.org) - Python 3 language interpreter.
    - [requests](https://pypi.org/project/requests/) - Requests is an elegant and simple HTTP library for Python, built for human beings.

## Usage

To use the tools in a new container from a terminal session:

```bash
docker run --rm -it jonlabelle/network-tools
```

**Docker Run Options:**

|         Option        |                    Description                    |
|-----------------------|---------------------------------------------------|
| `--rm`                | Automatically remove the container when it exits. |
| `--interactive`, `-i` | Keep STDIN open even if not attached              |
| `--tty`, `-t`         | Allocate a pseudo-TTY                             |

See [Docker Run Options documentation] for more options.

## Examples

> **NOTE:** To pull from [GitHub Container Registry], instead of [Docker Hub],
> replace `jonlabelle/network-tools` with `ghcr.io/jonlabelle/network-tools` in
> the examples below.

Use [Nmap](https://nmap.org/) to scan for devices on a local network (10.0.10.0/24):

```console
$ docker run --rm -it jonlabelle/network-tools
[docker@network-tools]$ nmap -v 10.0.10.0/24
Starting Nmap 7.91 ( https://nmap.org ) at 2021-04-26 15:32 UTC
Initiating Ping Scan at 15:32
Scanning 256 hosts [4 ports/host]
...
...
...
```

## Related

- [jonlabelle/docker-nmap](https://github.com/jonlabelle/docker-nmap). Minimal Docker image with Nmap Network Security Scanner pre-installed.

## License

[MIT License](https://github.com/jonlabelle/docker-network-tools/blob/main/LICENSE.txt)

[dockerhub]: https://hub.docker.com/r/jonlabelle/network-tools
[Docker Hub]: https://hub.docker.com/r/jonlabelle/network-tools
[GitHub Container Registry]: https://github.com/users/jonlabelle/packages/container/package/network-tools
[Docker run reference]: https://docs.docker.com/engine/reference/run/
[Docker Run Options documentation]: https://docs.docker.com/engine/reference/commandline/run/#options
