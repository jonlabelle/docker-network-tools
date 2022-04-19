# Docker Network Tools

[![cd](https://github.com/jonlabelle/docker-network-tools/actions/workflows/cd.yml/badge.svg)](https://github.com/jonlabelle/docker-network-tools/actions/workflows/cd.yml)
[![Docker Hub pulls](https://img.shields.io/docker/pulls/jonlabelle/network-tools.svg)][dockerhub]
[![CodeQL Analysis](https://github.com/jonlabelle/docker-network-tools/actions/workflows/code-analysis.yml/badge.svg)](https://github.com/jonlabelle/docker-network-tools/actions/workflows/code-analysis.yml "CodeQL Analysis")

> A Docker image with various network tools pre-installed.

## Bandwidth

| Tool                                                | Description                                      | Resources                                        |
| --------------------------------------------------- | ------------------------------------------------ | ------------------------------------------------ |
| [`nload`](https://github.com/rolandriegel/nload)    | Console network traffic and bandwidth monitor.   | [command examples](https://tldr.ostera.io/nload) |
| [`iperf`](https://sourceforge.net/projects/iperf2/) | A tool to measure IP bandwidth using UDP or TCP. | [command examples](https://tldr.ostera.io/iperf) |

## DNS

| Tool                                            | Description                                               | Resources                                                                               |
| ----------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `arpaname`                                      | Translate IP addresses to the corresponding ARPA names.   | -                                                                                       |
| `ddns-confgen`                                  | DDNS key generation tool.                                 | -                                                                                       |
| `delv`                                          | DNS lookup and validation utility.                        | -                                                                                       |
| `dig`                                           | DNS lookup utility.                                       | -                                                                                       |
| `dnsdomainname`                                 | Show the system's DNS domain name.                        | -                                                                                       |
| `dnstap-read`                                   | Print dnstap data in human-readable form.                 | -                                                                                       |
| `domainname`                                    | Show or set the system's NIS/YP domain name.              | -                                                                                       |
| [`drill`](https://nlnetlabs.nl/projects/ldns/)  | DNS(SEC) query tool ala dig.                              | [command examples](https://tldr.ostera.io/drill)                                        |
| `host`                                          | DNS lookup utility.                                       | -                                                                                       |
| `hostname`                                      | Show or set the system's host name.                       | -                                                                                       |
| [`libidn`](https://www.gnu.org/software/libidn) | Encode/decode library for internationalized domain names. | [command examples](https://www.gnu.org/software/libidn/manual/libidn.html#Invoking-idn) |
| `mdig`                                          | DNS pipelined lookup utility.                             | -                                                                                       |
| `named-checkzone`                               | Zone file validity checking or converting tool.           | -                                                                                       |
| `named-compilezone`                             | Zone file validity checking or converting tool.           | -                                                                                       |
| `named-journalprint`                            | Print zone journal in human-readable form.                | -                                                                                       |
| `named-rrchecker`                               | Syntax checker for individual DNS resource records.       | -                                                                                       |
| `nisdomainname`                                 | Show or set system's NIS/YP domain name.                  | -                                                                                       |
| `nslookup`                                      | Query Internet name servers interactively.                | -                                                                                       |
| `nsupdate`                                      | Dynamic DNS update utility.                               | -                                                                                       |
| `rndc-confgen`                                  | RNDC key generation tool.                                 | -                                                                                       |
| `tsig-keygen`                                   | DDNS key generation tool.                                 | -                                                                                       |
| `ypdomainname`                                  | Show or set the system's NIS/YP domain name.              | -                                                                                       |

## HTTP/Web

| Tool                                                                      | Description                                             | Resources                                                         |
| ------------------------------------------------------------------------- | ------------------------------------------------------- | ----------------------------------------------------------------- |
| [`ab`](https://httpd.apache.org/docs/current/programs/ab.html)            | Apache HTTP server benchmarking tool.                   | [command examples](https://tldr.ostera.io/ab)                     |
| [`curl`](https://curl.haxx.se)                                            | Tool for transferring data with URLs.                   | [command examples](https://tldr.ostera.io/curl)                   |
| [`jq`](https://stedolan.github.io/jq/)                                    | A lightweight and flexible command line JSON processor. | [command examples](https://tldr.ostera.io/jq)                     |
| [`oath-toolkit-oathtool`](https://www.nongnu.org/oath-toolkit/index.html) | Generate and validate one-time passwords.               | [man page](https://www.nongnu.org/oath-toolkit/man-oathtool.html) |
| [`requests`](https://pypi.org/project/requests/)                          | Simple HTTP library for Python.                         | [docs](https://docs.python-requests.org/en/latest/)               |
| [`wget`](https://www.gnu.org/software/wget/wget.html)                     | A network utility to retrieve files from the web.       | [command examples](https://tldr.ostera.io/wget)                   |

## IP Routing

| Tool     | Description                                                    | Resources |
| -------- | -------------------------------------------------------------- | --------- |
| `bridge` | Show / manipulate bridge addresses and devices.                | -         |
| `ctstat` | Unified linux network statistics.                              | -         |
| `genl`   | Generic netlink utility frontend.                              | -         |
| `ifcfg`  | Simplistic script which replaces ifconfig IP management.       | -         |
| `ifstat` | Handy utility to read network interface statistics.            | -         |
| `lnstat` | Unified linux network statistics.                              | -         |
| `nstat`  | Network statistics tools.                                      | -         |
| `route`  | Show / manipulate the IP routing table.                        | -         |
| `routef` | Flush network routes.                                          | -         |
| `routel` | List routes with pretty output format.                         | -         |
| `rtacct` | Monitor kernel SNMP counters and network interface statistics. | -         |
| `rtmon`  | Listens to and monitors RTnetlink.                             | -         |
| `rtpr`   | Replace backslashes with newlines.                             | -         |
| `rtstat` | Unified linux network statistics.                              | -         |

## IP and MAC address

| Tool                                                 | Description                                                | Resources                                   |
| ---------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------- |
| `ifconfig`                                           | Configure a network interface.                             | -                                           |
| [`ipcalc`](https://jodies.de/ipcalc)                 | Network IP calculator.                                     | [man page](https://manned.org/ipcalc.1)     |
| `ipmaddr`                                            | Adds, deletes, and displays multicast addresses.           | -                                           |
| [`macchanger`](https://github.com/alobbs/macchanger) | View and manipulate the MAC address of network interfaces. | [man page](https://manned.org/macchanger.1) |
| `nameif`                                             | Name network interfaces based on MAC addresses.            | -                                           |
| `plipconfig`                                         | Fine tune PLIP device parameters.                          | -                                           |
| `rarp`                                               | Manipulate the system RARP table.                          | -                                           |
| `slattach`                                           | Attach a network interface to a serial line.               | -                                           |

## Packet analysis

| Tool                                         | Description                                                                        | Resources                                                               |
| -------------------------------------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| [`fping`](https://fping.org)                 | A grep-like utility that allows you to search for network packets on an interface. | [command examples](https://tldr.ostera.io/fping)                        |
| [`hping3`](https://github.com/antirez/hping) | A ping-like TCP/IP packet assembler/analyzer.                                      | [command examples](https://tldr.ostera.io/hping3)                       |
| [`ngrep`](https://github.com/jpr5/ngrep/)    | A grep-like utility that allows you to search for network packets on an interface. | [command examples](https://tldr.ostera.io/ngrep)                        |
| [`tcpdump`](https://www.tcpdump.org)         | Dump and analyze traffic on a network.                                             | [tcpdump examples](https://tldr.ostera.io/tcpdump)                      |
| [`tshark`](https://www.wireshark.org/)       | Network protocol analyzer (console version).                                       | [tshark man page](https://www.wireshark.org/docs/man-pages/tshark.html) |

## Scanning and discovery

| Tool                                                      | Description                                                                                                         | Resources                                           |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| [`arp-scan`](https://github.com/royhills/arp-scan)        | Address Resolution Protocol (ARP) packet scanner.                                                                   | [command examples](https://tldr.ostera.io/arp-scan) |
| `arp`                                                     | Manipulate the system ARP cache.                                                                                    | -                                                   |
| `arping`                                                  | Send ARP REQUEST to a neighbor host.                                                                                | -                                                   |
| `clockdiff`                                               | Measure clock difference between hosts.                                                                             | -                                                   |
| [`masscan`](https://github.com/robertdavidgraham/masscan) | Internet-scale port scanner.                                                                                        | [command examples](https://tldr.ostera.io/masscan)  |
| `netstat`                                                 | Print network connections, routing tables, interface statistics, masquerade connections, and multicast memberships. | -                                                   |
| `ninfod`                                                  | Respond to IPv6 Node Information Queries.                                                                           | -                                                   |
| [`nmap`](https://nmap.org/)                               | Network Security Scanner.                                                                                           | [command examples](https://tldr.ostera.io/nmap)     |
| `ping6`                                                   | Send IP6 ICMP ECHO_REQUEST to network hosts.                                                                        | -                                                   |
| `ping`                                                    | Send IP4 ICMP ECHO_REQUEST to network hosts.                                                                        | -                                                   |
| `rarpd`                                                   | Reverse Address Resolution Protocol(RARP) daemon.                                                                   | -                                                   |
| `rdisc`                                                   | Network router discovery daemon.                                                                                    | -                                                   |

## Transmission and communication

| Tool                                                       | Description                                        | Resources                                          |
| ---------------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `iptunnel`                                                 | Creates, deletes, and displays configured tunnels. | -                                                  |
| [`netcat`](https://packages.debian.org/sid/netcat-openbsd) | The TCP/IP swiss army knife (OpenBSD variant).     | [command examples](https://tldr.ostera.io/netcat)  |
| [`openssl`](https://www.openssl.org/)                      | Toolkit for Transport Layer Security (TLS).        | [command examples](https://tldr.ostera.io/openssl) |
| [`socat`](http://www.dest-unreach.org/socat/)              | Multipurpose relay for binary protocols.           | [command examples](https://tldr.ostera.io/socat)   |
| [`ssh`](https://www.openssh.com/portable.html)             | OpenBSD's SSH client.                              | [command examples](https://tldr.ostera.io/ssh)     |
| `tftpd`                                                    | IPv4 Trivial File Transfer Protocol client.        | -                                                  |

## Trace

| Tool                                   | Description                                                        | Resources                                      |
| -------------------------------------- | ------------------------------------------------------------------ | ---------------------------------------------- |
| [`mtr`](https://www.bitwizard.nl/mtr/) | Full screen ncurses traceroute tool.                               | [command examples](https://tldr.ostera.io/mtr) |
| `tracepath6`                           | Traces path to a IP6 network host discovering MTU along this path. | -                                              |
| `tracepath`                            | Traces path to a IP4 network host discovering MTU along this path. | -                                              |
| `traceroute6`                          | Print the route packets trace to IP6 network host.                 | -                                              |

## Additional tools included

| Tool                                              | Description                                                   | Resources                                                         |
| ------------------------------------------------- | ------------------------------------------------------------- | ----------------------------------------------------------------- |
| [`envsubst`](https://github.com/kaniini/envsubst) | Perform variable substitutions on input.                      | [command examples](https://tldr.ostera.io/envsubst)               |
| `find`                                            | Search for files in a directory hierarchy.                    | [command examples](https://tldr.ostera.io/find)                   |
| [`git`](https://www.git-scm.com/)                 | Distribute d version control system.                          | [command examples](https://tldr.ostera.io/git)                    |
| `free`                                            | Report the amount of free and used memory in the system.      |                                                                   |
| `kill`                                            | Send a signal to a process based on PID.                      |                                                                   |
| `locate`                                          | List files in databases that match a pattern.                 | [man page](https://man7.org/linux/man-pages/man1/locate.1.html)   |
| `pgrep`                                           | List processes based on name or other attributes.             |                                                                   |
| `pkill`                                           | Send a signal to a process based on name or other attributes. |                                                                   |
| `pmap`                                            | Report memory map of a process.                               |                                                                   |
| `ps`                                              | Report information of processes.                              |                                                                   |
| `pwdx`                                            | Report current directory of a process.                        |                                                                   |
| `skill`                                           | Obsolete version of pgrep/pkill.                              |                                                                   |
| `slabtop`                                         | Display kernel slab cache information in real time.           |                                                                   |
| `snice`                                           | Renice a process.                                             |                                                                   |
| `sysctl`                                          | Read or Write kernel parameters at run-time.                  |                                                                   |
| `tload`                                           | Graphical representation of system load average.              |                                                                   |
| `top`                                             | Dynamic real-time view of running processes.                  |                                                                   |
| `updatedb`                                        | Update a file name database.                                  | [man page](https://man7.org/linux/man-pages/man1/updatedb.1.html) |
| `uptime`                                          | Display how long the system has been running.                 |                                                                   |
| `vmstat`                                          | Report virtual memory statistics.                             |                                                                   |
| `w`                                               | Report logged in users and what they are doing.               |                                                                   |
| `watch`                                           | Execute a program periodically, showing output full-screen.   |                                                                   |
| `xargs`                                           | Build and execute command lines from standard input.          | [command examples](https://tldr.ostera.io/xargs)                  |

## Usage

To use the tools in a new container from a terminal session:

```bash
docker run --rm -it jonlabelle/network-tools
```

**Docker Run Options:**

| Option                | Description                                       |
| --------------------- | ------------------------------------------------- |
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
[network-tools]$ nmap -v 10.0.10.0/24
Starting Nmap 7.91 ( https://nmap.org ) at 2021-04-26 15:32 UTC
Initiating Ping Scan at 15:32
Scanning 256 hosts [4 ports/host]
...
```

## Related

-   [jonlabelle/docker-nmap](https://github.com/jonlabelle/docker-nmap). Minimal Docker image with Nmap Network Security Scanner pre-installed.

## License

[MIT License](https://github.com/jonlabelle/docker-network-tools/blob/main/LICENSE.txt)

[dockerhub]: https://hub.docker.com/r/jonlabelle/network-tools
[docker hub]: https://hub.docker.com/r/jonlabelle/network-tools
[github container registry]: https://github.com/users/jonlabelle/packages/container/package/network-tools
[docker run reference]: https://docs.docker.com/engine/reference/run/
[docker run options documentation]: https://docs.docker.com/engine/reference/commandline/run/#options
