const express = require('express');

const app = express();

app.get('/', (request, response) =>{
    response.send('<h1>This is an HTML tag</h1>')
});

const PORT = 3000;
const HOST = 'localhost';

app.listen(3000, ()=>{
    console.log(`Server run: http://${HOST}:${PORT}`);
});