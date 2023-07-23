const formRegister = document.getElementById('registerForm');
const registerButton = document.getElementById('registerButton');
const registerMessage = document.getElementById('registerMessage');


registerButton.addEventListener('click', registerUser)

// registerButton.disabled = true

async function registerUser(event){
    event.preventDefault()
 
    const firstname = document.getElementById('firstname').value;
    const lastname = document.getElementById('lastname').value;
    const email = document.getElementById('email').value;
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value; 

    const response = await fetch("/register", {
        method: "POST",
        headers:{
            "Content-Type": "application/json"
        },
        body: JSON.stringify({firstname, lastname, email, username, password })
    })
        const result = await response.text();

        console.log(result);

        if(result === 'You are a register user now.'){
            registerMessage.textContent = "Hello. Now you are with us"
        }
        else {
            registerMessage.textContent = "This user already exist"

        }

}