// Exercise 1 : Find The Numbers Divisible By 23
// Create a function call displayNumbersDivisible() that takes no parameter.
// In the function, loop through numbers 0 to 500.
// Console.log all the numbers divisible by 23.
// At the end, console.log the sum of all numbers that are divisible by 23.
// Bonus: Add a parameter divisor to the function.

console.log('***********************');
console.log('Exercise 1 : Find The Numbers Divisible');

let sum = 0;
let srtring = 'Outcome: ';
function displayNumbersDivisible(divisor){
    for(let i =0; i<=500; i++){
        if(i%divisor==0){
        srtring += (' ' + i)
        sum +=i 
        }  
    } 
    console.log(srtring)
    console.log('Sum: ' + sum)
};

displayNumbersDivisible(23);

// Exercise 2 : Shopping List
// Add the stock and prices objects to your js file.
// Create an array called shoppingList with the following items: “banana”, “orange”, and “apple”. It means that you have 1 banana, 1 orange and 1 apple in your cart.
// Create a function called myBill() that takes no parameters.
// The function should return the total price of your shoppingList. In order to do this you must follow these rules:
// The item must be in stock. (Hint : check out if .. in)
// If the item is in stock find out the price in the prices object.
// Call the myBill() function.
// Bonus: If the item is in stock, decrease the item’s stock by 1

console.log('***********************');
console.log('Exercise 2 : Shopping List');
console.log('***********************');

const stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

const prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

const shoppingList =['banana', 'orange', 'apple'];
let total =0;
function myBill(){
    for (fruit of shoppingList){
        if (fruit in stock){
            total += prices[fruit]
            stock[fruit] --;
        }
    }
    console.log(stock);
    console.log('Pay: ' + total);
};

myBill();

console.log('***********************');
console.log('Exercise 3 : What\'s In My Wallet ?');
console.log('***********************');

// A quarters is 0.25
// A dimes is 0.10
// A nickel is 0.05
// A penny is 0.01

let sumOfChange=0;
function changeEnough(itemPrice, amountOfChange){
    let amountOfQuarters = amountOfChange[0];
    let amountOfDimes  = amountOfChange[1];
    let amountOfNickel  = amountOfChange[2]
    let amountOfPenny  = amountOfChange[3];

    let quarters = amountOfQuarters*0.25;
    let dimes = amountOfDimes*0.1;
    let nickel = amountOfNickel*0.05;
    let penny = amountOfPenny*0.01;

    let sum = quarters+dimes+nickel+penny
    console.log(sum)

    if(itemPrice <= sum){
        return true;
    }
    else{
        return false;
    }
}

console.log(changeEnough(4.25, [25, 20, 5, 0]));
console.log(changeEnough(14.11, [2,100,0,0]));
console.log(changeEnough(0.75, [0,0,20,5]));
console.log('***********************');
