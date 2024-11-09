NAME := network-tools
ARM_NAME := network-tools-arm

TAG := dev

IMAGE_NAME = $(NAME):$(TAG)
ARM_IMAGE_NAME = $(ARM_NAME):$(TAG)

# Determine if docker, podman, or nerdctl is installed
DOCKER := $(shell command -v docker 2> /dev/null || command -v podman 2> /dev/null || command -v nerdctl 2> /dev/null)

.PHONY: default
default: help

.PHONY: all
all: ## Lints the Dockerfile and runs the container in a terminal session
	$(MAKE) lint
	$(MAKE) run

.PHONY: lint
lint: ## Lints the Dockerfile
	@$(DOCKER) run --rm --interactive --env "HADOLINT_IGNORE=DL3013,DL3018" docker.io/hadolint/hadolint:latest < Dockerfile

build: ## Builds a local dev image (network-tools:dev)
	@$(DOCKER) build --tag "$(IMAGE_NAME)" .

build-arm: ## Builds the linux/arm64 image (network-tools-arm:dev)
	@$(DOCKER) buildx create --use
	@$(DOCKER) buildx build --platform linux/arm64 --output type=docker --tag "$(ARM_IMAGE_NAME)" .

.PHONY: run
run: ## Runs the container in a terminal session
	$(MAKE) build
	@$(DOCKER) run --name "$(NAME)" --rm --interactive --tty "$(IMAGE_NAME)"

.PHONY: run-arm
run-arm: ## Runs the linux/arm64 container in a terminal session
	$(MAKE) build-arm
	@$(DOCKER) run --name "$(ARM_NAME)" --platform linux/arm64 --rm --interactive --tty "$(ARM_IMAGE_NAME)"

.PHONY: clean
clean: ## Removes the built images
	@$(DOCKER) rmi "$(IMAGE_NAME)"; true
	@$(DOCKER) rmi "$(ARM_IMAGE_NAME)"; true
	@$(DOCKER) rmi hadolint/hadolint; true
	@$(DOCKER) buildx rm --all-inactive --force; true
	@$(DOCKER) buildx prune --force; true

.PHONY: help
help: ## Shows this help message
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST)  | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
