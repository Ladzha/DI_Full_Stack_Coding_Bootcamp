// Create a curried function, that returns the volume of an object the volume is calculated like this length * weight * height
// Call the function twice, for products of length 10cm. Weight and Height can differ
// Call the function twice, for products of length 10cm and weight 2 grams, height can differ

function returnVolume(length){
    return function(weight){
        return function (height){
            const value = length*weight*height
            return value
        }
    }
}

const returnVolume1 = (length)=>(weight) =>(height)=>length*weight*height

const length = returnVolume(10)

console.log(length(3)(5));

console.log(length(9)(2));

const weight = length(2)
console.log(weight(5));
console.log(weight(3));


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

// console.log(strMarioGame);
// console.log(strMarioGamePretty);
// console.log(objMarioGame);

const copyMarioGame = JSON.parse(JSON.stringify(strMarioGame));



let jsonString = `
{
    "quiz": {
        "sport": {
            "q1": {
                "question": "Which one is correct team name in NBA?",
                "options": [
                    "New York Bulls",
                    "Los Angeles Kings",
                    "Golden State Warriros",
                    "Huston Rocket"
                ],
                "answer": "Huston Rocket"
            }
        },
        "maths": {
            "q1": {
                "question": "5 + 7 = ?",
                "options": [
                    10,
                    11,
                    12,
                    13
                ],
                "answer": 12
            },
            "q2": {
                "question": "12 - 8 = ?",
                "options": [
                    1,
                    2,
                    3,
                    4
                ],
                "answer": 4
            }
        }
    }
}`


const objJ =JSON.parse(jsonString);
console.log(objJ);
console.log(objJ);

for(el of objJ["quiz"]["sport"]["q1"]["options"]){
    console.log(el);
}

const srtJ = JSON.stringify(objJ, null, 2);
console.log(srtJ);

// 🌟 Exercise 1 : HTML Form

const formGet = document.getElementById("formGet");
const nameGet = formGet.elements.namedItem("name");
const commentsGet = formGet.elements.namedItem("comments");

console.log(nameGet);
console.log(commentsGet);



//🌟 Exercise 2 : HTML Form #2

const formPost = document.getElementById("formPost");
const namePost = formPost.elements.namedItem("name");
const commentsPost = formPost.elements.namedItem("comments");

console.log(namePost);
console.log(commentsPost);

// formPost.addEventListener("submit", sendDataPost);


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