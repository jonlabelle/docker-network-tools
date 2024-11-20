# Docker Network Tools

[![cd](https://github.com/jonlabelle/docker-network-tools/actions/workflows/cd.yml/badge.svg)](https://github.com/jonlabelle/docker-network-tools/actions/workflows/cd.yml)
[![docker pulls](https://img.shields.io/docker/pulls/jonlabelle/network-tools?label=docker%20pulls)](https://hub.docker.com/r/jonlabelle/network-tools)
[![image size](https://img.shields.io/docker/image-size/jonlabelle/network-tools/latest?label=image%20size)](https://hub.docker.com/r/jonlabelle/network-tools/tags)

> A Docker image with various network tools pre-installed.

## Usage

To launch a Bash session in your terminal:

```bash
docker run --rm -it jonlabelle/network-tools
```

To launch a Bash session in your terminal on arm64:

```bash
docker run --rm -it --platform linux/arm64 jonlabelle/network-tools
```

To run a command directly and exit when finished (nmap in this case):

```bash
docker run --rm -it jonlabelle/network-tools nmap -v 10.0.10.0/24
```

> **NOTE:** To pull from [GitHub Container Registry], instead of [Docker Hub](https://hub.docker.com/r/jonlabelle/network-tools),
> replace **jonlabelle/network-tools** with **_ghcr.io/jonlabelle/network-tools_**.

## Included Tools

### Bandwidth

| Tool                                                      | Description                                      | Resources                                                                       |
| --------------------------------------------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------- |
| [`nethogs`](https://github.com/raboof/nethogs)            | Top-like monitor for network traffic.            | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/linux/nethogs.md) |
| [`nload`](https://github.com/rolandriegel/nload)          | Console network traffic and bandwidth monitor.   | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/nload.md)  |
| [`iperf`](https://sourceforge.net/projects/iperf2/)       | A tool to measure IP bandwidth using UDP or TCP. | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/iperf.md)  |
| [`speedtest-cli`](https://github.com/sivel/speedtest-cli) | CLI for testing bandwidth using speedtest.net.   | [usage](https://github.com/sivel/speedtest-cli#usage)                           |

### DNS

| Tool                                            | Description                                               | Resources                                                                       |
| ----------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `arpaname`                                      | Translate IP addresses to the corresponding ARPA names.   | -                                                                               |
| `ddns-confgen`                                  | DDNS key generation tool.                                 | -                                                                               |
| `delv`                                          | DNS lookup and validation utility.                        | -                                                                               |
| `dig`                                           | DNS lookup utility.                                       | -                                                                               |
| `dnsdomainname`                                 | Show the system's DNS domain name.                        | -                                                                               |
| `dnstap-read`                                   | Print dnstap data in human-readable form.                 | -                                                                               |
| `domainname`                                    | Show or set the system's NIS/YP domain name.              | -                                                                               |
| [`drill`](https://nlnetlabs.nl/projects/ldns/)  | DNS(SEC) query tool ala dig.                              | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/drill.md)  |
| `host`                                          | DNS lookup utility.                                       | -                                                                               |
| `hostname`                                      | Show or set the system's host name.                       | -                                                                               |
| [`libidn`](https://www.gnu.org/software/libidn) | Encode/decode library for internationalized domain names. | [examples](https://www.gnu.org/software/libidn/manual/libidn.html#Invoking-idn) |
| `mdig`                                          | DNS pipelined lookup utility.                             | -                                                                               |
| `named-checkzone`                               | Zone file validity checking or converting tool.           | -                                                                               |
| `named-compilezone`                             | Zone file validity checking or converting tool.           | -                                                                               |
| `named-journalprint`                            | Print zone journal in human-readable form.                | -                                                                               |
| `named-rrchecker`                               | Syntax checker for individual DNS resource records.       | -                                                                               |
| `nisdomainname`                                 | Show or set system's NIS/YP domain name.                  | -                                                                               |
| `nslookup`                                      | Query Internet name servers interactively.                | -                                                                               |
| `nsupdate`                                      | Dynamic DNS update utility.                               | -                                                                               |
| `rndc-confgen`                                  | RNDC key generation tool.                                 | -                                                                               |
| `tsig-keygen`                                   | DDNS key generation tool.                                 | -                                                                               |
| `ypdomainname`                                  | Show or set the system's NIS/YP domain name.              | -                                                                               |

### HTTP/Web

| Tool                                                                      | Description                                             | Resources                                                                        |
| ------------------------------------------------------------------------- | ------------------------------------------------------- | -------------------------------------------------------------------------------- |
| [`ab`](https://httpd.apache.org/docs/current/programs/ab.html)            | Apache HTTP server benchmarking tool.                   | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/ab.md)      |
| [`curl`](https://curl.haxx.se)                                            | Tool for transferring data with URLs.                   | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/curl.md)    |
| [`grpcurl`](https://github.com/fullstorydev/grpcurl)                      | Command-line tool for interacting with gRPC servers     | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/grpcurl.md) |
| [`jq`](https://stedolan.github.io/jq/)                                    | A lightweight and flexible command line JSON processor. | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/jq.md)      |
| [`oath-toolkit-oathtool`](https://www.nongnu.org/oath-toolkit/index.html) | Generate and validate one-time passwords.               | [man page](https://www.nongnu.org/oath-toolkit/man-oathtool.html)                |
| [`wget`](https://www.gnu.org/software/wget/wget.html)                     | A network utility to retrieve files from the web.       | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/wget.md)    |

### IP Routing

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

### IP and MAC address

| Tool                                                   | Description                                                | Resources                                                                         |
| ------------------------------------------------------ | ---------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `ifconfig`                                             | Configure a network interface.                             | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/ifconfig.md) |
| [`ipcalc`](https://jodies.de/ipcalc)                   | Network IP calculator.                                     | [man page](https://manned.org/ipcalc.1)                                           |
| `ipmaddr`                                              | Adds, deletes, and displays multicast addresses.           | -                                                                                 |
| [`macchanger`](https://github.com/alobbs/macchanger)   | View and manipulate the MAC address of network interfaces. | [man page](https://manned.org/macchanger.1)                                       |
| `nameif`                                               | Name network interfaces based on MAC addresses.            | -                                                                                 |
| [`nftables`](https://netfilter.org/projects/nftables/) | Netfilter tables userspace tools                           | [man page](https://www.netfilter.org/projects/nftables/manpage.html)              |
| `plipconfig`                                           | Fine tune PLIP device parameters.                          | -                                                                                 |
| `rarp`                                                 | Manipulate the system RARP table.                          | -                                                                                 |
| `slattach`                                             | Attach a network interface to a serial line.               | -                                                                                 |

### Packet analysis

| Tool                                         | Description                                   | Resources                                                                        |
| -------------------------------------------- | --------------------------------------------- | -------------------------------------------------------------------------------- |
| [`fping`](https://fping.org)                 | Search for network packets on an interface.   | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/fping.md)   |
| [`hping3`](https://github.com/antirez/hping) | A ping-like TCP/IP packet assembler/analyzer. | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/hping3.md)  |
| [`ngrep`](https://github.com/jpr5/ngrep/)    | Search for network packets on an interface.   | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/ngrep.md)   |
| [`tcpdump`](https://www.tcpdump.org)         | Dump and analyze traffic on a network.        | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/tcpdump.md) |
| [`tshark`](https://www.wireshark.org/)       | Network protocol analyzer (console version).  | [man page](https://www.wireshark.org/docs/man-pages/tshark.html)                 |

### Scanning and discovery

| Tool                                                              | Description                                        | Resources                                                                         |
| ----------------------------------------------------------------- | -------------------------------------------------- | --------------------------------------------------------------------------------- |
| [`arp-scan`](https://github.com/royhills/arp-scan)                | Address Resolution Protocol (ARP) packet scanner.  | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/arp.md-scan) |
| `arp`                                                             | Manipulate the system ARP cache.                   | -                                                                                 |
| `arping`                                                          | Send ARP REQUEST to a neighbor host.               | -                                                                                 |
| `clockdiff`                                                       | Measure clock difference between hosts.            | -                                                                                 |
| [`gping`](https://github.com/orf/gping)                           | Ping, but with a graph.                            | [usage](https://github.com/orf/gping#usage-saxophone)                             |
| [`masscan`](https://github.com/robertdavidgraham/masscan)         | Internet-scale port scanner.                       | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/masscan.md)  |
| [`netstat`](https://man7.org/linux/man-pages/man8/netstat.8.html) | Displays network-related information.              | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/netstat.md)  |
| `ninfod`                                                          | Respond to IPv6 Node Information Queries.          | -                                                                                 |
| [`nmap`](https://nmap.org/)                                       | Network Security Scanner.                          | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/nmap.md)     |
| [`nping`](https://nmap.org/nping/)                                | Network packet generation tool/ping utility.       | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/nping.md)    |
| `ping6`                                                           | Send IP6 ICMP ECHO_REQUEST to network hosts.       | -                                                                                 |
| `ping`                                                            | Send IP4 ICMP ECHO_REQUEST to network hosts.       | -                                                                                 |
| `rarpd`                                                           | Reverse Address Resolution Protocol (RARP) daemon. | -                                                                                 |
| `rdisc`                                                           | Network router discovery daemon.                   | -                                                                                 |

### Transmission and communication

| Tool                                                       | Description                                        | Resources                                                                        |
| ---------------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------------------------------------- |
| `iptunnel`                                                 | Creates, deletes, and displays configured tunnels. | -                                                                                |
| [`kcat`](https://github.com/edenhill/kcat)                 | Non-JVM Apache Kafka producer and consumer.        | [examples](https://github.com/edenhill/kcat#examples)                            |
| [`netcat`](https://packages.debian.org/sid/netcat-openbsd) | The TCP/IP swiss army knife (OpenBSD variant).     | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/netcat.md)  |
| [`openssl`](https://www.openssl.org/)                      | Toolkit for Transport Layer Security (TLS).        | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/openssl.md) |
| [`socat`](http://www.dest-unreach.org/socat/)              | Multipurpose relay for binary protocols.           | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/socat.md)   |
| [`ssh`](https://www.openssh.com/portable.html)             | OpenBSD's SSH client.                              | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/ssh.md)     |
| [`telnet`](https://www.gnu.org/software/inetutils/)        | Telnet client from GNU network utilities           | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/telnet.md)  |
| `tftpd`                                                    | IPv4 Trivial File Transfer Protocol client.        | -                                                                                |

### Tracing

| Tool                                                    | Description                                                        | Resources                                                                             |
| ------------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------------------- |
| [`mtr`](https://www.bitwizard.nl/mtr/)                  | Full screen ncurses traceroute tool.                               | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/mtr.md)          |
| [`tcptraceroute`](https://github.com/mct/tcptraceroute) | Display route path using TCP probes.                               | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/linux/tcptraceroute.md) |
| `tracepath6`                                            | Traces path to a IP6 network host discovering MTU along this path. | -                                                                                     |
| `tracepath`                                             | Traces path to a IP4 network host discovering MTU along this path. | -                                                                                     |
| `traceroute6`                                           | Print the route packets trace to IP6 network host.                 | -                                                                                     |

### Additional tools

| Tool                                              | Description                                                   | Resources                                                                         |
| ------------------------------------------------- | ------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| [`envsubst`](https://github.com/kaniini/envsubst) | Perform variable substitutions on input.                      | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/envsubst.md) |
| `find`                                            | Search for files in a directory hierarchy.                    | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/find.md)     |
| [`git`](https://www.git-scm.com/)                 | Distribute d version control system.                          | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/git.md)      |
| `free`                                            | Report the amount of free and used memory in the system.      | -                                                                                 |
| `kill`                                            | Send a signal to a process based on PID.                      | -                                                                                 |
| `locate`                                          | List files in databases that match a pattern.                 | [man page](https://man7.org/linux/man-pages/man1/locate.1.html)                   |
| `pgrep`                                           | List processes based on name or other attributes.             | -                                                                                 |
| `pkill`                                           | Send a signal to a process based on name or other attributes. | -                                                                                 |
| `pmap`                                            | Report memory map of a process.                               | -                                                                                 |
| `ps`                                              | Report information of processes.                              | -                                                                                 |
| `pwdx`                                            | Report current directory of a process.                        | -                                                                                 |
| `skill`                                           | Obsolete version of pgrep/pkill.                              | -                                                                                 |
| `slabtop`                                         | Display kernel slab cache information in real time.           | -                                                                                 |
| `snice`                                           | Renice a process.                                             | -                                                                                 |
| `sysctl`                                          | Read or Write kernel parameters at run-time.                  | -                                                                                 |
| `tload`                                           | Graphical representation of system load average.              | -                                                                                 |
| `top`                                             | Dynamic real-time view of running processes.                  | -                                                                                 |
| `updatedb`                                        | Update a file name database.                                  | [man page](https://man7.org/linux/man-pages/man1/updatedb.1.html)                 |
| `uptime`                                          | Display how long the system has been running.                 | -                                                                                 |
| `vmstat`                                          | Report virtual memory statistics.                             | -                                                                                 |
| `w`                                               | Report logged in users and what they are doing.               | -                                                                                 |
| `watch`                                           | Execute a program periodically, showing output full-screen.   | -                                                                                 |
| `xargs`                                           | Build and execute command lines from standard input.          | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/xargs.md)    |

## Related

[jonlabelle/docker-nmap](https://github.com/jonlabelle/docker-nmap). Minimal Docker image with Nmap Network Security Scanner pre-installed.

## License

[MIT License](https://github.com/jonlabelle/docker-network-tools/blob/main/LICENSE.txt)

[github container registry]: https://github.com/users/jonlabelle/packages/container/package/network-tools
