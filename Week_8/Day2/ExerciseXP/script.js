// 🌟 Exercise 1 : Scope
// Analyse the code below, and predict what will be the value of a in all the following functions.
// Write your prediction as comments in a js file. Explain your predictions.

// #1
// function funcOne() {
//     let a = 5;
//     if(a > 1) {
//         a = 3;
//     }
//     alert(`inside the funcOne function ${a}`); 
// }

// #1.1 - run in the console:
// funcOne() 
// +++++++ a = 3 Because 5>3 and we go inside if statement. And where change a value to 3


// #1.2 What will happen if the variable is declared with const instead of let ?     

// +++++++ it will show an error because you can't change const value

//#2
// let a = 0;
// function funcTwo() {
//     a = 5;
// }

// function funcThree() {
//     alert(`inside the funcThree function ${a}`);
// }

// #2.1 - run in the console:
// funcThree() 
// +++++++it' get global variable 'a' = 0;
// +++++++inside the funcThree function 0
// funcTwo()
// +++++++function take global variable, and it's rewrote it inside function now a = 5

// funcThree()
// +++++++ We inwoke this function after funcTwo(), so now a =5;
// +++++++ inside the funcThree function 5

// #2.2 What will happen if the variable is declared 
// with const instead of let ?

// +++++++ We can't change value const variable. We will get an error


//#3
// function funcFour() {
//     window.a = "hello"; //++++++ = global variable = a =hello and funcFive sees it
// }


// function funcFive() {
//     alert(`inside the funcFive function ${a}`);
// }

// #3.1 - run in the console:
// funcFour() //++++++ => a = 'hello'
// funcFive()
// ++++++ inside the funcFive function hello

//#4
// let a = 1;
// function funcSix() {
//     let a = "test";
//     alert(`inside the funcSix function ${a}`);
// }


// #4.1 - run in the console:
// funcSix()

// +++++++ inside the funcSix function test. Because we have local 'a' in function

// #4.2 What will happen if the variable is declared 
// with const instead of let ?

// ++++++inside function it's local variable 'a' and global variable doesn't see it, so we will not get an error

//#5
// let a = 2;
// if (true) {
//     let a = 5;
//     alert(`in the if block ${a}`);
// }
// alert(`outside of the if block ${a}`);

// We have 2 different variable global a = 2; and local inside if block a = 5;

// `in the if block 5` - take local variable 'a'

// `outside of the if block 2` - takes global variable 'a'

// We can change each variable to const, because they don't see each other

// #5.1 - run the code in the console
// #5.2 What will happen if the variable is declared 
// with const instead of let ?


// 🌟 Exercise 2 : Ternary Operator
function winBattle(){
    return true;
};

// Transform the winBattle() function to an arrow function.

winBattle = () => {return true}

// Create a variable called experiencePoints.

let experiencePoints;

// Assign to this variable, a ternary operator. If winBattle() is true, the experiencePoints variable should be equal to 10, else the variable should be equal to 1.
// Console.log the experiencePoints variable.

experiencePoints = winBattle()? 10 : 1; 
console.log(`Exercise 2: ${experiencePoints}`);


// 🌟 Exercise 3 : Is It A String ?

const isString = (param) => typeof param === "string" ? true : false;

console.log( `Exercise 3.1: ${isString('Google')}`); 
console.log(`Exercise 3.2: ${isString([1, 2, 4, 0])}`);
console.log(`Exercise 3.3: ${isString(4)}`);

// 🌟 Exercise 4 : Find The Sum

const sum = (a, b) => a+b;

console.log(`Exercise 4: ${sum(6,7)}`);


// 🌟 Exercise 5 : Kg And Grams

// First, use function declaration and invoke it.
function countWeightDeclaration (weight){
return `Exercise 5. Declaration: Your weight is ${weight*1000} gr`
};

console.log(countWeightDeclaration(53));

// Then, use function expression and invoke it.

const countWeightExpression = function(weight){
    return `Exercise 5. Expression: Your weight is ${weight*1000} gr`
};

console.log(countWeightExpression(68));
//Function expression is assigned to variable as its value. Function declaration doesn't need to be assigned to a variable 

const countWeightArrow = (weight) => `Exercise 5. Arrow: Your weight is ${weight*1000}`;

console.log(countWeightArrow(65));

// Syntax

// (function (name) {
//     alert("Hello " + name);
// })("Sarah")


// 🌟 Exercise 6 : Fortune Teller
// Create a self invoking function that takes 4 arguments: number of children, partner’s name, geographic location, job title.
// The function should display in the DOM a sentence like "You will be a <job title> in <geographic location>, and married to <partner's name> with <number of children> kids."

(function FortuneTeller(numberOfChildren, partnerName, geographicLocation, jobTitle){
    let text = document.createTextNode(`Exercise 6: You will be a ${jobTitle} in ${geographicLocation}, and married to ${partnerName}'s with ${numberOfChildren} kids.`)
    let div = document.querySelector('div');
    div.appendChild(text);
})(4, 'Sam', 'London', 'Designer' );

// 🌟 Exercise 7 : Welcome

(function (name){
    const greeting = `Exercise 7: Welcome ${name}`;
    const div = document.createElement('div');
    const img = document.createElement('img');
    const url = 'https://images.pexels.com/photos/3439576/pexels-photo-3439576.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260';
    img.setAttribute('src', url)
    img.style.width = '30px';

    const listUL = document.querySelector('ul');
    const welcomeText = document.createTextNode(greeting) 
    const newListItem = document.createElement('li');
    div.appendChild(img);
    div.appendChild(welcomeText);
    newListItem.appendChild(div);
    listUL.appendChild(newListItem);
    
}) ('John'); 

// 🌟 Exercise 8 : Juice Bar

// small, medium or large
function makeJuice(size='small'){

    function addIngredients(firstIngredient, secondIngredient, thirdIngredient){
        const orderText = `Exercise 8. Part I: The client wants a ${size} juice, containing ${firstIngredient}, ${secondIngredient}, and ${thirdIngredient}".`
        const text = document.createTextNode(orderText)
        const newDiv = document.createElement('div');
        const body = document.querySelector('body');
        newDiv.appendChild(text);
        body.appendChild(newDiv);
    }
    addIngredients('lemon', 'orange', 'apple')
}

makeJuice('medium')


function makeJuiceAgain(size='small'){

    let ingredients =[];
    
        function addIngredients(firstIngredient, secondIngredient, thirdIngredient){
            ingredients.push(firstIngredient, secondIngredient, thirdIngredient)
            return ingredients;
        }
        addIngredients('lemon', 'orange', 'apple')
        addIngredients('lemon', 'orange', 'apple')

        function displayOrder(){
            let ingredientsText = '';
            for(let ingredient of ingredients){
                ingredientsText += ' ' + ingredient +','
            }
            
            const orderText = `Exercise 8. Part II: The client wants a ${size} juice, containing ${ingredientsText}".`
            const text = document.createTextNode(orderText)
            const newDiv = document.createElement('div');
            const body = document.querySelector('body');
            newDiv.appendChild(text);
            body.appendChild(newDiv);
        }

        displayOrder();

    }
    makeJuiceAgain();


    
