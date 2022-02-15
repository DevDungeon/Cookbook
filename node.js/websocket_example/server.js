// npm install ws
// Run this server and then open client.html in browser
const { WebSocketServer } = require('ws');

const wss = new WebSocketServer({ port: 8080 });

let clients = [];

wss.on('connection', function connection(client, request) {
    console.log(`Remote IP: ${request.socket.remoteAddress}`);

  client.on('message', function message(data) {
    console.log('Client sent the server: %s', data);
  });

  client.send('Greetings, client!');
  clients.push(client);

  
  console.log(`Clients: ${clients}`);
});

console.log('Running...');

