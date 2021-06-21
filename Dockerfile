# syntax=docker/dockerfile:1
FROM alpine:edge

LABEL maintainer="Jon LaBelle <https://jonlabelle.com>" \
      description="A Docker image with various network tools pre-installed."

RUN apk -U upgrade && apk add --no-cache \
    apache2-utils \
    bash \
    bash-completion \
    bind-tools \
    ca-certificates \
    coreutils \
    curl \
    drill \
    findutils \
    fping \
    git \
    ipcalc \
    iperf \
    iproute2 \
    iputils \
    jq \
    libidn \
    macchanger \
    mtr \
    net-tools \
    netcat-openbsd \
    ngrep \
    nload \
    nmap \
    nmap-scripts \
    oath-toolkit-oathtool \
    openssh-client \
    openssl \
    procps \
    socat \
    tcpdump \
    tshark \
    wget \
    python3 \
    && python3 -m ensurepip \
    && pip3 install --upgrade pip \
    && python3 -m pip install requests \
    && rm -rf /var/cache/apk/* \
    && echo 'export PS1="[docker@network-tools]\$ "' >> /root/.bash_profile

COPY run_tests.sh .

CMD ["/bin/bash", "--login", "-i"]
