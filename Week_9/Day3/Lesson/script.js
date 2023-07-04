// fetch("https://jsonplaceholder.typicode.com/users") //promise
// .then(result => {
//     return result.json(); //promise //making the data accessible
// })
// .then((data) => {
//     displayRobot(data)
// })

// function displayRobot (robots) {
//     for (let robot of robots) {
//         console.log(`the robot is ${robot.name}, its email is ${robot.email}`);
//     } 
// }


// const btn = document.getElementById("btn");
// btn.addEventListener("click", makeRequest);

// function makeRequest () {
//     fetch("https://jsonplaceholder.typicode.com/uers")
//     .then(response => {
//         if (response.ok) {
//             return response.json();
//         } else {
//             throw new Error ("issues with fetch");
//         }
//     })
//     .then(data => displayRobots(data))
//     .catch(error => displayError(error))
// }

// const divElement = document.querySelector("#results");

// function displayError (error) {
//     divElement.textContent = `ERROR TRY AGAIN`;
// }

// function displayRobots (robots) {
//     for (let robot of robots) {
//         const para = document.createElement("p");
//         const text = document.createTextNode(`the robot is ${robot.name}, its email is ${robot.email}`);
//         para.appendChild(text);
//         divElement.appendChild(para)
//     } 
// }
// function getData(){
//     fetch("https://api.giphy.com/v1/gifs/random?tag=sun&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My")
//     .then(result => {
//         if(result.ok){
//             return result.json()
//         }
//         else{
//             throw new Error("error")
//         }})
       
//     .then(data => {
//         console.log(data);
//         displayGif(data)
//     })
// }


// get gif
function displayGif(data){
    const div = document.getElementById('gif');
    const img = document.createElement('img')
    img.src = data["data"]["images"]["original"]["url"]
    div.appendChild(img)
    const body = document.querySelector('body');
    body.appendChild(div)
}

// get random word


function getWord(){
     fetch("http://random-word-api.herokuapp.com/word?number=1")
    .then(result => {
        if(result.ok){
            return result.json()}
        else{
            throw new Error("error")
        }}        
    )
        
    .then(data => {
        console.log(data[0]);
        let randomWord = data[0]
        return randomWord
    })
    
}

let word = getWord()

function getRandomGif(word){
    fetch(`https://api.giphy.com/v1/gifs/random?tag=${word}&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My`)
    .then(result => {
        return result.json()})
    .then(data => {
        console.log(data);
        displayGif(data)
    })
}

getRandomGif(word)


