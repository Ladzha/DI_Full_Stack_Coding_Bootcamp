let index = 3;
const quotes = [
    { id:0, author:"Steve Jobs" , quote:"The only way to do great work is to love what you do."},
    { id:1, author:"Winston Churchill" , quote:"Success is not final, failure is not fatal: It is the courage to continue that counts."},
    { id:2, author:"Eleanor Roosevelt" , quote:"The future belongs to those who believe in the beauty of their dreams."},
    { id:3, author:"Albert Einstein" , quote:"In the middle of difficulty lies opportunity."},
]


const button = document.getElementById("button")

button.addEventListener("click", showQuote)

let currentRandomNumber = 0;

function showQuote(){
    const content =document.getElementById("content");

    content.textContent = ''

    let randomNumber = Math.floor(Math.random()*(index+1));

    while (currentRandomNumber===randomNumber){
        randomNumber = Math.floor(Math.random()*(index+1));
    }
    currentRandomNumber = randomNumber;

    console.log(randomNumber);
    const author =quotes[randomNumber].author
    console.log(author);
    const quote =quotes[randomNumber].quote
    console.log(quote);

    const quoteText = document.createTextNode(quote);
    const authorText = document.createTextNode(author);
    
    const divForQuote = document.createElement('div');
    divForQuote.classList.add("quote")
    const divForAuthor = document.createElement('div');
    divForAuthor.classList.add("author")
    divForQuote.appendChild(quoteText)
    divForAuthor.appendChild(authorText)
    content.appendChild(divForQuote)
    content.appendChild(divForAuthor)
}


const form = document.getElementById("myForm");
const inputAuthor = form.elements.namedItem("newAuthor");
const inputQuote =form.elements.namedItem("newQuote");


form.addEventListener("submit", addNewQuote)
function addNewQuote(event){
    event.preventDefault();
    index++;
    const newQuote = {id:index, author: inputAuthor.value, quote: inputQuote.value}
    quotes.push(newQuote);
    console.log(quotes);
    console.log(newQuote);
}


