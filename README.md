# List commands

List all containers running:
$ docker ps

List all containers running and history:
$ docker ps -a

List all containers:
$ docker container ls

List all images:
$ docker images
OR
$ docker image ls



# Create Containers

Create a container:
$ docker run <IMAGE>

Create a container exponsing a port:
$ docker run -p <MY PORT>:<IMAGE PORT> <IMAGE>

Create a container detached (terminal is free):
$ docker run -d <IMAGE>

Create a container with a specific name:
$ docker run --name <NAME> <IMAGE>

Create a container using a specific version of the image:
$ docker run <IMAGE>:<VERSION/TAG>

Create a container using a specific network:
$ docker run --network <NETWORK_NAME> <IMAGE>
  
  

# Images
  
List all images:
$ docker images
OR
$ docker image ls

Create a new image from Dockerfile:
$ docker build .
Where "." should be the directory with the Dockerfile.

Create a new image from Dockerfile with a specific name:
$ docker build -t <NAME>:<VERSION/TAG> .
Where "." should be the directory with the Dockerfile.

Delete an image:
$ docker image rm <IMAGE>
