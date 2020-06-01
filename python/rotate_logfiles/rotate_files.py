import glob
import os
from datetime import datetime

current_time = datetime.now().strftime('%Y-%m-%dT%H-%M-%S')
print(f'Current time: {current_time}')

files = glob.glob("*.txt")
# Oldest files are at the front. Newest files at the end
files.sort(key=os.path.getmtime)

print(f'Found {len(files)} files: {files}')
print(f'Oldest 2 files: {files[:2]}')
print(f'Newest 2 files: {files[-2:]}')
