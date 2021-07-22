SHELL := /bin/bash

NAME := network-tools
TAG := dev

IMAGE_NAME = $(NAME):$(TAG)

default: build
all: build run

.PHONY: build
build:
	@docker build --tag "$(IMAGE_NAME)" .

.PHONY: run
run:
	@docker run --name "$(NAME)" --rm --interactive --tty "$(IMAGE_NAME)"

.PHONY: clean
clean:
	@docker rmi "$(IMAGE_NAME)"
