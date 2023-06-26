// Exercise 1:
// Return the name of the the user, the user's name is a parameter. Do this exercise,
// - first by using function declarations
// - then function expression,
// - then arrow function

function nameUs(user){
    return user
}
const usName = function (user){
    return user
}
const usNameAr = (user)=>user

// Exercise 2: Function & Arrow function & Ternary Operator
// Check if the user's age is higher than 18. Use ternary operator.
// if the user's age is higher than 18, return "You can drive"
// else, return "You cannot drive"
// Do this exercise,

// - first by using function declarations
// - then function expression,
// - then arrow function

function nameUsAg(user){
    if(user.age > 18){
        return "You can drive";
    }
    else{
        return "You cannot drive";
    }
}


function nameUsAg(user){
    return user.age > 18? "You can drive": "You cannot drive";
}

const nameUsAgEx = function (user){
    const result = user.age > 18? "You can drive": "You cannot drive";
    return result;
}

const nameUsAgExAr = (user) => user.age > 18? "You can drive": "You cannot drive";



// 1. Create a function named starWars that takes no parameter.
// 2. The function should declare a variable characters equal to an empty array
// 3. In the startWars function, create a function named createCharacter. It receives two parameters, the first name and last name of a character. If the character doesn't have a last name, the default should be "Smith" and push it to the characters array.
// 4. In the startWars function, create a function named displayCharacter should display in the body the fullname of the characters,
// 5. Call the createCharacter function a few times inside the starWars function and call the displayCharacter function once


function starWars(){
    const characters=[]
    function createCharacter(firstName, lastName='Smith'){
        characters.push(` ${firstName} ${lastName} `)
        return characters
    };
    createCharacter('Sam', 'Johns');
    createCharacter('Sara', 'Sarantes');
    createCharacter('Lola', 'Land');

    function displayCharacter(){
        const character = document.createTextNode(characters)
        const body = document.querySelector('body')
        body.appendChild(character)
    }
    displayCharacter()
}

// starWars()

// Second Part : BONUS

// 6. Change the starWars function, to take one parameter, the name of the spaceship the characters are in 
// 7. The displayCharacter function should now display in the body the fullname and spaceship of the characters 
// 8. Call the starWars function once with the spaceship "The Devastator", and another times with the spaceship "Republic Attack Cruiser". what happens?


function starWars(spaceship){
    const characters=[]
    function createCharacter(firstName, lastName='Smith'){
        characters.push(` ${firstName} ${lastName}`)
        return `${characters} ${spaceship}`
    };
    createCharacter('Sam', 'Johns');
    createCharacter('Sara', 'Sarantes');
    createCharacter('Lola', 'Land');

    function displayCharacter(){
        const character = document.createTextNode(`${characters} ${spaceship}`)
        const body = document.querySelector('body')
        body.appendChild(character)
    }
    displayCharacter()
}

starWars('The Devastator')
// starWars('Republic Attack Cruiser')