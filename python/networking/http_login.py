import requests

postData = {
    'name': 'username',
    'pass': 'password',
    'form_id': 'user_login',
    'op': 'Log in'
}

loginUrl = 'http://www.example.com/login'

session = requests.Session()
response = session.post(loginUrl, data=postData)

print(response.text)
print(response.headers)
print(session.cookies)