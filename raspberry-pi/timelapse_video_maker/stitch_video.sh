# This will take all the images and stitch them together in to a video
# Requires: sudo apt-get install mencoder
# To set it up to run on a cron job once per day at 5am:
# crontab -e
# 0 5 * * * /home/pi/timelapse_scripts/stitch_video.sh


# Generate timelapse video
DATE=`date '+%Y-%m-%d %H:%M:%S'`
echo "$DATE [*] Creating timelapse video"
cd /home/pi/Pictures
ls *.jpg > image_list.txt
YESTERDAY=`date '+%Y-%m-%d' -d 'yesterday'`
VIDEO_FILENAME="timelapse-${YESTERDAY}.avi"
mencoder -nosound -ovc lavc -lavcopts vcodec=mpeg4:aspect=16/9:vbitrate=8000000 -vf scale=3280:2464 -o ${VIDEO_FILENAME} -mf type=jpeg:fps=24 mf://@image_list.txt
echo "[+] Done creating video."


# Delete images
echo "[*] Deleting images used to clear out space."
for img in $(cat image_list.txt)
do
	echo "Deleting $img"
	rm $img
done
rm image_list.txt
echo "[+] Done deleting images used in video."


# Upload video to S3
echo "[*] Uploading file to S3..."
python3 -m awscli s3 cp ${VIDEO_FILENAME} s3://mybucketname/Videos/


# Email notification
cd /home/pi/timelapse_scripts
python3 -m awscli ses send-email --from email@example.com --destination file://destination.json --message file://message.json
# Example destination.json
# {
# 	"ToAddresses":  ["email@example.com"],
# 	"CcAddresses":  [],
# 	"BccAddresses": []
# }

# Example message.json
# {
# 	"Subject": {
# 	"Data": "Test email sent using the AWS CLI",
# 	"Charset": "UTF-8"
# },
# 	"Body": {
# 		"Text": {
# 			"Data": "This is the message body in text format.",
# 			"Charset": "UTF-8"
# 		},
# 		"Html": {
# 			"Data": "This message body contains HTML formatting. It can, for example, contain links like this one: <a class=\"ulink\" href=\"http://docs.aws.amazon.com/ses/latest/DeveloperGuide\" target=\"_blank\">Amazon SES Developer Guide</a>.",
# 			"Charset": "UTF-8"
# 		}
# 	}
# }

