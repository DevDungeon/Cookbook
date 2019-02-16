# Requires: sudo apt-get install mencoder
# To set it up to run on a cron job once per day at 5am:
# crontab -e
# 0 5 * * * /home/pi/timelapse_scripts/stitch_video.sh
DATE=`date '+%Y-%m-%d %H:%M:%S'`
echo "$DATE [*] Creating timelapse video"

cd /home/pi/Pictures

ls *.jpg > image_list.txt
mencoder -nosound -ovc lavc -lavcopts vcodec=mpeg4:aspect=16/9:vbitrate=8000000 -vf scale=2592:1944 -o timelapse.avi -mf type=jpeg:fps=24 mf://@image_list.txt

echo "[+] Done creating video."