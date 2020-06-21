NAME=network-tools
TAG=dev
IMAGE_NAME=$(NAME):$(TAG)

.PHONY: build
build:
	docker build --tag "$(IMAGE_NAME)" .

.PHONY: run
run:
	docker run --name "$(NAME)" --interactive --tty "$(IMAGE_NAME)"

.PHONY: test
test:
	docker-compose --file docker-compose.test.yml up --build

.PHONY: clean
clean:
	docker rmi "$(IMAGE_NAME)"
