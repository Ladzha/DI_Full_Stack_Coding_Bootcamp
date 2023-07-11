// Exercise 2 : HTTP & JSON

const http = require('http')

const user = {
    firstname: 'John',
    lastname: 'Doe'
};

const server = http.createServer((request, response)=>{
    response.setHeader('content-type', 'text/html')
    response.end(JSON.stringify(user))
});

const PORT = 3000;
const HOST = 'localhost';

server.listen(PORT, HOST, ()=>{
    console.log(`Server run: http://${HOST}:${PORT}`);
});