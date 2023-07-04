// 🌟 Exercise 1 : Giphy API

function getData(){
    const url = "https://api.giphy.com/v1/gifs/search?q=hilarious&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My"
    fetch(url)
    .then(result => {
        if(result.ok){
            return result.json()
        }
        else{
            throw new Error('Something went wrong')
        }
    })
    .then(data =>{
        console.log('🌟 Exercise 1 : Giphy API');
        console.log(data)
    })
    .catch(error => {
        console.log("ERROR", error)
    })
}
getData();


// 🌟 Exercise 2 : Giphy API


function getData2(){

    const word = 'sun';
    const limit = 10;
    const offset = 2;
    const url = `https://api.giphy.com/v1/gifs/search?q=${word}&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My&limit=${limit}&offset=${offset}`
    fetch(url)
    .then(result => {
        if(result.ok){
            return result.json()
        }
        else{
            throw new Error('Something went wrong')
        }
    })
    .then(data =>{
        console.log('🌟 Exercise 2 : Giphy API');
        console.log(data)
    })
    .catch(error => {
        console.log("ERROR", error)
    })
}
getData2();


// 🌟 Exercise 3 : Async Function

// WAS
// fetch("https://www.swapi.tech/api/starships/9/")
//     .then(response => response.json())
//     .then(objectStarWars => console.log(objectStarWars.result));

// NOW
async function getStarship(){

    try{
        const respond = await fetch("https://www.swapi.tech/api/starships/9/")
        if(respond.ok){
            const data = await respond.json()
            console.log('🌟 Exercise 3 : Async Function');
            console.log(data.result)
        }
        else{
            throw new Error('Something went wrong')
        }
    }
    catch{
        console.log("ERROR", error)
    }

}

getStarship()

// 🌟 Exercise 4: Analyze

// the result of this function is word resolved after 2 second
function resolveAfter2Seconds() {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve('resolved');
        }, 2000);
    });
}

async function asyncCall() {
    console.log('calling'); // first we see this line in console "calling"
    let result = await resolveAfter2Seconds(); //after 2 second me get the result of resolveAfter2Seconds function = resolved
    console.log(result); //and console log word "resolved"
}
// So in console we see 
// calling
// resolved
asyncCall();