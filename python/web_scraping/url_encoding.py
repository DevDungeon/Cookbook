try:
    from urllib.parse import urlencode
except:
    from urllib import urlencode

query_string = urlencode({'q': 15, 'action': 'something'})
print(query_string)
