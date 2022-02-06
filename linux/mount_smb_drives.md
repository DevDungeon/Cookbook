# Mounting SMB drives

## Dependencies

In Debian 11, you will need the `cifs-utils` package.

```bash
sudo apt install cifs-utils
```

## Mount manually

Here are some examples of how to mount the drive manually with the `mount` command.

The `uid` & `gid` refer to local Linux users. User an password refer to NAS user credentials.

```bash
# Mount, with a prompt for the password
mount -t cifs -o uid=mylinuxuser,gid=sudo,user=dano, \\\\mynas.local\\music /mnt/music

# Get credentials from a file
mount -t cifs -o uid=mylinuxuser,gid=sudo,credentials=/root/smbcreds.txt \\\\mynas.local\\music /mnt/music

# Include password in command (NOT RECOMMENDED)
mount -t cifs -o uid=mylinuxuser,gid=sudo,user=dano,password="secret" \\\\mynas.local\\music /mnt/music
```

## Credential file

If using the credential file option, it should look like this:

```plaintext
username=mynasuser
password=my nas password
```

To lock it down, you could put it in the root user home directory with permissions of `400`.

```bash
mv creds.txt /root/smbcreds.txt
chmod 400 /root/smbcreds.txt
```


## Mount automatically

To mount the drives automatically on boot, setup the mounts in `/etc/fstab`.

```plaintext
# Append this in `/etc/fstab`
//mynas.local/music /mnt/music cifs uid=mylinuxuser,gid=sudo,credentials=/root/smbcreds.txt
```

If you are adding the drives for the first time, you can remount all drives without rebooting with:

```bash
# Remount `/etc/fstab` without rebooting
sudo mount -a
```