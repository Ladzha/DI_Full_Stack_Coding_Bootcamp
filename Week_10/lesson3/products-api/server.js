import express from "express";
import dotenv from "dotenv";

const app = express()
dotenv.config(); //to read env file

app.listen(process.env.PORT, ()=>{
    console.log((`run on port ${process.env.PORT}`));
});


