import requests

postData = {
    'name': 'nanodano',
    'pass': 'password1',
    'form_id': 'user_login',
    'op': 'Log in'
}

loginUrl = 'http://www.devdungeon.com/user'

session = requests.Session()
response = session.post(loginUrl, data=postData)

print(response.text)
print(response.headers)
print(session.cookies) # The session cookie is stored for subsequent requests
