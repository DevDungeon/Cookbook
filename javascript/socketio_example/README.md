SocketIO webpage: https://socket.io/docs/v4/

Run server with `node server.js`
Then open browser and visit http://localhost:3000/

// npm install express socket.io
// Optional
// npm install bufferutil utf-8-validate


In the server, you create an express app, then an http server that wraps the express app, then the socket io server taps into the http server
finally start the http server

## References

https://socket.io/docs/v4/

https://socket.io/docs/v4/server-initialization/
https://socket.io/docs/v4/handling-cors/
https://socket.io/docs/v4/server-options/
https://nodejs.org/docs/latest/api/http.html#http_class_http_server
npm install express socket.io