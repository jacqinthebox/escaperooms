# Escaperooms

The Big Escaperoom Race

## Run locally

```shell
podman run --cap-add SYS_PTRACE -e 'ACCEPT_EULA=1' -e 'MSSQL_SA_PASSWORD=your-password' -p 1433:1433 --name sqledge -d mcr.microsoft.com/azure-sql-edge
```

