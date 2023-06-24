//Exercise 5 : Event Listeners
// 1 / Add many events listeners to one element on your webpage. Use the click, mouseover, mouseout and dblclick events.
// 2 / Each listener should do a different thing, for instance - change position x, change position y, change color, change the font size… and more.

const buttonTest = document.querySelector('button');

buttonTest.addEventListener("mouseover", (event) => {
    buttonTest.style.color='blue'; 
    buttonTest.innerText = 'SecretText';});

buttonTest.addEventListener("mouseout", (event) => {
    buttonTest.style.color = 'black';
    buttonTest.innerText = 'Test'});

buttonTest.addEventListener("mouseup", (event) => {buttonTest.style.backgroundColor ='red';});

buttonTest.addEventListener("mousedown", (event) => {buttonTest.style.fontSize = '20px'; buttonTest.style.opacity = 0.4});

buttonTest.addEventListener("click", (event) => {
    buttonTest.style.position='absolute';
    buttonTest.style.left = '40px'});

buttonTest.addEventListener("dblclick", (event) => {
    buttonTest.style.opacity = 1;
    buttonTest.style.backgroundColor = 'yellow';
    buttonTest.style.width = '20rem';
});
