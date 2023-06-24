// 🌟 Exercise 2 : Work With Forms

//1 / Retrieve the form and console.log it.

const form = document.querySelector('form');
console.log(form);

//2 / Retrieve the inputs by their id and console.log them.

let inputFirstname = document.getElementById('fname');
console.log(inputFirstname);

let inputLastname = document.getElementById('lname');
console.log(inputLastname);

let inputSubmit = document.getElementById('submit');
console.log(inputSubmit);

//3 / Retrieve the inputs by their name attribute and console.log them.
// attribute??????

let inputFirstnameByAttribute = form.querySelector('[name = fname]')
console.log(inputFirstnameByAttribute);

let inputLastnameAttribute = form.querySelector('[name = lname]')
console.log(inputLastnameAttribute);

let inputSubmitAttribute =form.elements['submit']
console.log(inputSubmitAttribute);

//4 / When the user submits the form (ie. submit event listener)
//4.1 / use event.preventDefault(), why ?
//4.2 / get the values of the input tags,
//4.3 / make sure that they are not empty,
//4.4 / create an li per input value,
//4.5 / then append them to a the <ul class="usersAnswer"></ul>, below the form.

function checkForm(event){
    if(inputFirstname.value !='' || inputLastname.value !='' ){
        console.log(inputFirstname.value);
        console.log(inputLastname.value);
        let body = document.querySelector('body');
        let textFirstName = document.createTextNode(`User first name: ${inputFirstname.value}`);
        let textLastName = document.createTextNode(`User last name: ${inputLastname.value}`);
        let newLiForFirstName = document.createElement('li');
        newLiForFirstName.appendChild(textFirstName);
        let newLiForLaststName = document.createElement('li');
        newLiForLaststName.appendChild(textLastName);
        let newUl = document.createElement('ul'); 
        newUl.setAttribute('class', 'usersAnswer');
        newUl.appendChild(newLiForFirstName);
        newUl.appendChild(newLiForLaststName);
        let newDiv = document.createElement('div'); 
        newDiv.appendChild(newUl);
        body.appendChild(newDiv);

    }
    else{
        alert('Fill the form')
    }

    event.preventDefault()
}

form.addEventListener('submit', checkForm);



