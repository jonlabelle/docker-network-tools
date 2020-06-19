FROM alpine:latest
MAINTAINER Jon LaBelle <contact@jonlabelle.com>

RUN apk -U upgrade && apk add --no-cache \
    ca-certificates \
    openssl \
    net-tools \
    macchanger \
    fping \
    ngrep \
    nmap nmap-scripts \
    netcat-openbsd && \
    rm -rf /var/cache/apk/*

CMD ["/bin/sh"]
