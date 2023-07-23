import express from "express";
import * as fs from 'fs';
import path from 'path'

const __dirname = path.resolve()

const app = express();


app.use(express.urlencoded({extended: true}))
app.use(express.static('public'));
// app.use("/", express.static(__dirname +'/public'));
app.use(express.json());


app.get("/login", (req, res)=>{
    res.sendFile(__dirname + "/public/login.html")
});

app.get("/register", (req, res)=>{
    res.sendFile(__dirname + "/public/register.html")
});


app.post("/register", async (req, res)=>{
    const { name, lastName, email, username, password } = req.body;

    const data = fs.readFileSync('data.json');
    const users = JSON.parse(data);

    const userExists = users.find(user => user.username === username || user.password === password);

    if(userExists){
        return res.send('Error: user already exist')
    }

    users.push({ name, lastName, email, username, password });

    fs.writeFileSync('data.json', JSON.stringify(users, null, 2));

    res.send('You are a register user now.'); 
})

app.post("/login", async (req, res)=>{
    const { username, password } = req.body;

    const data = fs.readFileSync('data.json');

    const users = JSON.parse(data);
    
    const user = users.find(user => user.username === username && user.password === password);

    if(!user){
        return res.send("This user doesn't exist")
    }

    res.send('You are login');
})



const PORT =3000;

app.listen(PORT || 3005, ()=>{
    console.log(`YES I AM A SERVER! I AM LISTENING PORT ${PORT}`)
}) 