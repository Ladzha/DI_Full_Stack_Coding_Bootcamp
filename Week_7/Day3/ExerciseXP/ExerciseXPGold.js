// Exercise 1 : Divisible By Three
let numbers = [123, 8409, 100053, 333333333, 7];
for(number of numbers){
    let resNum = number/3
    let result = number%3
    if (result==0){
        console.log(resNum + ' true')
    }
    else{
        console.log(resNum +  ' false')
    }
};

// Exercise 2 : Attendance

let inputName = 'Randy';
inputName.toLowerCase();
let guestList = {
    randy: "Germany",
    karla: "France",
    wendy: "Japan",
    norman: "England",
    sam: "Argentina"
};

// let studentName = guestList;
// let studentCountry = guestList;


if('and' in guestList){
    console.log("Hi! I'm [name], and I'm from [country].")
};
