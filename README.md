# List commands

List all containers running:<br>
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
  
  
# Network

List networks:
$ docker network ls

Creating a new network:
$ docker network create <NAME>

Creating a new network with specific driver (brigde is default):
$ docker network create -d <TYPE>  <NAME>

Deleting a network:
$ docker network rm <NAME>
  
  

# Docker Swarm

Starting Docker Swarm:
$ docker swarm init --advertise-addr <Manager/Master IP>

Getting the Manager Node Token to send to another nodes:
$ echo $(docker swarm join-token manager | head -3 | tail -1)

Checking if the nodes are available:
$ docker node ls

Removing a node:
$ docker node rm <NODE>

Leaving Docker Swarm:
$ docker swarm leave

List the services running:
$ docker service ls

Creating a new service detached, with a port specification and a name:
$ docker service create -d -p 80:80 --name nginx_service nginx

Updating for a specific service the amount of replicas:
$ docker service update <OPTION> <SERVICE_ID>
$ docker service update --replicas=2 8ha2j0g1fxq0

Show information about one specific service:
$ docker service ps <SERVICE ID>

Creating a Overlay network (similar to Bridge, but only for Swarm):
$ docker network create -d overlay test_net

Create a new Stack or Swarm based on docker-compose.yml file:
$ docker stack deploy -c <docker-compose.yml> <SERVICE_NAME>

  

# Compose

Run a docker-compose.yaml file locally:
$ docker compose up

Stopping a docker-compose.yaml file locally:
$ docker compose down

Run a docker-compose.yaml file locally in another directory:
$ docker compose -f <docker-compose.yml file path> 

  

# Labs to test Docker Swarm
  
https://labs.play-with-docker.com



# Docker Hub
  
https://hub.docker.com
  
  
  
# My Docker Hub
  
https://hub.docker.com/u/marco77ap

  

# Docker Docs

https://docs.docker.com

