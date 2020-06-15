#!/usr/bin/python3
"""
Set it up to run on cron every 5 minutes.

```bash
sudo crontab -e
```

and add:

```
*/5 * * * * /home/pi/Pi-Timelapser/take_picture.py 2>&1
```

Notes: https://www.raspberrypi.org/documentation/raspbian/applications/camera.md
"""
# 
from os import system
from os.path import join
from datetime import datetime


now = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
output_filename = f'/opt/timelapser/images/plant-{now}.jpg'

system(f'raspistill -o {output_filename} --annotate 12 --quality 100')
