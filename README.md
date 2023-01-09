# Escaperooms

The Big Escaperoom Tournament.

This is a Svelte app merely for demo purposes. It will use SvelteKit in a next iteration, for now it is vanilla Svelte.
Hardcoded passwords are for demo use. 

A team can register to do the Escape room tournament. They can enter the escape room and solve puzzles. Once they are done:
* the time spent in the Escape room is registered,
* a picture is sent to the socials.

Until there is proper api documentation:

### frontend
- frontend
- port 8080

### registerservice
- Handles logins, registers and writes to database
- port 5000
- /api (GET)
- /api/register (POST)
- /api/ping (GET)
- /api/login (GET,POST)

### sqledge
- Database for registerservice
- port 1433

### roomservice
- Posts messages to score queue and image queue
- port 5005
- /room/leave (POST)
- /room/ping(GET)
- /room/purge(GET)

### scoreservice
- Consumes the score
- port 5006
- /score/ping(GET)
- /score/teams(POST)
- /dapr/subscribe(GET)


## Docker compose

```sh
docker-compose build
docker-compose up
```


## Run locally

Podman or docker.
```shell
podman run --cap-add SYS_PTRACE -e 'ACCEPT_EULA=1' -e 'MSSQL_SA_PASSWORD=your-password' -p 1433:1433 --name sqledge -d mcr.microsoft.com/azure-sql-edge
```
And start all the apps
