const prices = [10, 23, 5];
// 1. Using a normal for loop, find the sum of the array and save it into a variable
// 2. Using the for each method, find the sum of the array and save it into a variable

let sum = 0;
for(let i =0; i<prices.length; i++){
    sum += prices[i]
}
console.log(sum);

let sum2 = 0;
prices.forEach((element) => sum2 += element)
console.log(sum2);


function doubleValues(arr){
arr.forEach((element, index)=> arr[index]*=2)
}

function doubleValues(arr){
    arr.forEach(function(element, index){
        arr[index]*2
        return arr})
    }

// Write a function called doubleValues which accepts an array and doubles the values of the array
 // result [2,4,6]
console.log(doubleValues([1,2,3]));


// Write a function called vowelCount which accepts a string and returns an object with the keys as the vowel and the values as the number of times the vowel appears in the string. This function should be case insensitive so a lowercase letter and uppercase letter should count
Examples: vowelCount('Elie') // {e:2,i:1}; 
          vowelCount('Tim') // {i:1}; 
          vowelCount('Matt') // {a:1}) 
          vowelCount('hmmm') // {}; 
          vowelCount('I Am awesome and so are you') // {i: 1, a: 4, e: 3, o: 3, u: 1};

function vowelCount(){
    
}

const student = [
    {name:'Lol', score: 33},
    {name: 'Gary', score: 23}

]

const allSores = student.map((element)=>element.score)
console.log(allSores);

const famousPeople = [
    {
        name: "Angelina Jolie",
        job: "actor",
        age: 80
    },
    {
        name: "Georges Clooney",
        job: "actor",
        age: 2
    },
    {
        name: "Paris Hilton",
        job: "actor",
        age: 5
    },
    {
        name: "Kayne West",
        job: "singer",
        age: 16
    },
    {
        name: "Britney Spears",
        job: "singer",
        age: 100
    }
]

const famousName = famousPeople.map((element)=> element.name)
console.log(famousName);

const personFam = famousPeople.map((element)=> 
({name: element['name'],
job: element['job']}))

console.log(personFam);


const studentsFootball = [
    {name: 'Rich', score: 33}, 
    {name: 'Peter', score: 55}
];


// const personFam = famousPeople.map((element)=> 
// ({name: element['name'],
// job: element['job']}))

// console.log(personFam);


// const winner = studentsFootball.map((element, index, arr)=> element.score>50? isAboveAverage==true :isAbove==false )
// console.log(famousName);


// Exercise 1: create a new array that filters only the positive value
const numbers = [-23,-20,-17, -12, -5, 0, 1, 5, 12, 19, 20];
const positive = numbers.filter(element => element>0)

console.log(positive);

// Exercise 2: Suppose you have a list of Star Trek characters,
// and you want to get just the characters that appeared in Star Trek: The Next Generation. Use filter() to filter the array of characters below
const characters = [
   { name: 'James T. Kirk', series: ['Star Trek'] },
   { name: 'Spock', series: ['Star Trek', 'Star Trek: The Next Generation'] },
   { name: 'Jean-Luc Picard', series: ['Star Trek: The Next Generation'] },
   { name: 'Worf', series: ['Star Trek: The Next Generation', 'Star Trek: Deep Space Nine'] }
]; 

const someCharacter = characters.filter(element=> element.series.includes('Star Trek: The Next Generation'))

console.log(someCharacter);


// Exercise 3 NOT MANDATORY - send me the result by slack
// Use the filter method to create an array without duplicates. The result should be ["blue","red","yellow"]
const colors = ["blue", "red", "red", "blue", "yellow"]
// const unique = colors.filter((element, index) => )

// Exercise 1
// Find the sum of the score of the students using reduce

const students = [
 	{name: 'Rich', score: 33}, 
 	{name: 'Peter', score: 55},
 	{name: 'John', score: 75}
];

const score = students.reduce((acc, element)=>{return acc+element.score}, 0)
console.log(score);

// Exercise 2
// Turn an array of voter objects into a count of how many people voted
let voters = [
    {name:'Bob' , age: 30, voted: true},
    {name:'Jake' , age: 32, voted: true},
    {name:'Kate' , age: 25, voted: false},
    {name:'Sam' , age: 20, voted: false},
    {name:'Bob' , age: 30, voted: true},
];

const vote = voters.filter(element=>element.voted==true)
.reduce((acc, element, index)=>{return acc+index}, 0)

console.log(vote);