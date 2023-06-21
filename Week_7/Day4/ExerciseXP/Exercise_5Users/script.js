//#2.1 Retrieve the div and console.log it
let div = document.querySelector("div");
console.log(div);2

//#2.1 Change the name “Pete” to “Richard”.
document.querySelector('ul > li:last-child').innerHTML="Richard";


//List of Ul
const listOfUl = document.querySelectorAll('ul')

//Ul №1
const firstdUl=listOfUl[0];
//Ul №2
const secondUl=listOfUl[1];

//Ul №1 Li №1
const firstdUlfirstLi = firstdUl.firstElementChild;
//Ul №1 Li last
const firstdUllasttLi = firstdUl.lastElementChild;

//Ul №2 Li №1
const secondUlfirstLi = secondUl.firstElementChild;

//Ul №2 Li №2
const secondUlsecond = secondUl.children[1];

//Ul №2 Li last
const secondUllasttLi = secondUl.lastElementChild;

// console.log('******* LIST OF UL *******')
// console.log(listOfUl); 

// console.log('******* FIRST UL *******')
// console.log(firstdUl);

// console.log('******* SECOND UL *******')
// console.log(secondUl);

// console.log('******* FIRST UL FIRST LI *******')
// console.log(firstdUlfirstLi);

// console.log('******* FIRST UL LAST LI *******')
// console.log(firstdUllasttLi);


// console.log('******* SECOND UL FIRST LI *******')
// console.log(secondUlfirstLi);

// console.log('******* SECOND UL SECOND LI *******')
// console.log(secondUlsecond);

// console.log('******* SECOND UL LAST LI *******')
// console.log(secondUllasttLi);

//#2.3 Delete the <li> that contains the text node “Sarah”. (It’s the second <li> of the second <ul>).

secondUl.removeChild(secondUlsecond)

//#2.4 Change each first name of the two <ul>'s to your name. (Hint : use a loop)

const toChangeAll=document.querySelectorAll('ul > li:first-child')

for(let el of toChangeAll){
    el.textContent='Alla'
};

//#3.1 Add a class called student_list to both of the <ul>'s.

// listOfUl => List of ul 
for(ul of listOfUl){
    ul.classList.add('student_list')
};

//#3.2 Add the classes university and attendance to the first <ul>.
listOfUl[0].classList.add('university', 'attendance')

//#4.1 Add a “light blue” background color and some padding to the <div>.

div.style.backgroundColor = 'lightblue';
div.style.padding = '20px';

//#4.2 Do not display the <li> that contains the text node “Dan”. (the last <li> of the first <ul>)

secondUllasttLi.style.display = 'none';

//#4.3 Add a border to the <li> that contains the text node “Richard”. (the second <li> of the <ul>)
firstdUllasttLi.style.border = "thick solid #0000FF";

//#4.4 Change the font size of the whole body.
document.body.style.fontSize = '20px';
