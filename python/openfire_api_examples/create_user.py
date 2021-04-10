"""
Create a user on the Openfire XMPP server

Enable REST API by logging into admin portal (e.g. https://xmpp.devdungeon.com:9090) and go to `Plugins` and then `Available Plugins`. Enable the `REST API`.
Then go to `Server | Server Settings | REST API` and change it to `Enabled`.
Choose `Secret key auth` option and store that key.

(http 9090, https 9091)
POST https://example.org:9091/plugins/restapi/v1/users

HEADERS:

```
Authorization: SECRETKEY
Content-Type: application/json
```

Data (only username/password required):

```
{
    "username": "admin",
    "password": "p4ssword",
    "name": "Administrator",
    "email": "admin@example.com",
    "properties": {
        "property": [
            {
                "@key": "console.rows_per_page",
                "@value": "user-summary=8"
            },
            {
                "@key": "console.order",
                "@value": "session-summary=1"
            }
        ]
    }
}
```
"""
from requests import post
from settings import OPENFIRE_BASE_URL, OPENFIRE_SECRET_KEY
# OPENFIRE_SECRET_KEY = 'asdfasdfasdf'
# OPENFIRE_BASE_URL = 'https://xmpp.devdungeon.com:9091/plugins/restapi/v1'


endpoint = '/users'
headers = {
    'Authorization': OPENFIRE_SECRET_KEY,
    'Content-Type': 'application/json',
}
data = {
    "username": "newuser",
    "password": "$ecret",
    "name": "New User",
    "email": "newuser@devdungeon.com",
}


response = post(OPENFIRE_BASE_URL + endpoint, headers=headers, json=data, verify=False)
print(response)
print(response.text)
if response.status_code == 201:
    print('great success!')
if response.status_code == 409:
    # E.g. UserAlreadyExistsException
    print(response.json())  # keys: resource, message, exception
