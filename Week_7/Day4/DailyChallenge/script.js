// Daily Challenge: Planets

let section = document.querySelector('section');

// 1 / Create an array which value is the planets of the solar system.
let planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune'];

const colors = ['red', 'yellow', 'blue', 'green', 'white', 'pink', 'lightblue']

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


//BONUD NOT FINISHED


// let moons = {
//     'Mercury': null,
//     'Venus': null,
//     'Earth': 'Moon', 
//     'Mars': ['Phobos', 'Deimos'],
//     'Jupiter': ['Io', 'Europa', 'Ganymede', 'Callisto'],
//     'Saturn': ['Titan', 'Enceladus', 'Mimas', 'Rhea'],
//     'Uranus': ['Miranda', 'Ariel', 'Umbriel', 'Titania', 'Oberon'],
//     'Neptune': ['Triton', 'Nereid', 'Proteus']
//     }



    let moons = [
        {'Mercury': []},
        {'Venus': []},
        {'Earth': ['Moon']}, 
        {'Mars': ['Phobos', 'Deimos']},
        {'Jupiter': ['Io', 'Europa', 'Ganymede', 'Callisto']},
        {'Saturn': ['Titan', 'Enceladus', 'Mimas', 'Rhea']},
        {'Uranus': ['Miranda', 'Ariel', 'Umbriel', 'Titania', 'Oberon']},
        {'Neptune': ['Triton', 'Nereid', 'Proteus']}
    ]

const colorsMoons = ['Indigo', 'Coral', 'Lavender', 'Turquoise', 'Maroon', 'Teal', 'Plum', 'Amber', 'Slate', 'Periwinkle', 'Mauve', 'Olive', 'Crimson', 'Sapphire', 'Apricot', 'Jade', 'Lilac', 'Chestnut', 'Emerald', 'Rosewood', 'Azure', 'Orchid', 'Brick', 'Coral', 'Cobalt', 'Papaya', 'Mulberry', 'Topaz', 'Sienna', 'Chartreuse']


    for(let i =0; i< moons.length; i++){
        console.log(moons[i])
        for(let j =0; j< moons[i].length; j++){
            console.log(j)

        }

        // let divMoon = document.createElement('div');
        // divMoon.classList.add('moon');
        // divMoon.style.backgroundColor=colorsMoons[i];
        // section.appendChild(divMoon); 

};