
let anserCorrect = false
function playTheGame(){     
    let answer=confirm('Would like to play the game?');
    let userNumber;
    let computerNumber;
    let counter = 0;
    if(answer) 
    {
        while(!anserCorrect){
            userNumber = parseInt(prompt('Enter a number between 0 and 10'));     
            if(isNaN(userNumber)){
                alert('Sorry Not a number, Goodbye');
            }else if(userNumber>10 || userNumber<0){
                alert('Sorry it\'s not a good number, Goodbye');
            }
            else {
            anserCorrect = true
            computerNumber =Math.floor(Math.random() * 11);
            console.log(computerNumber); 
            console.log(userNumber); 
            compareNumbers(userNumber, computerNumber)
            counter++;
            };
        }
    }

    else{
        alert('No problem, Goodbye');
    };

    if(counter>3){
        alert('Out of chances');
    }
};

function compareNumbers(userNumber, computerNumber){
    if(userNumber ===computerNumber){
        alert('WINNER');
    }
    else if (userNumber>computerNumber) {
        alert('Your number is bigger then the computer\'s, guess again');
    }
    else if(userNumber<computerNumber){
        alert('Your number is smaller then the computer\'s, guess again');
    }
};

playTheGame()