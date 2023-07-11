const {greeting, hello, getRobot, getRobot2} = require("./greeting.js")

let a = 5;
let g =9;
console.log(a+g);


for(let i=0; i<4; i++){
    console.log(i);
}

// const greetng=(name)=>{
// console.log(`Hello ${name}`);
// }

greeting('fill')
hello('Sam')


getRobot().then((data)=>{
console.log(data[0]);
})

// console.log(getRobot());
// console.log(getRobot2());
