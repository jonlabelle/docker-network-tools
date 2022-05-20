NAME := network-tools
TAG := dev

IMAGE_NAME = $(NAME):$(TAG)

.PHONY: default
default: help

.PHONY: all
all: lint build run

.PHONY: lint
lint: ## Lints the Dockerfile
	@docker run --rm --interactive --env "HADOLINT_IGNORE=DL3013,DL3018" hadolint/hadolint < Dockerfile

build: ## Builds a local dev image (network-tools:dev)
	@docker build --tag "$(IMAGE_NAME)" .

.PHONY: run
run: ## Runs the container a terminal session
	@docker build --tag "$(IMAGE_NAME)" .
	@docker run --name "$(NAME)" --rm --interactive --tty "$(IMAGE_NAME)"

.PHONY: clean
clean: ## Removes the dev and linting images
	@docker rmi "$(IMAGE_NAME)"
	@docker rmi hadolint/hadolint

.PHONY: help
help: ## Shows this help message
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST)  | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
