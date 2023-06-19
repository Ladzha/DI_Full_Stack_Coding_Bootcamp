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
let userNumber
do {
    userNumber = prompt('Enter a number');
    typeof(userNumber);
}
while(userNumber<10);

// # Exercise 4 : Building Management
const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}

console.log('RESULT 1: ');
console.log('The number of floors in the building is ' + building.numberOfFloors)


console.log('RESULT 2: ');
console.log('The number apartments are on the floor 1 is ' + building.numberOfAptByFloor.firstFloor + ' and on the floor 3 is ' + building.numberOfAptByFloor.thirdFloor)

console.log('RESULT 3: ');
console.log('The name of the second tenant is ' + building.nameOfTenants[1] + ' and the number of rooms he has in his apartment is ' + building.numberOfRoomsAndRent.dan[0]);

console.log('RESULT 4: ');

let sum = building.numberOfRoomsAndRent.sarah[1] + building.numberOfRoomsAndRent.david[1];
let danRent = building.numberOfRoomsAndRent.dan[1];
 if(sum > danRent){

    danRent =1200

 };

console.log('The sum of Sarah\'s and David\'s rent is ' + sum + ' so now Dan\'s rent is ' + danRent);

// Exercise 5 : Family
const family = {lastName: 'Smith', member: 3, momName: 'Lola', dadName: 'John', childName: 'Mary', dog: true};

for(key in family){
    console.log(key)
};

for(values in family){
    console.log(family[values])
};

// Exercise 6 : Rudolf

const details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
}

let text1 = '';
for(key in details){
    text1 = text1 + (key + ' ' + details[key] + ' ')
};
console.log(text1)

// Exercise 7 : Secret Group

const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

names.sort();
let result = '';
for(letter in names){   
    result += names[letter][0] 
};
console.log('Super secret name: ' + result)
