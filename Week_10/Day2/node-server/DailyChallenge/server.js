const express = require('express');
const app = express();

app.get('/', (request, express.response)=>{
    response.send('test')
})

const PORT = 3000;
const HOST = 'localhost';

app.listen(POST)