const Discord = require('discord.js')
const client = new Discord.Client()

client.on('ready', () => {
    var generalChannel = client.channels.get("123456789") // Replace with known channel ID
    generalChannel.send("Hello, world!")  
})

client.login("XXXXXXXXXXX") // Replace XXXXX with your bot token