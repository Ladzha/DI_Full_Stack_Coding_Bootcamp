// Exercise 1 : Print Full Name
console.log('\n*** Exercise 1 : Print Full Name ***\n');

function printFullName(obj) {
const {first, last} = obj
console.log(`Your full name is ${first} ${last}`);

}

printFullName({first: 'Elie', last:'Schoppik'}) 

function printFullName2({first, last}) {
console.log(`Your full name is ${first} ${last}`);    
}
    
printFullName2({first: 'Elie', last:'Schoppik'}) 


// Exercise 2 : Keys And Values

console.log('\n*** Exercise 2 : Keys And Values ***\n');

function keysAndValues(object){

    const key = Object.keys(object);
    const value = Object.values(object);
    // const all = Object.entries(object);
    const all =[[...key], [...value]]
    // console.log(key);
    // console.log(value);
    console.log(all);

}

keysAndValues({ a: 1, b: 2, c: 3 })
// ➞ [["a", "b", "c"], [1, 2, 3]]

keysAndValues({ a: "Apple", b: "Microsoft", c: "Google" })
// ➞ [["a", "b", "c"], ["Apple", "Microsoft", "Google"]]

keysAndValues({ key1: true, key2: false, key3: undefined })
// ➞ [["key1", "key2", "key3"], [true, false, undefined]]

// Exercise 3 : Counter Class
console.log('\n*** Exercise 3 : Counter Class ***\n');

class Counter {
    constructor() {
      this.count = 0;
    }
  
    increment() {
      this.count++;
    }
  }
  
  const counterOne = new Counter();
  counterOne.increment(); //count = 1
  counterOne.increment(); //count = 2
  
  const counterTwo = counterOne;
  counterTwo.increment();  //count = 3
  
  console.log(counterOne.count);