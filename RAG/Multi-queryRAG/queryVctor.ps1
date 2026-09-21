$collectionName = "returns_policy_ecomm"
$response = Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/v1/collections/$collectionName" -Method Get
$collectionId =$response.id
Write-Host "Collection ID: $collectionId"

$body = @{
    query_texts = @("What is the return policy for Amazon?")
    n_results   = 2
} | ConvertTo-Json -Depth 3

$queryResponse = Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/v1/collections/$collectionId/query" `
    -Method Post `
    -ContentType "application/json" `
    -Body $body

# Format and view results
$queryResponse.documents | Format-Table