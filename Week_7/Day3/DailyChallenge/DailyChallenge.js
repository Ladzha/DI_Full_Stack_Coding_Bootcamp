let sentence = 'The movie is not that bad, I like it.';
let wordNot =sentence.indexOf('not');
let wordBad =sentence.indexOf('bad');

console.log(wordNot);
console.log(wordBad);

if (wordNot < wordBad){
    let newSentence =  sentence.replace('not that bad', 'good')
    console.log(newSentence)
}
else{
    console.log(sentence);
};

