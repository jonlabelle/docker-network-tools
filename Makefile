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

build-arm: ## Builds the linux/arm64 version
	@docker buildx create --use
	@docker buildx build --platform linux/arm64 --output type=docker --tag network-tools-arm .

.PHONY: run
run: ## Runs the container a terminal session
	@docker run --name "$(NAME)" --rm --interactive --tty "$(IMAGE_NAME)"

.PHONY: run-arm
run-arm: ## Runs the linux/arm64 container a terminal session
	@docker run --name "$(NAME)" --platform linux/arm64 --rm --interactive --tty network-tools-arm

.PHONY: clean
clean: ## Removes the built images
	@docker rmi "$(IMAGE_NAME)"; true
	@docker rmi network-tools-arm; true
	@docker rmi hadolint/hadolint; true
	@docker buildx rm --all-inactive --force; true
	@docker buildx prune --force; true

.PHONY: help
help: ## Shows this help message
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST)  | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
