// 🌟 Exercise 1 : Location

// Analyze the code below. What will be the output?
console.log('*** Exercise 1: Exercise 1 : Location ***');

const person = {
    name: 'John Doe',
    age: 25,
    location: {
        country: 'Canada',
        city: 'Vancouver',
        coordinates: [49.2827, -123.1207]
    }
}

const {name, location: {country, city, coordinates: [lat, lng]}} = person;
// we retrieve:
// name = name: 'John Doe'; 
// In this part 
// location: {country, city, coordinates: [lat, lng]}}
// we go inside location object and retrieve:
// - country - country: 'Canada',
// - city: 'Vancouver',
// and array coordinates - coordinates: [lat, lng] - by creating variable for them: lat, lng]
// RESULT:
// I am John Doe from Vancouver, Canada. Latitude(49.2827), Longitude(-123.1207)

console.log(`I am ${name} from ${city}, ${country}. Latitude(${lat}), Longitude(${lng})`);


// 🌟 Exercise 2: Display Student Info
// Using the code, destructure the parameter inside the function and return a string as the example seen below:
//output : 'Your full name is Elie Schoppik'

console.log('\n*** Exercise 2: Display Student Info ***\n');

function displayStudentInfo(objUser){

    const {first, last} = objUser
    console.log(`Your full name is ${first} ${last}`);
}

displayStudentInfo({first: 'Elie', last:'Schoppik'});


console.log('\n*** Exercise 3: User & Id ***\n');
// Using methods taught in class, turn the users object into an array:
// Excepted output: [ [ 'user1', 18273 ], [ 'user2', 92833 ], [ 'user3', 90315 ] ]

const users = { user1: 18273, user2: 92833, user3: 90315 };
const userArray = Object.entries(users);
console.log(userArray)

// Modify the outcome of part 1, by multipling the user’s ID by 2.
// Excepted output: [ [ 'user1', 36546 ], [ 'user2', 185666 ], [ 'user3', 180630 ] ]
const newArr = userArray.map((element, index) => {
    return[element[0], element[1]*2]})
console.log(newArr)
// console.log(Object.values(newArr));

// FYI : The number is their ID number.

console.log('\n*** Exercise 4 : Person Class ***\n');
// Analyze the code below. What will be the output?
class Person {
    constructor(name) {
      this.name = name;
    }
  }
  
const member = new Person('John');
console.log(typeof member); //- object  instance of class Person with name John


console.log('\n*** Exercise 5 : Dog Clas ***\n');

class Dog {
    constructor(name) {
      this.name = name;
    }
};
///****** - this one overwrite the Dog constructor, but in this constructor. There is not this.name = name;*/
class Labrador1 extends Dog {
    constructor(name, size) { 
      this.size = size;
    }
  };
// const labrador1 = new Labrador1('Sharick', 3) //get error

    // 2 This one ig good
class Labrador2 extends Dog {
    constructor(name, size) {
      super(name);
      this.size = size;
    }
};
const labrador2 = new Labrador2('Sharick', 3) 
console.log(labrador2);

  // 3 In this case we can't put name to the dog
  class Labrador3 extends Dog {
    constructor(size) {
      super(name);
      this.size = size;
    }
  };

const labrador3 = new Labrador3('Sharick', 3) //get error
// console.log(labrador3);

    // 4
class Labrador4 extends Dog {
    constructor(name, size) {
      this.name = name; // We don't need this line here
      this.size = size;
    }
  };
//   const labrador4 = new Labrador4('Sharick', 3)
//   console.log(labrador4); //get error

console.log('\n*** Exercise 6 : Challenges ***\n');
// [2] === [2] //false 2 different places in memory
// {} === {} //false 2 different places in memory
console.log([2] === [2]);
console.log({} === {});

// What is, for each object below, the value of the 
// property number and why?

const object1 = { number: 5 }; //Objects 1, 2, 3, link to 1 place in memory
const object2 = object1;  
const object3 = object2; 

const object4 = { number: 5}; //Objects 4 have it's own place in memory 

console.log(object1.number) //5 
console.log(object2.number) //5
console.log(object3.number) //5
console.log(object4.number) //5
console.log("***********")
object1.number = 4; //4 - change value in memory for object1. But objects 2 and 3 point to the same place in memory and value of number the same for all
console.log(object1.number) //4
console.log(object2.number) //4
console.log(object3.number) //4
console.log(object4.number) //5 //Objects 4 have it's own place in memory and hus own value for number


class Animal{
    constructor (name, type, color){
        this.animalName = name;
        this.animalType = type;
        this.animalColor = color;
    }
}

class Mamal extends Animal{
    // constructor(name, type, color){
    //     super(name, type, color)
    // }
    sound(sound){
        // this.animalSound = sound;
        console.log(`${sound} I'm a ${this.animalType}, named ${this.animalName} and I'm ${this.animalColor}`);
    }

}

const farmerCow = new Mamal('Lily', 'cow', 'brown and white')
console.log(farmerCow);
farmerCow.sound('Moooo')