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

.PHONY: test
test:
	@docker-compose --file docker-compose.test.yml up --build
	@docker-compose --file docker-compose.test.yml down

.PHONY: clean
clean:
	@docker rmi "$(IMAGE_NAME)"
