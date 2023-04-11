# List commands

List all containers running:<br>
$ docker ps

List all containers running and history:<br>
$ docker ps -a

List all containers:<br>
$ docker container ls

List all images:<br>
$ docker images<br>
OR<br>
$ docker image ls



# Create Containers

Create a container:<br>
$ docker run [ IMAGE ]<br>

Create a container exponsing a port:<br>
$ docker run -p [ MY PORT ]:[ IMAGE PORT] [ IMAGE ]<br>

Create a container detached (terminal is free):<br>
$ docker run -d [ IMAGE ]<br>

Create a container with a specific name:<br>
$ docker run --name [ NAME ] [ IMAGE ]<br>

Create a container using a specific version of the image:<br>
$ docker run [ IMAGE ]:[ VERSION/TAG ]<br>

Create a container using a specific network:<br>
$ docker run --network [ NETWORK_NAME ] [ IMAGE ]<br>
  
  

# Images
  
List all images:<br>
$ docker images<br>
OR<br>
$ docker image ls<br>

Create a new image from Dockerfile:<br>
$ docker build .<br>
Where "." should be the directory with the Dockerfile.<br>

Create a new image from Dockerfile with a specific name:<br>
$ docker build -t [ NAME ]:[ VERSION/TAG ] .<br>
Where "." should be the directory with the Dockerfile.<br>

Delete an image:<br>
$ docker image rm [ IMAGE ]<br>
  
  
# Network

List networks:<br>
$ docker network ls<br>

Creating a new network:<br>
$ docker network create [ NAME ]<br>

Creating a new network with specific driver (brigde is default):<br>
$ docker network create -d [ TYPE ]  [ NAME ]<br>

Deleting a network:<br>
$ docker network rm [ NAME ]<br>
  
  

# Docker Swarm

Starting Docker Swarm:<br>
$ docker swarm init --advertise-addr [ Manager/Master IP ]<br>

Getting the Manager Node Token to send to another nodes:<br>
$ echo $(docker swarm join-token manager | head -3 | tail -1)<br>

Checking if the nodes are available:<br>
$ docker node ls<br>

Removing a node:<br>
$ docker node rm [ NODE ]<br>

Leaving Docker Swarm:<br>
$ docker swarm leave<br>

List the services running:<br>
$ docker service ls<br>

Creating a new service detached, with a port specification and a name:<br>
$ docker service create -d -p 80:80 --name nginx_service nginx<br>

Updating for a specific service the amount of replicas:<br>
$ docker service update [ OPTION ] [ SERVICE_ID ]<br>
$ docker service update --replicas=2 8ha2j0g1fxq0<br>

Show information about one specific service:<br>
$ docker service ps [ SERVICE ID ]<br>

Creating a Overlay network (similar to Bridge, but only for Swarm):<br>
$ docker network create -d overlay test_net<br>

Create a new Stack or Swarm based on docker-compose.yml file:<br>
$ docker stack deploy -c [ docker-compose.yml ] [ SERVICE_NAME ]<br>

  

# Compose

Run a docker-compose.yaml file locally:<br>
$ docker compose up<br>

Stopping a docker-compose.yaml file locally:<br>
$ docker compose down<br>

Run a docker-compose.yaml file locally in another directory:<br>
$ docker compose -f [ docker-compose.yml file path ] <br>

  

# Labs to test Docker Swarm
  
https://labs.play-with-docker.com



# Docker Hub
  
https://hub.docker.com
  
  
  
# My Docker Hub
  
https://hub.docker.com/u/marco77ap

  

# Docker Docs

https://docs.docker.com

