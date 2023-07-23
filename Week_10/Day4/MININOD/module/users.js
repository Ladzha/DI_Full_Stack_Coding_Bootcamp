import {db} from "../config/db.js"
import bcrypt from "bcrypt"

export const register = async(first_name, last_name, username, email, hash) =>
{     const trx = await db.transaction();

try{

    const user = await db("users").insert({
        first_name:first_name, 
        last_name: last_name, 
        username: username, 
        email: email, 
        last_login:new Date()
    })
    .returning(["user_id", "username", "email", "first_name", "last_name"]).transacting(trx);
    console.log("user=>", user);

    const hashpwd = await db("hashpwd")
    .insert({
        username:user.username || username,
        password:hash,
    }, ["login_id", "username", "password"]).transaction() //tozhe sampoe chto i returning

    console.log("hashpwd=>", hashpwd);

    await trx.commit()
    return user;

}

catch(err){
    console.log("error=>", err);
    await trx.rollback();
    throw new Error(err.message);
}
    
}

export const login = async(username, password) =>
{     

    return await db("hashpwd")
    .join("users", { "users.username": "hashpwd.username" })
    .select("*")
    .where({ 'hashpwd.username': username });

}

export const updateLastLogin = (username) => {
    return db("users").update({ last_login: new Date() }).where({ username });
  };