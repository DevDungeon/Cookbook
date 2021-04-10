"""
Refer to create_user.py for more details on API.

DELETE /lockouts/{username}

Data: None
"""
from settings import OPENFIRE_BASE_URL, OPENFIRE_SECRET_KEY
from requests import delete

username = 'newuser'  # Existing user
endpoint = f'/lockouts/{username}'
headers = {
    'Authorization': OPENFIRE_SECRET_KEY,
    'Content-Type': 'application/json',
}

response = delete(OPENFIRE_BASE_URL + endpoint, headers=headers, verify=False)
print(response)
print(response.text)
if response.status_code == 201:
    print('great success!')
if response.status_code == 409:
    # E.g. UserAlreadyExistsException
    print(response.json())  # keys: resource, message, exception
