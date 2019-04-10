Every X minutes
- Take picture

Once per day, at 12:00am
- generate an avi from all the files on the pi, labeled with date of photos
- upload the avi to S3
- clear our the pictures dir on pi

On Amazon S3, the daily AVI files will be stored.
Periodically, at my convenience, I can download them all and merge them together and push it back up to s3 (replacing the file each time)