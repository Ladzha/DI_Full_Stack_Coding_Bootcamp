// Exercise 1: Sum Elements
// Write a JavaScript program to find the sum of all elements in an array.

console.log('**** Exercise 1: Sum Elements ****');
let number = [5, 7, 2, 8]
let sum = number.reduce((acc, element) => acc+element)
console.log(`Sum of element of "${number}" is ${sum}`)

// Exercise 2 : Remove Duplicates
// Write a JavaScript program to remove duplicate items in an array.

console.log('**** Exercise 2: Remove Duplicates ****');
let double = [5, 7, 8, 5, 3, 1, 1]
let single = [...new Set(double)]
console.log(single);
let uni = Array.from(new Set(double))
console.log(uni);

let unique = double.filter(function(element, index) {
    if(double.indexOf(element) != double.indexOf(element)){
        console.log('lol');
    }
    // if(element == element){
    //     console.log(element);
    //     return element
    // }
})

console.log('**** Exercise 3: Remove Certain Values ****');
const array = [NaN, 0, 15, false, -22, '',undefined, 47, null];
const result = array.filter(Boolean)
console.log(result);


console.log('**** Exercise 4 : Repeat Please! ****');

function repeat (string, number=1){
    const arr= string.split()
    for(let i = 0; i<number; i++){
        const newArr = arr.reduce((acc, element) =>
        {for(let i = 0; i<number; i++){
            acc+element
        }
        return acc+element}) 
        // console.log(newArr);
    }
    // return string*3
}
console.log(repeat('Ha!',3));