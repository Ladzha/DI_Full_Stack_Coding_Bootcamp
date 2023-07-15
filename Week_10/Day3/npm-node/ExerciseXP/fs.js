// Exercise 1 : Reading From A File In Node.JS
const fs = require('fs')
 fs.readFile('text.txt', 'utf-8', (err, data)=>{
    if(err) console.log(err);
    console.log(data);

 })

//  Exercise 2 : Writing Files With Node JS

fs.writeFile('newtext.txt', 'Nope still don\'t understand Node.js', (err)=>{
    if(err) console.log(err);
    else{
        console.log('Write operation complete.');
    }  
})

let newLine = 'But let\'s be optimistic..'

fs.appendFile('newtext.txt', '\n'+ newLine, (err)=>{
    if(err) console.log(err);
    else{
        console.log('Append operation complete.');
    }  
 })

 fs.unlink('delete.txt', (err)=>{
    if(err) console.log(err);
    else{
        console.log('Delete operation complete.');
    }  
 })