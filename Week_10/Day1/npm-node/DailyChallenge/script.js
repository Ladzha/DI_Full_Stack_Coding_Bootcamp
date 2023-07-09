// const a = require("largeNumber")
const largeNumber = require('./main2.js');
const b = 5;
console.log(largeNumber+b);

let http = require("http");

const server = http.createServer((request, response) =>{
    response.setHeader('Content-Type', 'text/html')
    response.end('<p>Hello</p>')
    console.log("I'm listening")
});

server.listen(3000)
