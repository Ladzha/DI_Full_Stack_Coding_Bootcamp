// // const object1 = {
// //     a: 'somestring',
// //     b: 42,
// //     c: false
// // };
// // console.log(Object.keys(object1))
// // //   const a = Object.fromEntries(object1)
// // //   console.log(a); 

// // const facts = {numPlanets: 8, yearNeptuneDiscovered: 1846};
// // const {numPlanets, yearNeptuneDiscovered} = facts;

// // console.log(numPlanets); // 8
// // console.log(yearNeptuneDiscovered); // 1846

// // let planetFacts = {
// //     numPlanets: 8,
// //     yearNeptuneDiscovered: 1846,
// //     yearMarsDiscovered: 1659
// //   };
  
// // let {numPlanets, ...discoveryYears} = planetFacts;
  
// //   console.log(discoveryYears); // {  yearNeptuneDiscovered: 1846, yearMarsDiscovered: 1659 }


// function getDetails(name, house, goodstudent) {

// 	console.log(name, house, goodstudent)
// }

// getDetails({name: 'Harry Potter',house: 'Gryfindor',goodstudent : false})


// function getDetails2(obj) {
//     const {name, house, goodstudent} =obj

// 	console.log(name, house, goodstudent)
// }

// getDetails2({name: 'Harry Potter',house: 'Gryfindor',goodstudent : false})



// // Modify the code below, and destructure the object in the parameter (ie. you should have 4 parameters : name, house, friendName and age)

// // function getMoreDetails( name, house, friend : {friendName, age}) {
// // 	console.log(name, house, friend )
// // }

// // Modify the code below, and destructure the object in the parameter (ie. you should have 4 parameters : firstname, lastname, locationOne, locationTwo, valueHouses)

// getMoreDetails(
// 			{name: 'Hermione Granger', 
// 				house: 'Gryfindor', 
// 				friend :  {
// 					friendName : 'Harry Potter', age : 20
// 				}
// 			})

//             const elonPerson = {
//                 first: 'Elon',
//                 last: 'Musk',
//                 housesLocation : ["new york", "paris"],
//                 twitter: '@elonmusk',
//                 company: 'Space X',
//                 houses : {
//                   amount: 2,
//                   value : "5Million"
//                 }
//             }
            
//             function getElonMuskDetails(/*FillInHere*/){
//                 console.log(firstname, lastname)
//                 console.log(locationOne, locationTwo, valueHouses)
            
//             }
            
//             getElonMuskDetails(elonPerson)

// class Wizard {
//     constructor (name, power, life=100) {
//         this.wizardName = name;
//         this.power = power;
//         this.life = life
//     }

//     fight (otherwizard) {
//         this.life -= 10;
//         otherwizard.life -= 100
//     }

//     showWizard () {
//         const sentence = `The wizard ${this.wizardName} has ${this.life} life point`
//         console.log(sentence);
//     }
// }

// const wizard1 = new Wizard("John", "fly", 200);
// wizard1.showWizard()
// wizard1.fight()
// wizard1.showWizard()
// const wizard2 = new Wizard("Emma", "read mind", 300);
// wizard2.showWizard()
// wizard1.showWizard()
// wizard2.fight(wizard1)
// wizard2.showWizard()
// wizard1.showWizard()

// class DeveloperWizard extends Wizard {
//     constructor (name, power,programminglanguage, life) {
//         super(name, power, life)
//         this.language = programminglanguage;
//     }

//     showWizard () {
//         const sentence = `The wizard ${this.wizardName} has ${this.life} life point and code in ${this.language}`
//         console.log(sentence);
//     }
// }

// const wizard3 = new DeveloperWizard("Tom", "code","Javascript")
// console.log(wizard3);
// wizard3.showWizard()


// Part I
// Create a TV function constructor with 3 parameters : brand, channel and volume Channel should be 1 by default. Volume should be 50 by default.
// Create properties brandTV, channelTV and volumeTV equal to the 3 parameters value.
// Add methods to increase and decrease volume. When the methods are called it will increase or decrease the volume by 1.
// Create an object for the LG TV
// Call the inscrease method, and check if the volume changed
// Part II
// Create a subclass for Smart TV
// It overrides the method increase, so it increase the volume by 10 and not by 1
// Add a attribute of Netflix that should be equal to true by default


class TV{
    constructor(brand, channel=1, volume =50){
        this.brandTV = brand,
        this.channelTV = channel,
        this.volumeTV = volume
    }

    decreaseVolume(){
        this.volumeTV -=1;
    } 
    increaseVolume(){
        this.volumeTV +=1;
    } 
}

const LGTV = new TV('LG')
console.log(LGTV['volumeTV']);
LGTV.decreaseVolume();
console.log(LGTV.volumeTV);


class SmartTV extends TV{
    constructor(brand, channel, volume, Netflix=true){
        super(brand, channel, volume)
        this.Netflix = Netflix;
    }

    increaseVolume(){
        this.volumeTV +=10;
    } 
}

const smart = new SmartTV('Smart')
console.log(smart['volumeTV']);
smart.increaseVolume();
console.log(smart.volumeTV); 