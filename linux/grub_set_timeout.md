# Change Timeout in GRUB

Set `GRUB_TIMEOUT` in `/etc/default/grub`.
Can be as low as 0 to skip.

```
# /etc/default/grub
GRUB_TIMEOUT=0
```

Then run:

```bash
sudo update-grub
```