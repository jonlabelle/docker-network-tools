FROM alpine:latest

LABEL maintainer="contact@jonlabelle.com"
LABEL description="Minimal Docker image with various network tools pre-installed."

RUN apk -U upgrade && apk add --no-cache \
    ca-certificates \
    openssl \
    curl \
    net-tools \
    macchanger \
    fping \
    ngrep \
    nmap nmap-scripts \
    netcat-openbsd \
    bind-tools \
    nload \
    tcpdump \
    wget \
    && rm -rf /var/cache/apk/*

CMD ["/bin/sh"]
