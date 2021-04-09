from settings import CPANEL_API_TOKEN, CPANEL_BASE_URL, CPANEL_USERNAME
from requests import get  # pip install requests
"""
Refer to create_email_account.py for more notes.

https://documentation.cpanel.net/display/DD/UAPI+Functions+-+Email%3A%3Apasswd_pop
"""
endpoint = '/execute/Email/passwd_pop'
params = {
    'email': 'myexistinguser',
    'password': 'newpass',
    'domain': 'devdungen.com',
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
# Data will be empty on success
if data:
    print(f'Data: {data}')
if metadata:
    print(f'Metadata: {metadata}')
# Messages was empty on failure. On success it contained two success messages
if messages:
    print('====== Messages ======')
    for message in messages:
        print(f'- {messages}')
# warnings was empty on success and failure during tests
if warnings:
    print('====== Warnings ======')
    for warning in warnings:
        print(f'- {warning}')
# Error was empty on success, contains message(s) on error
# For example: The password that you entered has a strength rating of “1”. You cannot use it because it is too weak and too easy to guess. Please enter a password with a strength rating of “65” or higher.
# For example: You do not have an email account named “mynewuser2@devdungeon.com”.
if errors:
    print('====== Errors ======')
    for error in errors:
        print(f'- {error}')

# NOTES:
# - On error, data is empty, status is 0, and errors has an array with the message(s).
# - On success, status is 1, data is empty, messages contains success message(s).
