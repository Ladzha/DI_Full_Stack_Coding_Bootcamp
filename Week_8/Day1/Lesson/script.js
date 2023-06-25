// Exercise 1 - basic add event listener
// Create two buttons - id of "red", id of "blue"
// When we click on the red button -> Change the backgroundcolor of the page to red
// When we click on the blue button -> Change the backgroundcolor of the page to blue

// Exercise 2 - using the event object
// const colors = ["blue", "yellow", "green", "pink"];
// Add inside the HTML file a div of id "container" (do it directly in the HTML)
// Add one button per color inside the div container (do it directly in the JS)
// Each button should have an "click" event listener that changes the background color of the document, to the color of the button (do it directly in the JS)/


let pics = ["https://images.pexels.com/photos/1741205/pexels-photo-1741205.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260", "https://images.pexels.com/photos/2253275/pexels-photo-2253275.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260", "https://images.pexels.com/photos/3439576/pexels-photo-3439576.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260" ];
// Using this array, create a button on the page that when clicked on display 3 animals, but the order of the picture should be random
// Set a class to the image, so each image will be 200px height, and width, and in the middle of the page
// Add a button next to each image
// When we click on one image, it should disappear(ie. be deleted),
// When we hover on the image, it should display the "alt".

let div = document.getElementById('container')
let bIText = document.createTextNode('Image');
let buttonImg = document.createElement('button');
buttonImg.appendChild(bIText)

for(el of pics){
    let newImg = document.createElement('img');
    newImg.setAttribute('src', el)
    div.appendChild(newImg)
}
div.appendChild(buttonImg)


buttonImg.addEventListener('click', function(){
    
})


let blueButton = document.getElementById('blue')
let redButton = document.getElementById('red')

blueButton.addEventListener('click', changeColor);
redButton.addEventListener('click', changeColor);

const colors = ["blue", "yellow", "green", "pink"]

for(el of colors){
    let newButton = document.createElement('button');
    let text  = document.createTextNode(el)
    newButton.setAttribute('id', el)
    newButton.setAttribute('value', el)
    newButton.appendChild(text)
    newButton.addEventListener('click', changeColor)
    div.appendChild(newButton)
}




function changeColor(event){
    let color = event.target.value
    document.body.style.backgroundColor = color;
    console.log(color)
}


// document.forms[0].elements.user
// <input type=​"text" id=​"username" name=​"user">

// document.forms[0].elements.username
// <input type=​"text" id=​"username" name=​"user">

// document.querySelector('[name="user"]')
// <input type=​"text" id=​"username" name=​"user">

// document.forms[0].elements