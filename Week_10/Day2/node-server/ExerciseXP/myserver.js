// Exercise 1 : HTTP

const http = require('http')
const server = http.createServer((request, response)=>{
    response.setHeader('content-type', 'text/html')
    response.end(`<h1>Hello!</h1>
    <h2>Yes you!</h2>
    <h3>Have a nice day!</h3> `)
})

const PORT = 3000
const HOST = 'localhost'
// server.listen(3000)

server.listen(PORT, HOST, ()=>{
    console.log(`Server run: http://${HOST}:${PORT}`);
});


