// Daily Challenge: Anagram

// Create a function that:
// takes in two strings as two parameters
// and returns a boolean that indicates whether or not the first string is an anagram of the second string.

const strArr = ['g', 'f', 'a', 'b', 'l']
// console.log(strArr.sort());
const str = 'hell   oa  ';

function compareStr(string1, string2){
    const strArr1 = string1.toLowerCase().split('').sort().join('').trim();
    const strArr2 = string2.toLowerCase().split('').sort().join('').trim();
    // console.log(strArr1);
    // console.log(strArr2);

    if(strArr1===strArr2){
        console.log(`${string1} is an anagram of ${strArr2}`)
    }
    else{
        console.log(`${string1} is NOT an anagram of ${strArr2}`)
    };

}

compareStr('Astronomer', 'Moon starer');
compareStr('School master', 'The classroom');
compareStr('The Morse Code', 'Here come dots');
compareStr('The Code', 'Here come dots');