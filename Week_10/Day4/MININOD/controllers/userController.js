import { register, login, updateLastLogin } from "../module/users.js";
import bcrypt from "bcrypt";

export const _register = async (req, res)=>{
    const first_name = req.body.fname; //proverit gde imya
    const last_name = req.body.lname;
    const username = req.body.username;
    const email = req.body.email.toLowerCase();
    const password = req.body.password +''; //chtobi ubeditsya chto eto string potomu chto bcrypt videt chislo kak chislo a ne string

    const salt = bcrypt.genSaltSync(10)
    const hash = bcrypt.hashSync(password, salt)


    try {

    const rows = await register(first_name, last_name, username, email, hash)
    res.json(rows)
        
    } catch (error) {
        console.log(error)
        res.status(404).json({msg: error.message})
    }
}


export const _login = async (req, res)=>{

    const { username, password } = req.body;

    try {

        const userinfo = login(username) //chtobi ubeditsya chto eto string potomu chto bcrypt videt chislo kak chislo a ne string
    
        if(userinfo.length ===0) return res.status(404).json({msg: "username not found"});

        const match = bcrypt.compareSync(password + "",  userinfo[0].password)

        if(!match)return res.status(401).json({ms:'wrong password'})

        await updateLastLogin(username);

        res.status(200).json({ userinfo: { ...userinfo[0], password: "" } })
        
    } catch (error) {
        console.log(error)
        res.status(404).json({msg: "Oh No! something went wrong"})
    }
};