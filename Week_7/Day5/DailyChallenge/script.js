//99 Bottles of Beer

// let bottlesNumber = 99;

function songBottles(){
    let bottlesNumber = parseInt(prompt('Enter a number of bottles'));     
    let takenBottles = 1;
    let lyrics = '';
    let word = 'it'
    for(let i =0; i<99; i++){
        if(bottlesNumber<=0 || (bottlesNumber - takenBottles )<0){
            break
        }
        lyrics = `\n${bottlesNumber} bottles of beer on the wall
${bottlesNumber} bottles of beer
Take ${takenBottles} down, pass ${word} around
${bottlesNumber - takenBottles } bottles of beer on the wall`

        console.log(lyrics);
        
        bottlesNumber -=takenBottles;
        takenBottles++;
        if(takenBottles>1){
            word = 'them'
        }
    }
    console.log('No more bottles. You drink too much.')
}

songBottles();