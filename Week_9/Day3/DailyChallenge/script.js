
const form = document.getElementById('myForm');
const deleteAllButton = document.getElementById('deleteAll');
const divContent = document.getElementById('content');

deleteAllButton.addEventListener('click', deleteAll)

function deleteAll(){
    divContent.innerHTML = ''
}

form.addEventListener('submit', getInput)

function getInput(event){
    event.preventDefault()
    const input = form["search"].value;
    console.log(input)
    getRandomGif(input)
}

function getRandomGif(word){
    fetch(`https://api.giphy.com/v1/gifs/random?tag=${word}&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My`)
    .then(result => {
        return result.json()})

    .then(data => {
        displayGif(data)
        console.log(data);
    })
}

function displayGif(data){
    const divForGif = document.createElement('div');
    const img = document.createElement('img')
    const deleteButton = document.createElement('button')
    deleteButton.textContent="Delete"
    deleteButton.addEventListener('click', deleteGif)
    img.src = data["data"]["images"]["original"]["url"]
    divForGif.appendChild(img);
    divForGif.appendChild(deleteButton);
    divContent.appendChild(divForGif);
    function deleteGif(divToDelete){
        divToDelete = divForGif
        divToDelete.remove()
    }
}
