// Exercise 1 : Express & JSON

const express = require('express');

const app = express();

const user = {firstname: 'John',lastname: 'Doe'};

app.use(express.static('public'))

app.get('/users', (request, response) =>{
    response.send(JSON.stringify(user))
    console.log(JSON.stringify(user));
});


// Exercise 2 : Express & Parameters

app.get('/:id', (request, response) =>{
    response.send(request.params)
    console.log('id: ', request.params);
});


const PORT = 3001;
const HOST = 'localhost';
 
app.listen(PORT, ()=>{
    console.log(`Server run: http://${HOST}:${PORT}`);
});



