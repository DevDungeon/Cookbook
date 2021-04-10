"""
Refer to create_user.py for more details on API.


Change password (update user)

PUT /users/{username}

Data:

{
    "username": "testuser",
    "name": "Test User edit",
    "email": "test@edit.de",
    "properties": [
        {
            "key": "keyname",
            "value": "value"
        }
    ]
}
"""
from settings import OPENFIRE_BASE_URL, OPENFIRE_SECRET_KEY
from requests import put

username = 'newuser'  # Existing user
endpoint = f'/users/{username}'
headers = {
    'Authorization': OPENFIRE_SECRET_KEY,
    'Content-Type': 'application/json',
}
data = {
    "username": username,
    "password": "$ecret123123",

}


response = put(OPENFIRE_BASE_URL + endpoint, headers=headers, json=data, verify=False)
print(response)
print(response.text)
if response.status_code == 200:
    print('great success!')
if response.status_code == 409:
    # E.g. UserAlreadyExistsException
    print(response.json())  # keys: resource, message, exception
