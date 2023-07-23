const formLogin = document.getElementById("login");
const loginMessage = document.getElementById('loginMessage');
console.log(formLogin);

const loginButton = document.getElementById("loginButton");
// loginButton.addEventListener('click', loginUser);



// loginButton.disabled = true;

const formRegister = document.getElementById('register');
const registerMessage = document.getElementById('registerMessage')
console.log(formRegister);

const registerButton = document.getElementById("registerButton");
// registerButton.addEventListener('click', registerUser)



// registerButton.disabled = true;

const loginUser = async (event)=>{
    event.preventDefault()

    const username = event.target.username.value;
    const password = event.target.password.value;

    // const dataFromLogin = new FormData(formLogin);
    // const objFromLogin = Object.fromEntries(dataFromLogin)
    // console.log(objFromLogin)

    try {

        const loginResponse = await fetch('http://localhost:3000/users/login', {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body:JSON.stringify({username, password})
        })

        const parseLoginData = await loginResponse.json()
        console.log("login input works")

        console.log(parseLoginData)
        
    } catch (error) {
        console.log("LOGIN ERROR")
    }

}

const registerUser = async (event)=>{
    event.preventDefault();

    const fname = event.target.fname.value;
    const lname = event.target.lname.value;
    const email = event.target.email.value;
    const username = event.target.username.value;
    const password = event.target.password.value;

    console.log(fname, lname, email, username, password);


    // const dataFromRegister = new FormData(formRegister);
    // const objFromRegister = Object.fromEntries(dataFromRegister)
    // console.log(objFromRegister)

    try {

        // const registerResponse = await fetch('http://localhost:3000/users/register',
        const registerResponse = await fetch('/users/register', {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({fname, lname, email, username, password})
        })

        const parseRegisterData = await registerResponse.json()
        console.log("register input works");
        console.log( parseRegisterData)

        
    } catch (error) {
        console.log("REGISTER ERROR")
    }


}

formLogin.addEventListener('submit', loginUser);

formRegister.addEventListener('submit', registerUser)
