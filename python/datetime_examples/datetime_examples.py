from time import time
from datetime import datetime, timedelta


"""
Get current time
"""

# Get current time as Unix timestamp
unix_timestamp_now = time()
print(f'Unix time: {unix_timestamp_now}')

# Get current time as DateTime object
datetime_now = datetime.now()
print(f'Datetime now: {datetime_now} {type(datetime_now)}')

"""
Convert between timestamp and datetime objects
"""

# Get Unix timestamp from a datetime object
datetime_unix_time = datetime.now().timestamp()
print(f'Datetime as unix timestamp: {datetime_unix_time}')

# Convert timestamp to datetime object
datetime_from_unix_time = datetime.fromtimestamp(time())
print(f'DateTime from Unix timestamp: {datetime_from_unix_time}')

"""
Formatting output
"""

# Format date output
formatted_date = datetime_now.strftime('%A %B, %-d, %Y %-H:%M %p %Z')
print(f'Formatted date: {formatted_date}')  # E.g. Sunday June, 14, 2020 3:17 AM

# Get ISO 8601 format string
# https://en.wikipedia.org/wiki/ISO_8601
# https://strftime.org
iso_date_with_microseconds = datetime_now.strftime('%Y-%m-%dT%H:%M:%S.%fZ%z')
print(f'ISO 8601 date format with microseconds: {iso_date_with_microseconds}')
iso_date_without_microseconds = datetime_now.strftime('%Y-%m-%dT%H:%M:%S.%fZ%z')
print(f'ISO 8601 date format w/o microseconds: {iso_date_with_microseconds}')
easy_iso_format = datetime_now.isoformat()  # Will include microseconds
print(f'ISO 8601 date format: {easy_iso_format}')


"""
Time zones
"""
# The best way to handle timezones is to use `pytz` module and call localize
# pip install pytz
import pytz
timezone = pytz.timezone('America/Chicago')
local_time = timezone.localize(datetime.now())
print(f"Local time ISO: {local_time.isoformat()}")
print(f"Local time friendly: {local_time.strftime('%A %B, %-d, %Y %-H:%M %p %Z')}")


"""
Get future/past times
"""
three_days_ago = datetime.now() - timedelta(days=3)
print(f'Three days ago: {three_days_ago}')


"""
Calculate delta between times
"""

delta = datetime.now() - three_days_ago
print(f'Time delta: {delta} - Days: {delta.days}, Seconds: {delta.seconds}')
print(f'Time delta total seconds: {delta.total_seconds()}')