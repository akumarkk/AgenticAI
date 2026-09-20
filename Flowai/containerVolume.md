###### container volume

```

docker volume inspect flowise_data
[
    {
        "CreatedAt": "2026-09-19T22:11:40Z",
        "Driver": "local",
        "Labels": null,
        "Mountpoint": "/var/lib/docker/volumes/flowise_data/_data",
        "Name": "flowise_data",
        "Options": null,
        "Scope": "local"
    }
]

// to mount on local folder
-v C:/flowise:/root/.flowise
```