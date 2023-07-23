import express from "express";
import dotenv from 'dotenv';
import knex from "knex";
import cors from "cors";
import db from './config/db.js';
import u_router from './routes/usersrouter.js';
import path from 'path';

const app = express();
app.use(cors());

//body-parse

app.use(express.urlencoded({extended: true}));
app.use(express.json())
const __dirname = path.resolve()

app.use("/", express.static(__dirname + "/public"))
dotenv.config()

app.use('/users', u_router)

// db('users')
// .select('*')
// .then((rows) => {console.log(rows);})

app.listen(process.env.PORT|| 3005, ()=>{
    console.log('I am listening')
})
