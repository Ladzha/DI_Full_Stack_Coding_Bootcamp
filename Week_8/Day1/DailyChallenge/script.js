// Tell The Story
// Get the value of each of the inputs in the HTML file when the form is submitted. Remember the event.preventDefault()
// Make sure the values are not empty
// Write a story that uses each of the values.
// Make sure you check the console for errors when playing the game.
// Bonus: Add a “shuffle” button to the HTML file, when clicked the button should change the story currently displayed (but keep the values entered by the user). The user could click the button at least three times and get a new story. Display the stories randomly.


// GET RANDOM NUMBER
function randomNumber(){
    const randomNum = Math.floor(Math.random() * (2 - 0 + 1) + 0);
    return randomNum;
}

const arr = [];

// GET RANDOM STORY
function chooseStory(){
    document.getElementById('story').innerText='';

    let stories = [
        `Once upon a time, there was a ${arr[0]} named ${arr[1]} who lived in a ${arr[4]} house in ${arr[3]}. One day, ${arr[1]} decided to ${arr[2]} to the top of a mountain in ${arr[3]}. The journey was ${arr[4]}, but ${arr[1]} was determined to reach the summit. As ${arr[1]} climbed, the view became ${arr[4]}. Finally, ${arr[1]} reached the peak and admired the ${arr[3]} below. After descending, ${arr[1]} shared their adventure, inspiring others to explore and conquer their own mountains.`, 
        `In a bustling ${arr[3]}, there was a curious ${arr[0]} named ${arr[1]}. Their vibrant ${arr[4]} apartment was filled with books and artwork. One sunny morning, ${arr[1]} decided to ${arr[2]} to a serene park nearby. The walk was refreshing, and ${arr[1]} embraced the ${arr[4]} scenery. As they strolled, ${arr[1]} encountered a friendly ${arr[0]}, sparking a delightful conversation. After bidding farewell, ${arr[1]} returned home, cherishing the unexpected encounter and the joy of exploration.`, 
        `Deep within a mystical ${arr[3]}, a whimsical ${arr[0]} named ${arr[1]} resided in a cozy ${arr[4]} cottage. One magical evening, ${arr[1]} ventured out to ${arr[2]} under the twinkling stars. As they gazed at the night sky, a shooting star streaked across, fulfilling ${arr[1]}'s secret wish. Filled with wonder, ${arr[1]} whispered their hopes to the enchanting forest, feeling the embrace of nature\'s energy. With renewed spirit, ${arr[1]} returned home, carrying the forest\'s magic within their heart.`];
    
    let storyNumber = randomNumber();
    let newStory = stories[storyNumber]
    displayStory(newStory)
};

//GENERATE A STORY
function getValues(event){
    event.preventDefault();
    let form = document.forms.libform;
    let noun = form.elements.noun.value;
    let adjective = form.elements.adjective.value;
    let person = form.elements.person.value;
    let verb = form.elements.verb.value;
    let place = form.elements.place.value;
    if(noun !='' && adjective !='' && person !='' && verb !='' && place !=''){
        arr.push(noun, person, verb, place, adjective)
        chooseStory();
    }
    else{
        alert('Fill each field');
        return false;
    };
};

function displayStory (story) {
    let placeForStory = document.getElementById('story')
    let storyText = document.createTextNode(story)
    placeForStory.appendChild(storyText)
}

document.forms.libform.addEventListener('submit', getValues);

let shuffleButton = document.getElementById('shuffle');

shuffleButton.addEventListener('click', function(){
    chooseStory()
});
