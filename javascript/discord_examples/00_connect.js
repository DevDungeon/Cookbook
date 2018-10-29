// Tutorial available at: 
// https://www.devdungeon.com/content/javascript-discord-bot-tutorial
// https://www.youtube.com/watch?v=7A6cNW04g2M
// https://discordapp.com/developers

const Discord = require('discord.js')
const client = new Discord.Client()

client.on('ready', () => {
    console.log("Connected as " + client.user.tag)
})

// Get your bot's secret token from:
// https://discordapp.com/developers/applications/
// Click on your application -> Bot -> Token -> "Click to Reveal Token"
bot_secret_token = "XXXXXXXXXXX"

client.login(bot_secret_token)