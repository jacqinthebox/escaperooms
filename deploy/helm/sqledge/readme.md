Example secret:

```shell
kubectl create secret generic mssql-sa-secret --from-literal=secret=SomeNiceSecret! --dry-run=client -o yaml
```
