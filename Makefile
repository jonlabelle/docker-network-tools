SHELL := /bin/sh

NAME := network-tools
TAG := dev

IMAGE_NAME = $(NAME):$(TAG)

default: build
all: lint build run

build: ## Build the dev image
	@docker build --no-cache --tag "$(IMAGE_NAME)" .

.PHONY: lint
lint: ## Lint the Dockerfile
	@docker run --rm -i --env "HADOLINT_IGNORE=DL3013,DL3018" hadolint/hadolint < Dockerfile

.PHONY: run
run: ## Run the container a terminal session
	@docker run --name "$(NAME)" --rm --interactive --tty "$(IMAGE_NAME)"

.PHONY: clean
clean: ## Remove the dev and linting images
	@docker rmi "$(IMAGE_NAME)"
	@docker rmi hadolint/hadolint

.PHONY: help
help: ## Show this help message
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST)  | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
