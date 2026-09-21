##### Chroma collections
```
Invoke-RestMethod -Method Post -Uri "http://localhost:8000/api/v2/tenants/default_tenant/databases/default_database/collections" -ContentType "application/json" -Body '{"name": "test_friends", "get_or_create": true}'



Invoke-RestMethod -Method Post -Uri "http://localhost:8000/api/v2/tenants/default_tenant/databases/default_database/collections/24569914-9816-4598-a1e8-d95020aef0c2/add" -ContentType "application/json" -Body '{ "ids": ["api_id_1"], "embeddings": [[0.1, 0.2, 0.3, 0.4]], "documents": ["Hello from PowerShell using the v2 API!"] }'



Invoke-RestMethod -Method Post -Uri "http://localhost:8000/api/v2/tenants/default_tenant/databases/default_database/collections/24569914-9816-4598-a1e8-d95020aef0c2/get" -ContentType "application/json" -Body '{}'


ids        : {api_id_1}
embeddings :
documents  : {Hello from PowerShell using the v2 API!}
uris       :
metadatas  : {$null}
include    : {documents, metadatas}



```