import requests

price_url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'

data = requests.get(price_url).json()

price_in_usd = data['bpi']['USD']['rate']

print("Bitcoin price is currently at $" + price_in_usd + " USD")


