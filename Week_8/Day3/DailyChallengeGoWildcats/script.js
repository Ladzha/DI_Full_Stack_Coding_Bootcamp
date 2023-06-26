// Create an array using forEach that contains all the usernames from the gameInfo array, add an exclamation point (ie. “!”) to the end of every username.
// The new array should look like this :
// const usernames = ["john!", "becky!", "susy!", "tyson!"]


// 2. Create an array using forEach that contains the usernames of all players with a score bigger than 5.
// The new array should look like this :

// const winners = ["becky", "susy"]


// 3. Find and display the total score of the users. (Hint: The total score is 71)

const gameInfo = [
    {
      username: "john",
      team: "red",
      score: 5,
      items: ["ball", "book", "pen"]
    },
    {
      username: "becky",
      team: "blue",
      score: 10,
      items: ["tape", "backpack", "pen"]
    },
    {
      username: "susy",
      team: "red",
      score: 55,
      items: ["ball", "eraser", "pen"]
    },
    {
      username: "tyson",
      team: "green",
      score: 1,
      items: ["book", "pen"]
    },
];

//Not used methods
const userNames = [];
gameInfo.forEach(function(element){
  userNames.push(element.username+'!')
});
console.log(userNames);

const winners = []
gameInfo.forEach(function(element){
    if(element.score>5){
      winners.push(element.username);
    }
});
console.log(winners);

let total =0;
gameInfo.forEach(function(element){  
    total+= element.score;  
});
console.log(`The total score is ${total}`);


//With map method
const mapUsers = gameInfo.map((element)=> {
  return element.username+'!'});
console.log(mapUsers);

//With filter method

const coolUsersFilter=gameInfo.filter((element) => element.score>5);

const coolUsers = [];
coolUsersFilter.forEach((element) => {
  coolUsers.push(element.username);
});
console.log(coolUsers);

//With reduce method
const totalScore = gameInfo.reduce((accumulator, num) => {
    return accumulator+num.score}, 0);

console.log(`The total score is ${totalScore}`);
