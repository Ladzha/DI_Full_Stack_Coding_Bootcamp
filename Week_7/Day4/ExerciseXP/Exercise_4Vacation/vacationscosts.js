console.log('Exercise 4 : Vacations Costs');
console.log('***********************');

function hotelCost(numberOfNights){

    let hotelPrice = numberOfNights *140;
    return hotelPrice;

};

function planeRideCost(destination){

    let planeTickets;

    if(destination == 'London'){
        planeTickets = 183;
    }
    else if(destination == 'Paris') {
        planeTickets = 220;
    }
    else{
        planeTickets = 300;
    };

    return planeTickets;

};

function rentalCarCost(amountOfDays){
    let carPrice =0;
    if(amountOfDays>10){
        carPrice = (amountOfDays*40) - (amountOfDays*40/100*5);
    }
    else{
        carPrice = amountOfDays*40;
    }
    return carPrice;
};

let vacationCost = 0;
function totalVacationCost(){

    let numberOfNights =2;
    let amountOfDays = 11;
    let destination = 'London';

    do {
        numberOfNights = prompt('Enter the number of nights you would like to stay in hotel: ')
    }
    while(isNaN(numberOfNights));

    do {
        amountOfDays = prompt('Enter the number of days you would like to rent the car: ')
    }
    while(isNaN(amountOfDays));

    do {
        destination = prompt('Enter destination: ')
    }
    while(typeof(destination)==='srtring');


    let hotelPrice = hotelCost(numberOfNights);
    let carPrice = rentalCarCost(amountOfDays);
    let planeTickets = planeRideCost(destination);

    vacationCost = hotelPrice + carPrice + planeTickets;

    console.log(`The hotel cost: ${hotelPrice} the car cost: ${carPrice}, the plane tickets cost: ${planeTickets}. Total: ${vacationCost}`);
};

totalVacationCost();