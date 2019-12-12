start_new_server:
	echo "bootstrapping a new server for you"

environment:
	virtualenv venv
	echo "now call: source ./venv/bin/activate"

install:
	pip3 install -r ./requirements.txt

run:
	python3 server.py

DOCKER_IMAGE := docker-host-name/docker-u-name/image-name:tag-no

package:
	echo "to create a docker build/ python package/code artefacts"
	# docker build -t ${DOCKER_IMAGE} .
	docker-compose -f ./docker-compose.yml build

run_package:
	# docker run --expose=4200 ${DOCKER_IMAGE}
	docker-compose -f docker-compose.yml up

publish:
	echo "TODO: to publish a created docker image / code artefacts to a cental repository"
	# docker push ${DOCKER_IMAGE}
	docker-compose -f ./docker-compose.yml push

