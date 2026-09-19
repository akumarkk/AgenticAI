#### Flowai setup
```
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart


Invoke-WebRequest -Uri "https://aka.ms/wslubuntu2404" -OutFile "Ubuntu2404.appxbundle" -UseBasicParsing
Add-AppxPackage .\Ubuntu2404.appxbundle
```


##### Pre-requisites
```
We've detected that you have an incompatible version of Windows.

Docker Desktop requires Windows 10 Pro/Enterprise/Home 22H2 (19045) or Windows 11 Pro/Enterprise/Home 23H2 (22631) or above.

To continue with the installation, upgrade Windows to a supported version and then re-run the installer.


```

##### Install flowai

```
docker pull flowiseai/flowise:2.2.5
docker run -d --name flowise -p 3000:3000 flowise


In case failure
docker rm -f flowises

docker logs -f flowise

### seem to be an issue with latest 9/19, dependency broken;
```