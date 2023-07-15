const { error } = require('console');
const fs = require('fs');

fs.readFile('RightLeft.txt', 'utf-8', (error, data) =>{
    if(error)console.log(error)
    else{
        const dataArr = data.split('')
        check(dataArr)
        // console.log(dataArr)
    }
    
})


function check(text){

    let position = 1;
    let numberOfSteps =0;
    let count = 0;
    for(let i =0; i<text.length; i++){

        if(text[i]=='>'){
            position++;
        }
        else{
            position--;
        }
        if(position == -1 && count == 0){
            count++
            console.log(`The number of steps needed to hit position the -1 for the first time ${numberOfSteps} `)

        }
        numberOfSteps ++;

    }
    console.log(`${position} steps to the right`)

}