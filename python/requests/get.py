#get.py

import requests

r = requests.get("http://localhost:9999", timeout=5)

print(r)
print(r.text)