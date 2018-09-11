const Discord = require('discord.js')
const client = new Discord.Client()

client.on('ready', () => {
    var generalChannel = client.channels.get("123456789") // Replace with known channel ID
  
    // Provide a path to a local file
    const localFileAttachment = new Discord.Attachment('D:\\logo.png')
    generalChannel.send(localFileAttachment)

    // Provide a URL to a file
    const webAttachment = new Discord.Attachment('https://www.devdungeon.com/sites/all/themes/devdungeon2/logo.png')
    generalChannel.send(webAttachment)
})

client.login("XXXXXXXXXXX") // Replace XXXXX with your bot token