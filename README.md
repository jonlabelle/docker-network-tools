# Docker Network Tools

[![cd](https://github.com/jonlabelle/docker-network-tools/actions/workflows/cd.yml/badge.svg)](https://github.com/jonlabelle/docker-network-tools/actions/workflows/cd.yml)
[![Test Prune Script](https://github.com/jonlabelle/docker-network-tools/actions/workflows/test-prune-script.yml/badge.svg)](https://github.com/jonlabelle/docker-network-tools/actions/workflows/test-prune-script.yml)
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

> **NOTE:** To pull from [GitHub Container Registry](https://github.com/jonlabelle/docker-network-tools/pkgs/container/network-tools), instead of [Docker Hub](https://hub.docker.com/r/jonlabelle/network-tools),
> replace **jonlabelle/network-tools** with **_ghcr.io/jonlabelle/network-tools_**.

## Included tools

### Bandwidth

Tools for measuring network bandwidth and traffic.

| Tool                                                      | Description                                      | Resources                                                                       |
| --------------------------------------------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------- |
| [`nethogs`](https://github.com/raboof/nethogs)            | Top-like monitor for network traffic.            | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/linux/nethogs.md) |
| [`nload`](https://github.com/rolandriegel/nload)          | Console network traffic and bandwidth monitor.   | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/nload.md)  |
| [`iperf`](https://sourceforge.net/projects/iperf2/)       | A tool to measure IP bandwidth using UDP or TCP. | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/iperf.md)  |
| [`speedtest-cli`](https://github.com/sivel/speedtest-cli) | CLI for testing bandwidth using speedtest.net.   | [usage](https://github.com/sivel/speedtest-cli#usage)                           |

### DNS

Tools for querying and managing DNS.

| Tool                                                                          | Description                                               | Resources                                                                         |
| ----------------------------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------------------------------- |
| [`arpaname`](https://manpages.ubuntu.com/manpages/jammy/man1/arpaname.1.html) | Translate IP addresses to the corresponding ARPA names.   | [man page](https://manpages.ubuntu.com/manpages/jammy/man1/arpaname.1.html)       |
| [`ddns-confgen`](https://linux.die.net/man/8/ddns-confgen)                    | DDNS key generation tool.                                 | [man page](https://linux.die.net/man/8/ddns-confgen)                              |
| [`delv`](https://linux.die.net/man/1/delv)                                    | DNS lookup and validation utility.                        | [man page](https://linux.die.net/man/1/delv)                                      |
| [`dig`](https://linux.die.net/man/1/dig)                                      | DNS lookup utility.                                       | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/dig.md)      |
| [`dnsdomainname`](https://man7.org/linux/man-pages/man1/dnsdomainname.1.html) | Show the system's DNS domain name.                        | [man page](https://man7.org/linux/man-pages/man1/dnsdomainname.1.html)            |
| [`dnstap-read`](https://github.com/dnstap/dnstap.read)                        | Print dnstap data in human-readable form.                 | [README](https://github.com/dnstap/dnstap.read/blob/master/README.md)             |
| [`domainname`](https://man7.org/linux/man-pages/man1/domainname.1.html)       | Show or set the system's NIS/YP domain name.              | [man page](https://man7.org/linux/man-pages/man1/domainname.1.html)               |
| [`drill`](https://nlnetlabs.nl/projects/ldns/)                                | DNS(SEC) query tool ala dig.                              | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/drill.md)    |
| [`host`](https://man7.org/linux/man-pages/man1/host.1.html)                   | DNS lookup utility.                                       | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/host.md)     |
| [`hostname`](https://man7.org/linux/man-pages/man1/hostname.1.html)           | Show or set the system's host name.                       | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/hostname.md) |
| [`libidn`](https://www.gnu.org/software/libidn)                               | Encode/decode library for internationalized domain names. | [examples](https://www.gnu.org/software/libidn/manual/libidn.html#Invoking-idn)   |
| [`mdig`](https://linux.die.net/man/1/mdig)                                    | DNS pipelined lookup utility.                             | [man page](https://linux.die.net/man/1/mdig)                                      |
| [`named-checkzone`](https://linux.die.net/man/8/named-checkzone)              | Zone file validity checking or converting tool.           | [man page](https://linux.die.net/man/8/named-checkzone)                           |
| [`named-compilezone`](https://linux.die.net/man/8/named-compilezone)          | Zone file validity checking or converting tool.           | [man page](https://linux.die.net/man/8/named-compilezone)                         |
| [`named-journalprint`](https://linux.die.net/man/8/named-journalprint)        | Print zone journal in human-readable form.                | [man page](https://linux.die.net/man/8/named-journalprint)                        |
| [`named-rrchecker`](https://linux.die.net/man/8/named-rrchecker)              | Syntax checker for individual DNS resource records.       | [man page](https://linux.die.net/man/8/named-rrchecker)                           |
| [`nisdomainname`](https://man7.org/linux/man-pages/man1/nisdomainname.1.html) | Show or set system's NIS/YP domain name.                  | [man page](https://man7.org/linux/man-pages/man1/nisdomainname.1.html)            |
| [`nslookup`](https://linux.die.net/man/1/nslookup)                            | Query Internet name servers interactively.                | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/nslookup.md) |
| [`nsupdate`](https://linux.die.net/man/1/nsupdate)                            | Dynamic DNS update utility.                               | [man page](https://linux.die.net/man/1/nsupdate)                                  |
| [`rndc-confgen`](https://linux.die.net/man/8/rndc-confgen)                    | RNDC key generation tool.                                 | [man page](https://linux.die.net/man/8/rndc-confgen)                              |
| [`tsig-keygen`](https://linux.die.net/man/1/tsig-keygen)                      | DDNS key generation tool.                                 | [man page](https://linux.die.net/man/1/tsig-keygen)                               |
| [`ypdomainname`](https://man7.org/linux/man-pages/man1/ypdomainname.1.html)   | Show or set the system's NIS/YP domain name.              | [man page](https://man7.org/linux/man-pages/man1/ypdomainname.1.html)             |

### HTTP

Tools for interacting with HTTP servers.

| Tool                                                                      | Description                                             | Resources                                                                        |
| ------------------------------------------------------------------------- | ------------------------------------------------------- | -------------------------------------------------------------------------------- |
| [`ab`](https://httpd.apache.org/docs/current/programs/ab.html)            | Apache HTTP server benchmarking tool.                   | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/ab.md)      |
| [`curl`](https://curl.haxx.se)                                            | Tool for transferring data with URLs.                   | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/curl.md)    |
| [`grpcurl`](https://github.com/fullstorydev/grpcurl)                      | Command-line tool for interacting with gRPC servers     | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/grpcurl.md) |
| [`jq`](https://stedolan.github.io/jq/)                                    | A lightweight and flexible command line JSON processor. | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/jq.md)      |
| [`oath-toolkit-oathtool`](https://www.nongnu.org/oath-toolkit/index.html) | Generate and validate one-time passwords.               | [man page](https://www.nongnu.org/oath-toolkit/man-oathtool.html)                |
| [`wget`](https://www.gnu.org/software/wget/wget.html)                     | A network utility to retrieve files from the web.       | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/wget.md)    |

### IP routing

Tools for managing IP routing tables.

| Tool                                                            | Description                                                    | Resources                                                        |
| --------------------------------------------------------------- | -------------------------------------------------------------- | ---------------------------------------------------------------- |
| [`bridge`](https://man7.org/linux/man-pages/man8/bridge.8.html) | Show / manipulate bridge addresses and devices.                | [man page](https://man7.org/linux/man-pages/man8/bridge.8.html)  |
| [`ctstat`](https://man7.org/linux/man-pages/man8/ctstat.8.html) | Unified linux network statistics.                              | [man page](https://man7.org/linux/man-pages/man8/ctstat.8.html)  |
| [`genl`](https://man7.org/linux/man-pages/man8/genl.8.html)     | Generic netlink utility frontend.                              | [man page](https://man7.org/linux/man-pages/man8/genl.8.html)    |
| [`ifcfg`](https://linux.die.net/man/8/ifcfg)                    | Simplistic script which replaces ifconfig IP management.       | [man page](https://linux.die.net/man/8/ifcfg)                    |
| [`ifstat`](https://linux.die.net/man/1/ifstat)                  | Handy utility to read network interface statistics.            | [man page](https://linux.die.net/man/1/ifstat)                   |
| [`lnstat`](https://man7.org/linux/man-pages/man8/lnstat.8.html) | Unified linux network statistics.                              | [man page](https://man7.org/linux/man-pages/man8/lnstat.8.html)  |
| [`nstat`](https://man7.org/linux/man-pages/man8/nstat.8.html)   | Network statistics tools.                                      | [man page](https://man7.org/linux/man-pages/man8/nstat.8.html)   |
| [`route`](https://man7.org/linux/man-pages/man8/route.8.html)   | Show / manipulate the IP routing table.                        | [man page](https://man7.org/linux/man-pages/man8/route.8.html)   |
| [`routef`](https://linux.die.net/man/8/routef)                  | Flush network routes.                                          | [man page](https://linux.die.net/man/8/routef)                   |
| [`routel`](https://github.com/routel/routel)                    | List routes with pretty output format.                         | [README](https://github.com/routel/routel/blob/master/README.md) |
| [`rtacct`](https://man7.org/linux/man-pages/man8/rtacct.8.html) | Monitor kernel SNMP counters and network interface statistics. | [man page](https://man7.org/linux/man-pages/man8/rtacct.8.html)  |
| [`rtmon`](https://man7.org/linux/man-pages/man8/rtmon.8.html)   | Listens to and monitors RTnetlink.                             | [man page](https://man7.org/linux/man-pages/man8/rtmon.8.html)   |
| [`rtpr`](https://linux.die.net/man/1/rtpr)                      | Replace backslashes with newlines.                             | [man page](https://linux.die.net/man/1/rtpr)                     |
| [`rtstat`](https://man7.org/linux/man-pages/man8/rtstat.8.html) | Unified linux network statistics.                              | [man page](https://man7.org/linux/man-pages/man8/rtstat.8.html)  |

### Interface and address management

Tools for configuring network interfaces and addresses.

| Tool                                                                    | Description                                                | Resources                                                                         |
| ----------------------------------------------------------------------- | ---------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `ifconfig`                                                              | Configure a network interface.                             | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/ifconfig.md) |
| [`ipcalc`](https://jodies.de/ipcalc)                                    | Network IP calculator.                                     | [man page](https://manned.org/ipcalc.1)                                           |
| [`ipmaddr`](https://man7.org/linux/man-pages/man8/ipmaddr.8.html)       | Adds, deletes, and displays multicast addresses.           | [man page](https://man7.org/linux/man-pages/man8/ipmaddr.8.html)                  |
| [`macchanger`](https://github.com/alobbs/macchanger)                    | View and manipulate the MAC address of network interfaces. | [man page](https://manned.org/macchanger.1)                                       |
| [`nameif`](https://linux.die.net/man/8/nameif)                          | Name network interfaces based on MAC addresses.            | [man page](https://linux.die.net/man/8/nameif)                                    |
| [`nftables`](https://netfilter.org/projects/nftables/)                  | Netfilter tables userspace tools                           | [man page](https://www.netfilter.org/projects/nftables/manpage.html)              |
| [`plipconfig`](https://man7.org/linux/man-pages/man8/plipconfig.8.html) | Fine tune PLIP device parameters.                          | [man page](https://man7.org/linux/man-pages/man8/plipconfig.8.html)               |
| [`rarp`](https://man7.org/linux/man-pages/man8/rarp.8.html)             | Manipulate the system RARP table.                          | [man page](https://man7.org/linux/man-pages/man8/rarp.8.html)                     |
| [`slattach`](https://man7.org/linux/man-pages/man8/slattach.8.html)     | Attach a network interface to a serial line.               | [man page](https://man7.org/linux/man-pages/man8/slattach.8.html)                 |

### Packet analysis

Tools for capturing and analyzing network packets.

| Tool                                         | Description                                   | Resources                                                                        |
| -------------------------------------------- | --------------------------------------------- | -------------------------------------------------------------------------------- |
| [`fping`](https://fping.org)                 | Search for network packets on an interface.   | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/fping.md)   |
| [`hping3`](https://github.com/antirez/hping) | A ping-like TCP/IP packet assembler/analyzer. | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/hping3.md)  |
| [`ngrep`](https://github.com/jpr5/ngrep/)    | Search for network packets on an interface.   | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/ngrep.md)   |
| [`tcpdump`](https://www.tcpdump.org)         | Dump and analyze traffic on a network.        | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/tcpdump.md) |
| [`tshark`](https://www.wireshark.org/)       | Network protocol analyzer (console version).  | [man page](https://www.wireshark.org/docs/man-pages/tshark.html)                 |

### Discovery and scanning

Tools for discovering hosts and scanning ports.

| Tool                                                                  | Description                                        | Resources                                                                         |
| --------------------------------------------------------------------- | -------------------------------------------------- | --------------------------------------------------------------------------------- |
| [`arp-scan`](https://github.com/royhills/arp-scan)                    | Address Resolution Protocol (ARP) packet scanner.  | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/arp.md-scan) |
| [`arp`](https://man7.org/linux/man-pages/man8/arp.8.html)             | Manipulate the system ARP cache.                   | [man page](https://man7.org/linux/man-pages/man8/arp.8.html)                      |
| [`arping`](https://linux.die.net/man/8/arping)                        | Send ARP REQUEST to a neighbor host.               | [man page](https://linux.die.net/man/8/arping)                                    |
| `clockdiff`                                                           | Measure clock difference between hosts.            | -                                                                                 |
| [`clockdiff`](https://man7.org/linux/man-pages/man8/clockdiff.8.html) | Measure clock difference between hosts.            | [man page](https://man7.org/linux/man-pages/man8/clockdiff.8.html)                |
| [`gping`](https://github.com/orf/gping)                               | Ping, but with a graph.                            | [usage](https://github.com/orf/gping#usage-saxophone)                             |
| [`masscan`](https://github.com/robertdavidgraham/masscan)             | Internet-scale port scanner.                       | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/masscan.md)  |
| [`netstat`](https://man7.org/linux/man-pages/man8/netstat.8.html)     | Displays network-related information.              | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/netstat.md)  |
| [`ninfod`](https://www.systutorials.com/docs/linux/man/8-ninfod/)     | Respond to IPv6 Node Information Queries.          | [man page](https://www.systutorials.com/docs/linux/man/8-ninfod/)                 |
| [`nmap`](https://nmap.org/)                                           | Network Security Scanner.                          | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/nmap.md)     |
| [`nping`](https://nmap.org/nping/)                                    | Network packet generation tool/ping utility.       | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/nping.md)    |
| `ping6`                                                               | Send IP6 ICMP ECHO_REQUEST to network hosts.       | -                                                                                 |
| `ping`                                                                | Send IP4 ICMP ECHO_REQUEST to network hosts.       | -                                                                                 |
| [`rarpd`](https://man7.org/linux/man-pages/man8/rarpd.8.html)         | Reverse Address Resolution Protocol (RARP) daemon. | [man page](https://man7.org/linux/man-pages/man8/rarpd.8.html)                    |
| [`rdisc`](https://man7.org/linux/man-pages/man8/rdisc.8.html)         | Network router discovery daemon.                   | [man page](https://man7.org/linux/man-pages/man8/rdisc.8.html)                    |

### Transmission and communication

Tools for sending and receiving data over the network.

| Tool                                                                            | Description                                        | Resources                                                                          |
| ------------------------------------------------------------------------------- | -------------------------------------------------- | ---------------------------------------------------------------------------------- |
| [`iptunnel`](https://www.kernel.org/doc/Documentation/networking/ip-tunnel.txt) | Creates, deletes, and displays configured tunnels. | [documentation](https://www.kernel.org/doc/Documentation/networking/ip-tunnel.txt) |
| [`kcat`](https://github.com/edenhill/kcat)                                      | Non-JVM Apache Kafka producer and consumer.        | [examples](https://github.com/edenhill/kcat#examples)                              |
| [`netcat`](https://packages.debian.org/sid/netcat-openbsd)                      | The TCP/IP swiss army knife (OpenBSD variant).     | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/netcat.md)    |
| [`openssl`](https://www.openssl.org/)                                           | Toolkit for Transport Layer Security (TLS).        | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/openssl.md)   |
| [`socat`](http://www.dest-unreach.org/socat/)                                   | Multipurpose relay for binary protocols.           | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/socat.md)     |
| [`ssh`](https://www.openssh.com/portable.html)                                  | OpenBSD's SSH client.                              | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/ssh.md)       |
| [`telnet`](https://www.gnu.org/software/inetutils/)                             | Telnet client from GNU network utilities           | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/telnet.md)    |
| `tftpd`                                                                         | IPv4 Trivial File Transfer Protocol client.        | -                                                                                  |

### Tracing

Tools for tracing network paths.

| Tool                                                    | Description                                                        | Resources                                                                             |
| ------------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------------------- |
| [`mtr`](https://www.bitwizard.nl/mtr/)                  | Full screen ncurses traceroute tool.                               | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/common/mtr.md)          |
| [`tcptraceroute`](https://github.com/mct/tcptraceroute) | Display route path using TCP probes.                               | [examples](https://github.com/tldr-pages/tldr/blob/main/pages/linux/tcptraceroute.md) |
| `tracepath6`                                            | Traces path to a IP6 network host discovering MTU along this path. | -                                                                                     |
| `tracepath`                                             | Traces path to a IP4 network host discovering MTU along this path. | -                                                                                     |
| `traceroute6`                                           | Print the route packets trace to IP6 network host.                 | -                                                                                     |

### Additional tools

Miscellaneous tools available in the image.

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

## Automated Builds

This image is automatically built and published:

- **Weekly**: Every Sunday at 1:43 AM UTC to ensure the latest security updates and package versions are included. This weekly schedule ensures that even if no code changes are made, the base Alpine Linux image and all installed network tools receive the latest security patches and updates.
- **On commits**: Whenever changes are pushed to the main branch, ensuring immediate availability of new features or fixes
- **Manual**: Can be triggered manually via GitHub Actions workflow dispatch for emergency updates or testing

Images are published to both [Docker Hub](https://hub.docker.com/r/jonlabelle/network-tools) and [GitHub Container Registry](https://github.com/jonlabelle/docker-network-tools/pkgs/container/network-tools) with multi-architecture support (linux/amd64 and linux/arm64).

To keep storage manageable, old untagged images are automatically pruned after 7 days during the build process. This cleanup process runs against both registries and removes intermediate build artifacts while preserving all tagged releases.

The automated image cleanup is handled by a custom Python script in `scripts/prune/` which is thoroughly tested with automated CI/CD workflows that run whenever the script is modified.

## Related

[jonlabelle/docker-nmap](https://github.com/jonlabelle/docker-nmap). Minimal Docker image with Nmap Network Security Scanner pre-installed.

## License

[MIT License](https://github.com/jonlabelle/docker-network-tools/blob/main/LICENSE.txt)
