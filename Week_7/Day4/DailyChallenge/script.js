// Daily Challenge: Planets

let section = document.querySelector('section');

// 1 / Create an array which value is the planets of the solar system.
let planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'];

const colors = ['lightgreen', 'yellow', 'blue', 'green', 'white', 'pink', 'lightblue', 'orange']

// 2 / For each planet in the array, create a <div> using createElement. This div should have a class named "planet".

// 3 / Each planet should have a different background color. (Hint: you could add a new class to each planet - each class containing a different background-color).

// 4 / Finally append each div to the <section> in the HTML (presented below).

for(let i =0; i< planets.length; i++){

    const planetName = document.createTextNode(planets[i])
    const paragraph = document.createElement('p')
    paragraph.appendChild(planetName)

    const divForPlanet = document.createElement('div');
    divForPlanet.appendChild(paragraph)

    divForPlanet.classList.add('planet', colors[i]);
    divForPlanet.style.backgroundColor=colors[i];
    section.appendChild(divForPlanet); 
};


//BONUS


    let moons = [
        {planet: 'Mercury', moon: []},
        {planet: 'Venus', moon: []},
        {planet: 'Earth', moon: ['Moon']}, 
        {planet: 'Mars', moon: ['Phobos', 'Deimos']},
        {planet: 'Jupiter', moon: ['Io', 'Europa', 'Ganymede', 'Callisto']},
        {planet: 'Saturn', moon: ['Titan', 'Enceladus', 'Mimas', 'Rhea']},
        {planet: 'Uranus', moon: ['Miranda', 'Ariel', 'Umbriel', 'Titania', 'Oberon']},
        {planet: 'Neptune', moon: ['Triton', 'Nereid', 'Proteus']}
    ]

const colorsMoons = ['Indigo', 'Coral', 'Lavender', 'Turquoise', 'Maroon', 'Teal', 'Plum', 'yellow', 'darkgreen', 'darkred', 'darkblue', 'Olive', 'Crimson', 'lightyellow', 'green', 'gray', 'violet', 'gold', 'lightgray', 'Azure', 'Orchid', 'Brick', 'Coral', 'Cobalt', 'Papaya', 'Mulberry', 'Topaz', 'Sienna', 'Chartreuse']

console.log(moons.planet);

    let index = 0;

    for(let i =0; i< moons.length; i++){
        let planet = moons[i].planet;
        let moonList = moons[i].moon;

        const planetName = document.createTextNode(planets[i])
        const paragraph = document.createElement('p')
        paragraph.appendChild(planetName)
    
        const divForPlanet = document.createElement('div');
        divForPlanet.appendChild(paragraph)
        divForPlanet.style.position += 
    
        divForPlanet.classList.add('planet', colors[i]);
        divForPlanet.style.backgroundColor=colors[i];
        section.appendChild(divForPlanet); 

        for(let j=0; j< moonList.length; j++){
            console.log(moonList[j])
            const moonName = document.createTextNode(moonList[j])
            const paragraphMoon = document.createElement('p')
            paragraphMoon.appendChild(moonName)
        
            const divForMoon = document.createElement('div');
            divForMoon.appendChild(paragraphMoon)
        
            console.log("color", colorsMoons[index], "moon", moonList[j]);

            divForMoon.classList.add('moon', colorsMoons[index]);
            divForMoon.style.backgroundColor=colorsMoons[index];
            divForMoon.style.position = 'relative';
            divForMoon.style.left = '150 px';
            section.appendChild(divForMoon); 
            index+= 1;
        }

};
