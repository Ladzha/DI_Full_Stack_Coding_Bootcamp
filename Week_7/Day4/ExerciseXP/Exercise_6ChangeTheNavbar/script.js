
//Using Javascript, in the <div>, change the value of the id attribute from navBar to socialNetworkNavigation, using the setAttribute method.

let div = document.querySelector('div');
console.log(div);

div.setAttribute('navBar', 'socialNetworkNavigation');

//3. add a new <li> to the <ul>
// 3.1. First, create a new <li> tag (use the createElement method).
const newli = document.createElement("li");
// 3.2. Create a new text node with “Logout” as its specified text.
const newText = document.createTextNode('Logout');
//3.3. Append the text node to the newly created list node (<li>).
newli.appendChild(newText);
//3.4. Finally, append this updated list node to the unordered list (<ul>), using the appendChild method.
const navBar = document.querySelector('ul');
navBar.appendChild(newli);

//4
console.log(navBar.firstElementChild.textContent);
console.log(navBar.lastElementChild.textContent);