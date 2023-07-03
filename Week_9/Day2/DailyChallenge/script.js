// Daily Challenge: Play With Words
// 1rst Daily Challenge

function makeAllCaps(words){

    const promise1 = new Promise((resolve, reject)=>{

       if(words.every((element)=> typeof element == "string")){
        const newarr = words.map(element => element.toUpperCase())
        resolve(newarr)
       }
       else{
        reject('Something went wrong')
       }
    })
    return promise1
}

function sortWords(words){
    const promise2 = new Promise((resolve, reject)=>{

        if(words.length > 4){
            resolve(words.sort())
        } 
        else{
            reject('Something went wrong with reason')
        }  
    })

    return promise2
}

// Test

// //in this example, the catch method is executed
// makeAllCaps([1, "pear", "banana"])
//       .then((arr) => sortWords(arr))
//       .then((result) => console.log(result))
//       .catch(error => console.log(error))

// //in this example, the catch method is executed
// makeAllCaps(["apple", "pear", "banana"])
//       .then((arr) => sortWords(arr))
//       .then((result) => console.log(result))
//       .catch(error => console.log(error))

// //in this example, you should see in the console, 
// // the array of words uppercased and sorted
// makeAllCaps(["apple", "pear", "banana", "melon", "kiwi"])
//       .then((arr) => sortWords(arr))
//       .then((result) => console.log(result)) //["APPLE","BANANA", "KIWI", "MELON", "PEAR"]
//       .catch(error => console.log(error))


// 2nd Daily Challenge

const morse = `{
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
}`

//this part works
function toJs(morse){

    const promise3 = new Promise((resolve, reject) => {

        const morseObject = JSON.parse(morse)

        if(Object.keys(morseObject).length != 0){
            resolve(morseObject)
        }
        else{
            reject('The object is empty')
        }
    })

    return promise3
}

function toMorse(morseJS){

    const input = prompt('Enter a word or a sentence');
    const morseArray =[];
    const promise4 = new Promise((resolve, reject) => {
    
        for(let letter of input){

            if(Object.keys(morseJS).includes(letter)){
                morseArray.push(morseJS[letter])
            }
            else{
                reject('A character that doesn\'t exist')
            }
        }

        resolve(morseArray) });

    return promise4
}

//this part works
function joinWords(morseTranslation){
    const finalText = morseTranslation.join('\n');
    const body = document.querySelector('body');
    const text = document.createTextNode(`RESULT:  ${finalText}`);
    const div = document.createElement('div');
    div.appendChild(text);
    body.appendChild(div);
}

toJs(morse)
    .then((result) => {
        console.log(result)
        return toMorse(result)
    })
    .then((resultmorse) => {
        console.log(resultmorse)
        joinWords(resultmorse)
    })
    .catch(error => console.log(error))
    .finally(() => console.log("It works!!!"))
