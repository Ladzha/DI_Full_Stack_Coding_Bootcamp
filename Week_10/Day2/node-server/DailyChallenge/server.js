const express = require('express');
const app = express();

app.use('/', express.static(__dirname+'/public'))


app.get('/', (request, response)=>{
    response.send('test')
})

function allLetter(inputtxt)
  {
   var letters = /^[A-Za-z]+$/;
   if(inputtxt.value.match(letters))
     {
      return true;
     }
   else
     {
    //  alert("message");
     return false;
     }
  }

app.get('/aboutMe/:hobby', (request, response)=>{
    const hobby = request.params.hobby
    
    if(!allLetter)return response.status(404).json({msg: "Think again"})
    else{
        response.send(`My hobby is ${hobby}`)
    }
})

app.get('/pic', (request, response)=>{
    response.sendFile(__dirname+'/public/pic.html')
})

app.get('/form', (request, response)=>{
    response.sendFile(__dirname+'/public/form.html')
})

app.get('/formData', (request, response)=>{
    const email = request.params.email
    const message = request.params.message

    response.send(`${email} sent you a message ${message}`)
})



// app.get('/', (request, response)=>{
//     response.send('test')
// })

const PORT = 3000;
const HOST = 'localhost';

app.listen(3001, () =>{
    console.log("server listen");
})