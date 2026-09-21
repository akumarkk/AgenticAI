###### Ollama

```

$Body = @{
>>     model  = "llama3.2"
>>     prompt = "Why is the sky blue?"
>>     stream = $false
>> } | ConvertTo-Json

$Response = Invoke-RestMethod -Uri "http://localhost:11434/api/generate" -Method Post -Body $Body -ContentType "application/json"
$Response.response
```