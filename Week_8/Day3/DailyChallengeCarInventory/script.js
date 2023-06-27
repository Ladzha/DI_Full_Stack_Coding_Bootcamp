// Daily Challenge: Car Inventory

const inventory = [
    { id: 1, car_make: "Lincoln", car_model: "Navigator", car_year: 2009 },
    { id: 2, car_make: "Mazda", car_model: "Miata MX-5", car_year: 2001 },
    { id: 3, car_make: "Honda", car_model: "Accord", car_year: 1983 },
    { id: 4, car_make: "Land Rover", car_model: "Defender Ice Edition", car_year: 2010 },
    { id: 5, car_make: "Honda", car_model: "Accord", car_year: 1995 },
];

function getCarHonda(carInventory){
    const carHonda = carInventory.find(element=>{
        return element.car_make=="Honda"
    })
    let str = `This is a ${carHonda.car_make} ${carHonda.car_model} from ${carHonda.car_year}`;
    console.log(carHonda);
    console.log(str);
}
getCarHonda(inventory)

function sortCarInventoryByYear(carInventory){
    carInventory.sort((a, b) => a.car_year - b.car_year);
    console.log(carInventory);
}

sortCarInventoryByYear(inventory)