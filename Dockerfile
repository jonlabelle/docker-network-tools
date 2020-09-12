FROM alpine:latest

LABEL maintainer="Jon LaBelle <contact@jonlabelle.com>" \
      description="Minimal Docker image with various network tools pre-installed." \
      org.label-schema.url="https://hub.docker.com/r/jonlabelle/network-tools" \
      org.label-schema.vcs-url="https://github.com/jonlabelle/docker-network-tools" \
      org.label-schema.vcs-type="Git"

RUN apk -U upgrade && apk add --no-cache \
    bash \
    bash-completion \
    ca-certificates \
    openssl \
    libressl \
    curl \
    socat \
    net-tools \
    openssh-client \
    coreutils \
    iputils \
    macchanger \
    fping \
    ngrep \
    nmap nmap-scripts \
    netcat-openbsd \
    bind-tools \
    nload \
    tcpdump \
    wget \
    jq \
    ipcalc \
    iperf \
    tshark \
    oath-toolkit-oathtool \
    && rm -rf /var/cache/apk/* \
    && echo 'export PS1="[docker@network-tools]\$ "' >> /root/.bash_profile

CMD ["/bin/bash", "--login", "-i"]
