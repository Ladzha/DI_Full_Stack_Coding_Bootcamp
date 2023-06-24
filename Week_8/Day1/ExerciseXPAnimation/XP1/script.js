// 🌟 Exercise 1: Timer

// Part I
// In your Javascript file, using setTimeout, call a function after 2 seconds.
// The function will alert “Hello World”.

function helloWold(){
    alert('Hello world')
};

setTimeout(helloWold, 2000);

// Part II
// In your Javascript file, using setTimeout, call a function after 2 seconds.
// The function will add a new paragraph <p>Hello World</p> to the <div id="container">.
let paragraphCounter = 0;
let timer = setInterval(addParagraph, 2000);
function clearInter(){
    clearInterval(timer)
}

function addParagraph(){
    let div = document.getElementById('container');
    let text = document.createTextNode('Hello World');
    let paragraph = document.createElement('p');
    paragraph.appendChild(text);
    div.appendChild(paragraph);
    paragraphCounter++;
    if(paragraphCounter==5){
        clearInter();
        console.log('Now there are 5 paragraphs in the div');
    }
}

setTimeout(addParagraph, 2000);

// Part III
// In your Javascript file, using setInterval, call a function every 2 seconds.
// The function will add a new paragraph <p>Hello World</p> to the <div id="container">.
// The interval will be cleared (ie. clearInterval), when the user will click on the button.
// Instead of clicking on the button, the interval will be cleared (ie. clearInterval) as soon as there will be 5 paragraphs inside the <div id="container">.

let clearButton = document.getElementById('clear');

clearButton.addEventListener('click', clearInter)