```bash
#!/bin/bash
#sudo apt install cifs-utils

# Can omit password
sudo mount -t cifs -o uid=odin,gid=sudo,user=dano,password=secret \\\\datnas.local\\home /mnt/smbhome
```
