# Take a picture with the Pi camera
# Set this script to run on a cron job
# crontab -e
# Every 5th minute
# */5 * * * /home/pi/timelapse_scripts/take_pic.sh 2>&1

DATE=`date '+%Y-%m-%d-%H-%M-%S'`
echo "$DATE [*] Taking picture"
raspistill -o /home/pi/Pictures/image-${DATE}.jpg
DATE=`date '+%Y-%m-%d-%H-%M-%S'`
echo "$DATE [+] Done taking picture."