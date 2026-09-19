#### Flowai setup
```
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart


Invoke-WebRequest -Uri "https://aka.ms/wslubuntu2404" -OutFile "Ubuntu2404.appxbundle" -UseBasicParsing
Add-AppxPackage .\Ubuntu2404.appxbundle
```