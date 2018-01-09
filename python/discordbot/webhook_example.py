# This sample Discord bot will post the current Bitcoin price to the webhook provided
# Reference: https://discordapp.com/developers/docs/resources/webhook
import requests

# Create a webhook in the Discord server admin page and copy the URL it provides
# You configure what the bot is named and what channel it posts to when you set up the webhook
discord_webhook_url = 'https://discordapp.com/api/webhooks/371076383537102849/bsfT2mjICLSXRGjKC7Ex2n4ho-9tzJgFnJuqLWYOMmezN1jo-Pqs0lupONr6WELMN4Zk'

# Get the BTC price from CoinDesk
bitcoin_price_url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'

data = requests.get(bitcoin_price_url).json()
price_in_usd = data['bpi']['USD']['rate']
message = "Bitcoin price is currently at $" + price_in_usd + " USD"

# Post the message to the Discord webhook
data = {
    'content': message
}
requests.post(discord_webhook_url, data=data)
