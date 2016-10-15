import requests

# Perform an HTTP GET with a session cookie

url = 'http://www.devdungeon.com'
cookies = {'session': '1234567890'}

# One shot request with cookies
response = requests.get(url, cookies=cookies)

# Print response info
print(response.text) # Response content
print(response.cookies) # Cookies the server gave back to us

# Alternatively, use a session to store response cookies for subsequent requests
#session = requests.Session()
#response = session.get(url, cookies=cookies)