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
    };
};

// Exercise 2 : Attendance

let guestList = {
    randy: "Germany",
    karla: "France",
    wendy: "Japan",
    norman: "England",
    sam: "Argentina"
};

let studentInput = prompt('Enter your name');
let studentName = studentInput.toLocaleLowerCase();

let studentCountry = guestList;

if(studentName in guestList){
   studentNameModify=studentName.charAt(0).toUpperCase()+studentName.slice(1);

    console.log(`Hi! I'm ${studentNameModify}, and I'm from ${guestList[studentName]}.`);
}
else{
    console.log("Hi! I'm a guest.");
};

//Exercise 3 : Playing With Numbers
let age = [20,5,12,43,98,55];
let sum =0;
let highestAge = age[0];
for(let i=0; i<age.length; i++ ){
    sum+=age[i];
    if(highestAge<age[i]){
        highestAge = age[i]
    };
}
console.log(`The sum of all the numbers in the age array - ${sum}`);
console.log(`The highest age in the array - ${highestAge}`);