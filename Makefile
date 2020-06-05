NAME=network-tools
VERSION=dev

IMAGE_NAME=$(NAME):$(VERSION)

.PHONY: build
build:
	docker build --rm -t $(IMAGE_NAME) .
.PHONY: run
run:
	docker run --name network-tools -it network-tools:dev

.PHONY: test
test:
	docker-compose -f docker-compose.test.yml up --build

.PHONY: clean
clean:
	docker rmi $(IMAGE_NAME)
