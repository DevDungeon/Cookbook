Timelapse video maker with s3 storage
=====================================

- Set up take_pic.sh to run on cron a descrbed in the file. It will take an image periodically.
- Set up stitch_video.sh to run nightly on cron. It will create a timelapse video from all the images of the day, upload it to s3, and delete the images to free up space
- Whenever you decide, pull down all the videos from s3 and run merge_avis.sh to combine all the nightly videos in to a single video file.
