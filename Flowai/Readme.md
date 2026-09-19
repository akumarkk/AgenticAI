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