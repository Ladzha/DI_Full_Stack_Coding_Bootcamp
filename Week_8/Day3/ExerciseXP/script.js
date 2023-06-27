// 🌟 Exercise 1 : Colors
const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
// Write a JavaScript program that displays the colors in the following order : “1# choice is Blue.” “2# choice is Green.” “3# choice is Red.” ect…
// Check if at least one element of the array is equal to the value “Violet”. If yes, console.log("Yeah"), else console.log("No...")
// Hint : Use the array methods taught in class. Look at the lesson Array Methods.

console.log('\n**** Exercise 1 : Colors ****\n')

let answer;
colors.forEach((color, index)=>{
    console.log(`${index+1}# choice is ${color}`);
    colors.some(color => color ==='Violet')?  answer="Yeah" : answer = "No..."
});
console.log(answer)

colors.forEach((color, index)=>{
    console.log(`${index+1}# choice is ${color}`);
    colors.includes('Violet') ?  answer="Yeah" : answer = "No..."
});
console.log(answer)

// 🌟 Exercise 2 : Colors #2
// Write a JavaScript program that displays the colors in the following order : “1st choice is Blue .” “2nd choice is Green.” “3rd choice is Red.” ect…
// Hint : Use the array methods taught in class and ternary operator.

console.log('\n**** Exercise 2 : Colors #2 ****\n')

const colorsList = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
const ordinal = ["th","st","nd","rd"];

colorsList.forEach((color, colorIndex) =>{
    const ordinal = ["th","st","nd","rd"]
    console.log(`${colorIndex+1}${ordinal[colorIndex>3 ? colorIndex=0: colorIndex=colorIndex ]} choice is ${color}`)
});

// Exercise 3 : Analyzing

console.log('\n**** Exercise 3 : Analyzing ****\n')

// ------1------
const fruits = ["apple", "orange"];
const vegetables = ["carrot", "potato"];

const result = ['bread', ...vegetables, 'chicken', ...fruits];
console.log(result);
//new array result consist of: 0 element: bread; all elements from array vegetables (1: carrot, 3: potato), 3 element chicken and all elements from array fruits (4: apple, 5: orange)

// ------2------
const country = "USA";
console.log([...country]);
// country is a new array, each element letter from USA

// ------Bonus------
let newArray = [...[,,]];
console.log(newArray); 
//new array try to get elements from empty array with 2 non exist elements


// 🌟 Exercise 4 : Employees

const users = [{ firstName: 'Bradley', lastName: 'Bouley', role: 'Full Stack Resident' },
             { firstName: 'Chloe', lastName: 'Alnaji', role: 'Full Stack Resident' },
             { firstName: 'Jonathan', lastName: 'Baughn', role: 'Enterprise Instructor' },
             { firstName: 'Michael', lastName: 'Herman', role: 'Lead Instructor' },
             { firstName: 'Robert', lastName: 'Hajek', role: 'Full Stack Resident' },
             { firstName: 'Wes', lastName: 'Reid', role: 'Instructor'},
             { firstName: 'Zach', lastName: 'Klabunde', role: 'Instructor'}];


console.log('\n**** Exercise 4 : Employees ****\n')


// Using the map() method, push into a new array the firstname of the user and a welcome message.

const welcomeStudents = users.map(function(element){
    return `Hello ${element.firstName}`
})
console.log(welcomeStudents);

const welcomeStudentsArrow = users.map(element => `Hello ${element.firstName}`)
console.log(welcomeStudentsArrow);

// 2. Using the filter() method, create a new array, containing only the Full Stack Residents.

const fullStackUsers = users.filter(function(element){
return element.role === 'Full Stack Resident';
});

console.log(fullStackUsers);

const fullStackUsersArrow = users.filter(element => element.role === 'Full Stack Resident');
console.log(fullStackUsersArrow);

// 3. Bonus : Chain the filter method with a map method, to return an array containing only the lastName of the Full Stack Residents.

const fullStackLastName = users.filter(element => element.role === 'Full Stack Resident').map(element => `${element.lastName}`)

console.log(fullStackLastName);

// Exercise 5 : Star Wars
// Using this array use the reduce() method to combine all of these into a single string.

console.log('\n**** Exercise 5 : Star Wars ****\n')

const epic = ['a', 'long', 'time', 'ago', 'in a', 'galaxy', 'far far', 'away'];

const singleString = epic.reduce(function(accumulator, element){
    return `${accumulator + element} `
}, ' ');

console.log(singleString);


const singleStringArrow = epic.reduce((accumulator, element) => `${accumulator + element} `, ' ');

console.log(singleStringArrow);


// 🌟 Exercise 6 : Employees #2

console.log('\n**** Exercise 6 : Employees #2 ****\n')

// Using the filter() method, create a new array, containing the students that passed the course.

const students = [{name: "Ray", course: "Computer Science", isPassed: true}, 
               {name: "Liam", course: "Computer Science", isPassed: false}, 
               {name: "Jenner", course: "Information Technology", isPassed: true}, 
               {name: "Marco", course: "Robotics", isPassed: true}, 
               {name: "Kimberly", course: "Artificial Intelligence", isPassed: false}, 
               {name: "Jamie", course: "Big Data", isPassed: false}];

const goodStudents = students.filter(function(element){
    return element.isPassed ==true;
})
console.log(goodStudents);

const goodStudentsArrow = students.filter(element => element.isPassed ==true);
console.log(goodStudentsArrow);

// Bonus : Chain the filter method with a forEach method, to congratulate the students with their name and course name (ie. “Good job Jenner, you passed the course in Information Technology”, “Good Job Marco you passed the course in Robotics” ect…)


// const congratulation = students.forEach(function(element) {
//     return `Good job ${element.name}, you passed the course in ${element.course}`}).filter(function(element) {
//         return element.isPassed ==true})
// console.log(congratulation);


// const congratulation = students.filter(element => element.isPassed ==true).forEach(element =>`Good job ${element.name}, you passed the course in ${element.course}`);
// console.log(congratulation);

const congratulation = students.

filter(function(element) {

return element.isPassed ===true
}) 
.forEach(function(element) {
    console.log(`Good job ${element.name}, you passed the course in ${element.course}`)
})

// console.log(congratulation);
