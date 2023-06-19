// Exercise 1 : List Of People
const people = ["Greg", "Mary", "Devon", "James"];
console.log(people);
people.shift();
console.log('RESULT 1/1: ' + people);
people[2] = 'Jason';
console.log('RESULT 1/2: ' + people);
people.push('Alla');
console.log('RESULT 1/3: ' + people);
console.log('RESULT 1/4: ' + people.indexOf('Mary'))
newPeople = people.slice(1, -1);
console.log('RESULT 1/5: ' + newPeople);
console.log('RESULT 1/6: ' + people.indexOf('Foo')) /* Result: -1. Because 'Foo' doesn't exist in array*/
let last1 = people[people.length-1]
console.log('RESULT 1/7.1: ' + last1);
let last2 = people.slice(-1)
console.log('RESULT 1/7.2: ' + last2);
let last3 = people.pop()
console.log('RESULT 1/7.3: ' + last3);

console.log('RESULT 2/1: ');
for(let i = 0; i < people.length; i++){
    console.log(people[i])
}

console.log('RESULT 2/2: ');
for(let i = 0; i < people.length; i++){
    if(people[i]=='Devon'){
        break;
    }
    console.log(people[i])
}

// Exercise 2 : Your Favorite Colors

const colors = ['blue', 'lavander', 'violet', 'indigo', 'turquoise'];
let number=1;
for(let i = 0; i < colors.length; i++){
    console.log('My #' + number + ' choice is ' + colors[i])
    number++;
}

console.log('BONUS')

let number2=1;
const suffix = ['st', 'nd', 'rd', 'th', 'th'];
for(let i = 0; i < colors.length; i++){
    console.log('My #' + number2 + suffix[i] + ' choice is ' + colors[i])
    number2++;
}

// Exercise 3 : Repeat The Question
