const axios = require('axios')
const bcrypt = require('bcrypt')

const user = async()=>{
    try{
const axios = require('axios')
        const res = await axios.get('https://jsonplaceholder.typicode.com/users')
        console.log(res.data);
    }
    catch(error){
        console.log(error);
    }
}

user()

const harshPassword = async(pass)=>{
    try{
        const axios = require('axios')
                const salt = await bcrypt.genSalt(10)
                const hash = bcrypt.hashSync(pass, salt)
                console.log(hash);
            }
            catch(error){
                console.log(error);
        }
}

harshPassword(12348980980)