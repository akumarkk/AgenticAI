$collectionName = "returns_policy_ecomm"
$uri = "http://127.0.0.1:8000/api/v2/tenants/default_tenant/databases/default_database/collections"

$response = Invoke-RestMethod -Uri $uri -Method Get
$collectionId =$response.id
Write-Host "Collection ID: $collectionId"

# $body = @{
#     query_embeddings = @(
#         # Replace these numbers with your actual embedding vector floats matching your model dimension
#         @(0.12, 0.34, 0.56, 0.78) 
#     )
#     n_results   = 2
# } | ConvertTo-Json -Depth 3

# $body = @"
# {
#     "query_embeddings": [
#         [0.12, 0.34, 0.56, 0.78]
#     ],
#     "n_results": 2
# }
# "@

# Generate an array of 384 floating-point zeros (or random floats) to match the dimension requirement
# $dummyEmbedding = @(0.0) * 384

# # Construct the payload using a custom PowerShell hashtable converted safely with a high depth
# $bodyObject = @{
#     query_embeddings = @(
#         $dummyEmbedding
#     )
#     n_results = 2
# }

# $body = $bodyObject | ConvertTo-Json -Depth 10

# #$uri = "http://127.0.0.1:8000/api/v2/tenants/default_tenant/databases/default_database/collections/$collectionId/query"
# $itemUri = "http://127.0.0.1:8000/api/v2/tenants/default_tenant/databases/default_database/collections/$collectionId/query"
# $queryResponse = Invoke-RestMethod -Uri $itemUri `
#     -Method Post `
#     -ContentType "application/json" `
#     -Body $body

$CollectionId = "8fa5a0d0-5308-49b8-a609-bd1cc1a5e9c0"
$ItemUri = "http://127.0.0.1:8000/api/v2/tenants/default_tenant/databases/default_database/collections/$collectionId/query"

# Generate 384 float values as strings and join them with commas
$floats = 1..384 | ForEach-Object { "0.01" }
$innerArrayString = $floats -join ","

# Construct the raw JSON payload explicitly
$body = @"
{
    "query_embeddings": [
        [$innerArrayString]
    ],
    "n_results": 2
}
"@

$QueryResponse = Invoke-RestMethod -Uri $ItemUri `
    -Method Post `
    -ContentType "application/json" `
    -Body $body

$QueryResponse
# Format and view results
$queryResponse.documents | Format-Table