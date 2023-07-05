function showInfo(characterName, height, gender, birthYear, homeWorld){

    const content = document.getElementById("content")
    content.innerHTML="";
    const paragraphName = document.createElement('p')
    paragraphName.classList.add('name')
    paragraphName.textContent = characterName
    content.appendChild(paragraphName);
    
    const paragraphHeight = document.createElement('p')
    paragraphHeight.textContent = `Height: ${height}`
    content.appendChild(paragraphHeight);
    
    const paragraphGender = document.createElement('p')
    paragraphGender.textContent = `Gender: ${gender}`
    content.appendChild(paragraphGender);
    
    const paragraphBirth = document.createElement('p')
    if(birthYear=='unknown'){
        birthYear = "We don't know the exact year"
    }
    paragraphBirth.textContent = `Birth Year: ${birthYear}`
    content.appendChild(paragraphBirth);
    
    const paragraphHome = document.createElement('p')
    if(homeWorld=='unknown'){
        homeWorld = "We don't know the exact planet"
    }
    paragraphHome.textContent = `Home World: ${homeWorld}`
    content.appendChild(paragraphHome);
}

const button = document.querySelector('button', showAll)

button.addEventListener("click", getCharacter)

function getRandomNumber(){
    const randomNumber = Math.floor(Math.random()*84)
    return randomNumber;
}

function loading(){

    const content = document.getElementById("content")
    content.innerHTML="";
    const divAnimation = document.createElement('div')
    const imgAnimation = document.createElement('img')

    const paragraphLoading = document.createElement('p')
    paragraphLoading.classList.add('loading')
    paragraphLoading.textContent = "Loading"
    content.appendChild(paragraphLoading);
    imgAnimation.src = 'spin.svg'
    divAnimation.appendChild(imgAnimation)
    content.appendChild(divAnimation);
}

async function getCharacter(){
    loading()

    let randomNumber = getRandomNumber();
    try {
        const response = await fetch(`https://www.swapi.tech/api/people/${randomNumber}`)

        if(response.ok){
            const characterInfo = await response.json()

            const characterName = characterInfo["result"]["properties"]["name"];
            const height = characterInfo["result"]["properties"]["height"];
            const gender = characterInfo["result"]["properties"]["gender"];
            const birthYear = characterInfo["result"]["properties"]["birth_year"];
            const planetUrl = characterInfo["result"]["properties"]["homeworld"];

            const homeWorld = await getPlanet(planetUrl)    
            showInfo(characterName, height, gender, birthYear, homeWorld);
        }
        else{
            throw new Error('OH NO! THIS PERSON IS NOT AVAILABLE!')
        }
    }
    catch(error){
        const content = document.getElementById("content")
        content.innerText = error;
        console.log("error");
    }
}

function showAll(event){
    event.preventDefault()
    getCharacter()
}

async function getPlanet(url){
    try {
        const response = await fetch(url)
        if(response.ok){
            const planetInfo = await response.json()
            const homeWorld = planetInfo["result"]["properties"]["name"];
            return homeWorld
        }
        else{
            throw new Error('OH NO! THIS PLANET IS NOT AVAILABLE!')
        }
    }
    catch(error){
        const content = document.getElementById("content")
        content.innerText = error;
        console.log("error");
    }
}