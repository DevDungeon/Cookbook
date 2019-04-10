# Merge multiple AVI files in to one
# Requires: sudo apt-get install mencoder

# Use mencoder to merge all avi files in to one.
mencoder -oac copy \
         -ovc copy $(ls /home/pi/Pictures/*.avi) \
         -o /home/pi/Pictures/full_movie.avi

