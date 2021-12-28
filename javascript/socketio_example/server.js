// server.js
// npm install express socket.io
// Optional
// npm install bufferutil utf-8-validate

const express = require('express');
const http = require('http');
const path = require('path');
const { Server } = require("socket.io");

const expressApp = express();
const httpServer = http.createServer(expressApp);

socketioOptions = {
    cors:
    {
        origin: "http://localhost:3000",
        methods: ["GET", "POST"]  
    },
}
const io = new Server(httpServer, socketioOptions);

/**
 * Express.js Routes
 */

expressApp.use('/', express.static(path.join(__dirname, 'public')))


/**
 * Socket.io Handlers
 */

io.on("connection", socket => {
    // either with send()
    socket.send("Hello!");

    // or with emit() and custom event names
    socket.emit("greetings", "Hey!", { "ms": "jane" }, Buffer.from([4, 3, 3, 1]));

    // handle the event sent with socket.send()
    socket.on("message", (data) => {
        console.log(data);
    });

    // handle the event sent with socket.emit()
    socket.on("salutations", (elem1, elem2, elem3) => {
        console.log(elem1, elem2, elem3);
    });
});

/**
 * Start server
 */
httpServer.listen(3000, () => { console.log('listening on *:3000'); });

