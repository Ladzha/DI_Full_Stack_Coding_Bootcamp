// 🌟 Exercise 1 : Change The Article
//1 / Using a DOM property, retrieve the h1 and console.log it.

let h1 = document.querySelector('h1');
console.log(h1);


//2 / Using DOM methods, remove the last paragraph in the <article> tag.

let article = document.querySelector('article');
let lastParagrath = article.lastElementChild
article.removeChild(lastParagrath);

//3 / Add a event listener which will change the background color of the h2 to red, when it’s clicked on.

let h2 = document.querySelector('h2');

h2.addEventListener('click', function(){
    h2.style.backgroundColor = 'red'
});

//4 / Add an event listener which will hide the h3 when it’s clicked on (use the display:none property).

let h3 = document.querySelector('h3');

h3.addEventListener('click', function(){
    h3.style.display = 'none'
});

//5 / Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.

let paragraphList = document.querySelectorAll('p');
let buttonText = document.createTextNode('Let\'s change!');
let button = document.createElement('button');
button.appendChild(buttonText);
article.appendChild(button);

button.addEventListener('click', function(){

    for(let paragraph of paragraphList){
        paragraph.style.fontWeight = "900";
    };
})

//6 /  BONUS : When you hover on the h1, set the font size to a random pixel size between 0 to 100.(Check out this documentation);

h1.addEventListener('mouseover', function(){
    let random = Math.floor(Math.random() * 101);
    console.log(random)
    h1.style.fontSize = `${random}px`;
    
});


//7 /  BONUS : When you hover on the 2nd paragraph, it should fade out (Check out “fade css animation” on Google)
let secondParagrath = document.getElementById('fade');

secondParagrath.addEventListener('mouseover', function(){
    secondParagrath.style.opacity = 0;
});

secondParagrath.addEventListener('mouseout', function(){
    secondParagrath.style.opacity = 1;
});