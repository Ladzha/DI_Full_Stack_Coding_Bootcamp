const formLogin = document.getElementById('formLogin');
const loginButton = document.getElementById('loginButton');
const loginMessage = document.getElementById('loginMessage');

const userLogin = document.getElementById('username')
const passwordLogin = document.getElementById("password")

async function login(event) {
  event.preventDefault();
    const loginInfo = JSON.stringify({ username: userLogin.value, password: passwordLogin.value });

    try {
      const response = await fetch("/login", {
        method: "POST",
        headers: {
          "content-type": "application/json",
        },
        body: loginInfo,
      });


      const parsedData = await response.text();

      console.log(parsedData);

      if(parsedData === 'You are login'){
        loginMessage.textContent = `Welcome ${userLogin.value}`
      } else {

        loginMessage.textContent = "We don't know this user"

      }

    } catch (err) {
      console.log(err);
    }
  }

  loginButton.addEventListener('click', login)

