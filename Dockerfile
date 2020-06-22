FROM alpine:latest

LABEL maintainer="Jon LaBelle <contact@jonlabelle.com>" \
      description="Minimal Docker image with various network tools pre-installed." \
      org.label-schema.url="https://hub.docker.com/r/jonlabelle/network-tools" \
      org.label-schema.vcs-url="https://github.com/jonlabelle/docker-network-tools" \
      org.label-schema.vcs-type="Git"

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
    jq \
    ipcalc \
    && rm -rf /var/cache/apk/*

CMD ["/bin/sh"]
