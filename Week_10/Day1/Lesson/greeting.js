const greeting=(name)=>{
    console.log(`Hello ${name}`);
}

const hello=(name)=>{
    console.log(`Hello ${name}`);
}

// module.exports = greeting; //экспортирует функцию



async function getRobot(){
    try{
        const res = await fetch('https://jsonplaceholder.typicode.com/users')
        const data = await res.json();
        return data
    }
    catch(error){
        console.log(error);
    }
}

// function getRobot2(){
//     const response =  fetch('https://jsonplaceholder.typicode.com/users')
//     response
//     .then((response) => {
//         response.json();
//     })
//     .then((data)=>{
//         return data
//     })
//     console.log(details)
//     return details

// }

module.exports ={
    greeting,
    hello,
    getRobot,
    getRobot2,
};