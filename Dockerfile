FROM alpine:edge

LABEL maintainer="Jon LaBelle <contact@jonlabelle.com>" \
      description="A Docker image with various network tools pre-installed." \
      org.label-schema.url="https://hub.docker.com/r/jonlabelle/network-tools" \
      org.label-schema.vcs-url="https://github.com/jonlabelle/docker-network-tools" \
      org.label-schema.vcs-type="Git"

RUN apk -U upgrade && apk add --no-cache \
    bash \
    procps \
    bash-completion \
    ca-certificates \
    openssl \
    libressl \
    socat \
    net-tools \
    openssh-client \
    coreutils \
    findutils \
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
    drill \
    libidn \
    oath-toolkit-oathtool \
    curl \
    git \
    && rm -rf /var/cache/apk/* \
    && echo 'export PS1="[docker@network-tools]\$ "' >> /root/.bash_profile

CMD ["/bin/bash", "--login", "-i"]
