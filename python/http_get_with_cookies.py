import requests

url = 'http://www.example.com'
cookies = {'session': 'asdfasdf12341234'}

# User session to store response cookies for subsequent requests
#session = requests.Session()
#response = session.get(url, cookies=cookies)

# One shot request with cookies specified manually
response = requests.get(url, cookies=cookies)

# Print response info
print(response.text)
print(response.cookies)