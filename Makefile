NAME := network-tools
ARM_NAME := network-tools-arm

TAG := dev

IMAGE_NAME = $(NAME):$(TAG)
ARM_IMAGE_NAME = $(ARM_NAME):$(TAG)

.PHONY: default
default: help

.PHONY: all
all: ## Lints the Dockerfile and runs the container a terminal session
	$(MAKE) lint
	$(MAKE) run

.PHONY: lint
lint: ## Lints the Dockerfile
	@docker run --rm --interactive --env "HADOLINT_IGNORE=DL3013,DL3018" hadolint/hadolint < Dockerfile

build: ## Builds a local dev image (network-tools:dev)
	@docker build --tag "$(IMAGE_NAME)" .

build-arm: ## Builds the linux/arm64 image (network-tools-arm:dev)
	@docker buildx create --use
	@docker buildx build --platform linux/arm64 --output type=docker --tag "$(ARM_IMAGE_NAME)" .

.PHONY: run
run: ## Runs the container a terminal session
	$(MAKE) build
	@docker run --name "$(NAME)" --rm --interactive --tty "$(IMAGE_NAME)"

.PHONY: run-arm
run-arm: ## Runs the linux/arm64 container a terminal session
	$(MAKE) build-arm
	@docker run --name "$(ARM_NAME)" --platform linux/arm64 --rm --interactive --tty "$(ARM_IMAGE_NAME)"

.PHONY: clean
clean: ## Removes the built images
	@docker rmi "$(IMAGE_NAME)"; true
	@docker rmi "$(ARM_IMAGE_NAME)"; true
	@docker rmi hadolint/hadolint; true
	@docker buildx rm --all-inactive --force; true
	@docker buildx prune --force; true

.PHONY: help
help: ## Shows this help message
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST)  | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
