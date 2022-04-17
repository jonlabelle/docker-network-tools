ARG ALPINE_TAG=latest
FROM alpine:${ALPINE_TAG}

LABEL maintainer="Jon LaBelle <https://jonlabelle.com>" \
    description="A Docker image with various network tools pre-installed."

RUN apk -U upgrade \
    && apk add --no-cache \
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
        masscan \
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
    && apk add --repository=http://dl-cdn.alpinelinux.org/alpine/edge/testing/ --no-cache \
        arp-scan \
        envsubst \
        hping3 \
    && python3 -m ensurepip \
    && pip3 install --no-cache-dir --disable-pip-version-check --upgrade pip \
    && python3 -m pip install --no-cache-dir requests \
    && rm -rf /var/cache/apk/* \
    && echo 'export PS1="[docker@network-tools]\$ "' >> /root/.bash_profile

CMD ["/bin/bash", "--login"]
