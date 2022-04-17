SHELL := /bin/sh

NAME := network-tools
TAG := dev

IMAGE_NAME = $(NAME):$(TAG)

default: build
all: lint build run

.PHONY: lint
lint:
	@docker run --rm -i --env "HADOLINT_IGNORE=DL3013,DL3018" hadolint/hadolint < Dockerfile

.PHONY: build
build:
	@docker build --no-cache --tag "$(IMAGE_NAME)" .

.PHONY: run
run:
	@docker run --name "$(NAME)" --rm --interactive --tty "$(IMAGE_NAME)"

.PHONY: clean
clean:
	@docker rmi "$(IMAGE_NAME)"
	@docker rmi hadolint/hadolint
