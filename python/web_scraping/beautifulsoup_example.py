import requests
from bs4 import BeautifulSoup


response = requests.get('https://www.devdungeon.com/archive')

soup = BeautifulSoup(response.text)

# print(soup.prettify())

print(soup.title.string)

for a in soup.find_all('a'):
    print(a.string)
    print(a.get('href'))


for img in soup.find_all('img'):
    print(img.get('src'))
    print(img.get('alt'))

for script in soup.find_all('script'):
    print(script.string)
    print(script.get('src'))
