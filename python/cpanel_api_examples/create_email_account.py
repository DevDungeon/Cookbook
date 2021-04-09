from settings import CPANEL_API_TOKEN, CPANEL_BASE_URL, CPANEL_USERNAME
from requests import get  # pip install requests
"""
Examples:

CPANEL_API_TOKEN = 'AAABBBCCCDDDD'
CPANEL_BASE_URL = 'https://cpanel.example.net:2083/cpsess##########'
CPANEL_USERNAME = 'myuser'

Docs:

- Create email (add_pop): https://documentation.cpanel.net/display/DD/UAPI+Functions+-+Email%3A%3Aadd_pop
- Delete email (delete_pop): https://documentation.cpanel.net/display/DD/UAPI+Functions+-+Email%3A%3Adelete_pop
- Change pass (passwd_pop): https://documentation.cpanel.net/display/DD/UAPI+Functions+-+Email%3A%3Apasswd_pop

Example add main call:

https://hostname.example.com:2083/cpsess##########/execute/Email/add_pop?email=user&password=12345luggage&quota=0&domain=example.com&skip_update_db=1

"""

endpoint = '/execute/Email/add_pop'
params = {
    'email': 'mynewuser',
    'password': '$ecret1234!',
    'domain': 'devdungeon.com',
    'quota': '5000',  # in megabytes
    'skip_update_db': 0,
    'send_welcome_email': 1,
}
headers = {
    'Authorization': f'cpanel {CPANEL_USERNAME}:{CPANEL_API_TOKEN}'
}
url = CPANEL_BASE_URL + endpoint
print(f'URL: {url}')
result = get(url=url, headers=headers, params=params, verify=True)
print('===== Raw output =====')
print(result.text)
print('===== End raw output =====')

# We still get a 200 OK even if the request is denied. Check ['errors']
if result.status_code != 200:
    raise Exception('Error making create email request!')

# Extract data from response
response = result.json()
data = response.get('data')  # On success, should be `user+domain.com`
errors = response.get('errors')
warnings = response.get('warnings')
messages = response.get('messages')
status = response.get('status')
metadata = response.get('metadata')

# Print things out
print(f'Response status code: {result.status_code}')
# Status will be 0 on fail, 1 on success
if status == 0:
    print('Things did not seem to go well. Check errors.')
elif status == 1:
    print('Success!')
print(f'Status: {status}')
# Data will be empty on error and contain `user+domain.com` on success
if data:
    print(f'Data: {data}')
if metadata:
    print(f'Metadata: {metadata}')
# Messages was empty on failure. On success it contained one empty string in list.
if messages:
    print('====== Messages ======')
    for message in messages:
        print(f'- {messages}')
# warnings was empty on success and failure during tests
if warnings:
    print('====== Warnings ======')
    for warning in warnings:
        print(f'- {warning}')
# Error was empty on success, contained array of messages on failure
# For example: 'The password that you entered has a strength rating of “1”. You cannot use it because it is too weak and too easy to guess. Please enter a password with a strength rating of “65” or higher.'
# For example: 'The account mynewuser@devdungeon.com already exists!'
if errors:
    print('====== Errors ======')
    for error in errors:
        print(f'- {error}')

# NOTES:
# - On error, data is empty, status is 0, and errors has an array with the message(s).
# - On success, data contains `user+domain.com`, status is 1, errors is empty, messages contains one object in the list but it's empty
