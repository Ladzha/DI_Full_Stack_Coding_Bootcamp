// console.log('lol');
// let arr = ['tiger', 'cat', 'dog', 'bear', 'bird']
// console.log(arr);
// arr.splice(1,'ferret', 'rabbit');
// console.log(arr);
// let arrSlice=arr.slice(0, 4)
// console.log(arrSlice);
// const arrStr  = arr.join('*');
// console.log(arrStr);
// console.log(arr.shift())
// console.log(arr)
// console.log(arr.unshift('puma'))
// console.log(arr)
// console.log(arr.pop());
// console.log(arr);
// arr.push('lion', 'ferret', 'fish');
// console.log(arr.push());
// console.log(arr);
// console.log(arr.concat())
// console.log(arr)
// console.log(arr.sort())
// console.log(arr)
//  for(let i =0; i<arr.length; i++){
//     console.log(arr[i])
//  };

// arr.forEach(function(animal, i)
// {
//     console.log(i)
// });


// arr.forEach(animal =>
// {
//     console.log(animal)
// });

// function animalCount(animal, i){
//     console.log('Animal: ' + animal + ' - index - ' + i)
// }

// arr.forEach(animalCount);

// for of

// for (animal of arr){
//     console.log('New loop: for of ' + animal)
// }

// for in

// for (animal of arr){
//     console.log('New loop: for in ' + animal)
// }

// let obj = {
//     firstName : "Sarah",
//     lastName : "Smith",
//     isSingle : true
// }

// let today = new Date();
// console.log(today)

// today.setDate(today.getDate() + 5);
// console.log(today)


// let newDay = new Date(2023, 4, 11);
// console.log(newDay)

// let str = "Hello Everyone, please say hello to the class ";
// console.log(str.indexOf('the'));

// console.log(str.substring(0, 5));
// console.log(str.slice(0, 5));
// console.log(str.toLocaleLowerCase());
// let myStr = str.toLocaleUpperCase()
// console.log(myStr);
// let myNewStr= myStr.replace('THE', 'BOOOP');
// console.log(myNewStr);

// let text = str.concat('*****', myStr);
// console.log(text);

// let text1 = "      Hello World!      ";
// let text2 = text1.trim();
// console.log(text1);
// console.log(text.charAt(0));

// let op = 10.6789
// console.log(op.toFixed(0));
// console.log(op.toFixed(3));


const fruits = ["melon", "pear", "apple"];

// i want to create 1 li per fruit and add it to the ul

//1. retrieve the ul
const container = document.getElementById("all_fruits");

for (let fruit of fruits) {
    //2. create the li
    const newLi = document.createElement("li");
    //3. create the text
    const text = document.createTextNode(fruit);
    //4. append the text to the li
    newLi.appendChild(text);
    //5. append the li to the ul
    container.appendChild(newLi);
}

// // console.log(document);
// // let div = document.querySelector("div");
// // console.log(div);
// // let il = document.querySelector('ul > li:last-child').innerHTML="Richard";
// // console.log(il);
// // let arr = document.querySelectorAll('ul > li');

// // document.body.firstElementChild.textContent = 'Greate';

// // let username = 'John';
// // let s = document.body.firstElementChild;
// // console.log(arr);
// // console.log(arr);
// // for(let element of arr){
// //     if(element==='Sara'){
// //         console.log(element)
// //     }
    
// // }
// // // let name = document.getElementById("container").innerHTML="Good"

// // document.body.style.backgroundColor = 'pink';

// const div = document.createElement('div');
// const paragrath = document.createElement('p');
// const content = document.createTextNode('Hello my darling!');

// paragrath.classList.add('ocean');

// document.body.appendChild(div)
// div.appendChild(paragrath);
// paragrath.appendChild(content);


// const us = document.body.firstElementChild;
// console.log(us)

// const us3 = document.body.children[0];
// console.log(us3)

// const us2 = document.querySelector('div');
// console.log(us2)

// const ul = document.body.firstElementChild.nextElementSibling;
// console.log(ul)

// const ul2 = document.body.children[1];
// console.log(ul2)

// const li = ul2.lastElementChild
// console.log(li)

// const li2 = ul2.children[1]
// console.log(li2)

// const allli = document.getElementsByTagName('li')
// console.log(allli)

// const w = document.getElementsByClassName('sun')
// console.log(w)


// <div class="sun">Users:</div>
// <ul>
//   <li>John</li>
//   <li>Pete</li>
// </ul>

// <style>
//   .ocean {
//       background-color: lightblue;
//       border: 1px solid black;
//       margin : 2rem;
//       padding : 2rem
//   }

//   .sun {
//       background-color: yellow;
//       border: 1px solid black;
//       margin : 2rem;
//       padding : 2rem
//   }
// </style>