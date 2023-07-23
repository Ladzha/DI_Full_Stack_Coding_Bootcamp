const express = require('express');
const app = express();


app.use('/', express.static(__dirname+'/public'))
app.use(express.urlencoded({ extended: true }));



app.get('/aboutMe/:hobby', (request, response)=>{
    const hobby = request.params.hobby
    
    if(!containsOnlyLetters(hobby)){

        response.status(404).json({msg: "Think again"})

    }
    
    else{
        response.json(`My hobby is ${request.params.hobby}`)
    }
})

app.get('/pic', (request, response)=>{
    response.sendFile(__dirname+'/public/pic.html')
})

app.get('/form', (request, response)=>{
    response.sendFile(__dirname+'/public/form.html')
})

app.post('/formData', (request, response)=>{
    const email = request.body.email
    const message = request.body.message

    response.send(`${email} sent you a message ${message}`)
})


function containsOnlyLetters(str) {
    const lettersRegex = /^[A-Za-z]+$/;
    return lettersRegex.test(str);
  }

app.listen(3001, () =>{
    console.log("server listen");
})