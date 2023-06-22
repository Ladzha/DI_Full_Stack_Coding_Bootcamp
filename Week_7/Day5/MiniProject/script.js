//#1
function getConfirmation(){
    let play=confirm('Would like to play the game?');
    if(!play)
    {
        alert('No problem, Goodbye');
        return false;
    }
    else{
        return true;
    }
}
//#2
function getInput(){
    let anserCorrect = false;
    while(!anserCorrect){
        userNumber = parseInt(prompt('Enter a number between 0 and 10'));     
        if(isNaN(userNumber)){
            alert('Sorry Not a number, try again');
        }else if(userNumber>10 || userNumber<0){
            alert('Sorry it\'s not a good number, try again');
        }
        else {
            anserCorrect = true
        };
    };
    return userNumber;
}

//#3
function getComputerNumber(){
    let computerNumber =Math.floor(Math.random() * 11);
    return computerNumber;
}

//#4
function compareNumbers(userNumber, computerNumber){
    console.log(userNumber);
    console.log(computerNumber);

    if(userNumber ===computerNumber){
        alert('WINNER');
        return true;
    }
    else if (userNumber>computerNumber) {
        alert('Your number is bigger then the computer\'s, guess again')
        return false;
    }
    else if(userNumber<computerNumber){
        alert('Your number is smaller then the computer\'s, guess again');
        return false;
    }
};

//#5
function playTheGame(){  //all together
    if(getConfirmation()){
        for (var i = 0; i < 3; i++) {
            let userNumber=getInput();
            let computerNumber=getComputerNumber()
           if(compareNumbers(userNumber, computerNumber)){
            break;
           } 
        }
        alert('Game over');
    };
};

