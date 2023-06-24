//Exercice 4 : Volume Of A Sphere
// Write a JavaScript program to calculate the volume of a sphere. Use the code below as a base:

// 1  - get radius from user

function getInput(){
    let radiusInput = parseFloat(document.getElementById('radius').value);

    if(!isNaN(radiusInput)){
        return radiusInput;
    }
    else{
        alert('Enter a radius')
        document.getElementById("MyForm").reset();  
        return false
    }
};

// 2 - calculate volume of a sphere by formula - V = 4/3 π r³

function calculateVolume(radius){
    let volumeOfSphere = (4/3 * Math.PI * Math.pow(radius, 3)).toFixed(3);
    return volumeOfSphere
};

// 3 - display result

const form = document.getElementById('MyForm')

function displayVolume(event){
    let volumeInput = document.getElementById('volume');
    let radius = getInput();
    if(radius){
        volumeInput.value = calculateVolume(radius);
        console.log(volume.value);
    };
    event.preventDefault();
}

form.addEventListener('submit', displayVolume);


