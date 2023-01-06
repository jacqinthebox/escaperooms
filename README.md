# Escaperooms

The Big Escaperoom Tournament.

This is a Svelte app merely for demo purposes. It will use SvelteKit in a next iteration, for now it is vanilla Svelte.
Hardcoded passwords are for demo use.

## Run locally

Podman or docker.

```shell
podman run --cap-add SYS_PTRACE -e 'ACCEPT_EULA=1' -e 'MSSQL_SA_PASSWORD=your-password' -p 1433:1433 --name sqledge -d mcr.microsoft.com/azure-sql-edge
```

And start all the apps


## Docker compose

```sh
docker-compose build
docker-compose up
```
