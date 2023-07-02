// 🌟 Exercise 1 : HTML Form

const formGet = document.getElementById("formGet");
const nameGet = formGet.elements.namedItem("name");
const commentsGet = formGet.elements.namedItem("comments");

console.log(formGet);
console.log(nameGet);
console.log(commentsGet);
 
//Data appear in the url


//🌟 Exercise 2 : HTML Form #2

const formPost = document.getElementById("formPost");
const namePost = formPost.elements.namedItem("name");
const commentsPost = formPost.elements.namedItem("comments");

console.log(formPost);
console.log(namePost);
console.log(commentsPost);

 
//Data appear in the data body

// 🌟 Exercise 3 : JSON Mario

const marioGame = {
    detail : "An amazing game!",
    characters : {
        mario : {
          description:"Small and jumpy. Likes princesses.",
          height: 10,
          weight: 3,
          speed: 12,
        },
        bowser : {
          description: "Big and green, Hates princesses.",
          height: 16,
          weight: 6,
          speed: 4,
        },
        princessPeach : {
          description: "Beautiful princess.",
          height: 12,
          weight: 2,
          speed: 2,
        }
    },
}

const strMarioGame = JSON.stringify(marioGame)
const strMarioGamePretty  = JSON.stringify(marioGame, null, 2)

const objMarioGame = JSON.parse(strMarioGame)

console.log(strMarioGame);
console.log(strMarioGamePretty);
console.log(objMarioGame);