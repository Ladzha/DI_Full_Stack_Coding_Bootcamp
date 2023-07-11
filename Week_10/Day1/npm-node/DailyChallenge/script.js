// const a = require("largeNumber")
const {largeNumber, getDateTime} = require('./main2.js');
const b = 5;
const res = largeNumber+b
console.log(res);

let http = require("http"); 

const server = http.createServer((request, response) =>{
    response.setHeader('Content-Type', 'text/html')
    response.end(`<h1>"Hi there at the frontend"</h1><p>My Module is ${res}</p> <p>${getDateTime()}</p>`)
    console.log("I'm listening")
});

server.listen(3001)
