// Discord kick ban bot
// npm install discord.js
var TOKEN = "NjI4MTczMTMxMjA2NDkyMTYx.XZHWSg.TacRJBai9YCTcav7Za5CVjgF-JE";

const Discord = require('discord.js');

const client = new Discord.Client();

client.on('message', message => {
    if (!message.guild) return; // Ignore private messages
    if (message.content.startsWith('!kickme')) {
        //const user = message.mentions.users.first();
        // Now we get the member from the user
        message.guild.member.kick('Optional reason that will display in the audit logs').then(() => {
            message.reply(`Successfully kicked ${user.tag}`);
        }).catch(err => {
            message.reply('I was unable to kick the member');
            console.error(err);
        });
    }
});

// Get tokens from https://discordapp.com/developers/applications/me
client.login(TOKEN);