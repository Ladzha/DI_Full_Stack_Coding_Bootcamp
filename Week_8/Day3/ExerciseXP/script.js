// 🌟 Exercise 1 : Colors
const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
// Write a JavaScript program that displays the colors in the following order : “1# choice is Blue.” “2# choice is Green.” “3# choice is Red.” ect…
// Check if at least one element of the array is equal to the value “Violet”. If yes, console.log("Yeah"), else console.log("No...")
// Hint : Use the array methods taught in class. Look at the lesson Array Methods.

let answer;
colors.forEach((color, index)=>{
    console.log(`${index+1}# choice is ${color}`);
    colors.some(color => color ==='Violet')?  answer="Yeah" : answer = "No..."
});
console.log(answer)

// 🌟 Exercise 2 : Colors #2
// Write a JavaScript program that displays the colors in the following order : “1st choice is Blue .” “2nd choice is Green.” “3rd choice is Red.” ect…
// Hint : Use the array methods taught in class and ternary operator.

const colorsList = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
const ordinal = ["th","st","nd","rd"];

colorsList.forEach((color, colorIndex) =>{
    const ordinal = ["th","st","nd","rd"]
    console.log(`${colorIndex+1}${ordinal[colorIndex>3 ? colorIndex=0: colorIndex=colorIndex ]} choice is ${color}`)
});

// Exercise 3 : Analyzing

// ------1------
const fruits = ["apple", "orange"];
const vegetables = ["carrot", "potato"];

const result = ['bread', ...vegetables, 'chicken', ...fruits];
console.log(result);

// ------2------
const country = "USA";
console.log([...country]);

// ------Bonus------
let newArray = [...[,,]];
console.log(newArray);

