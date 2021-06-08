var net = require('net');  // https://nodejs.org/dist/latest/docs/api/net.html


var client = new net.Socket();

client.connect(6667, 'irc.devdungeon.com', function() {
  client.write('USER dano 0 * :John Leon\n');
  client.write('NICK dano\n'); // Must wait a second to register

  setTimeout(function(){ 
     client.write('JOIN #general\n');
      client.write('PRIVMSG #general Hello from my Node.js bot!\n');
   }, 3000);
   
});

client.on('data', function(data) {
  console.log('MESSAGE_FROM_SERVER: ' + data);

  // If data starts with PING, respond with PONG :whatever
  if (data.toString().startsWith('PING')) {
    client.write('PONG ' + data.toString().substring(5));  // Remove `PING ` and pong back what it sent me
    console.log('Recieved PING. PONGED.');
  } else if (data.toString().split(' ')[1] == 'PRIVMSG') {
    // If data comes from a channel
    // :nanodano1!johnd@107.181.165.217 PRIVMSG #general :Hello bot
    // If data comes from privmsg
    // :nanodano1!johnd@107.181.165.217 PRIVMSG dano :hey
    console.log('Destination:' + data.toString().split(' ')[2])
    // Was it a direct message or to the channel?
    if (data.toString().split(' ')[2] == '#general') {
       console.log('message was from general chat')
    } 
    if (data.toString().split(' ')[2] == 'dano') {
       console.log('message was directly to me chat')
    }
    // Was the message a command?
    if (data.toString().split(' ')[3].substring(1).startsWith('!')) {
      console.log('Command detected with ! prefix')
      // Cut off first character, and check command. Run appropriate function. !bitcoin. !ping !8-ball
    }
    console.log('Message:' + data.toString().split(' ')[3].substring(1)); // Cut off : in front
  } else {
    console.log('discarded. unimportant or unplanned');
  }
});



