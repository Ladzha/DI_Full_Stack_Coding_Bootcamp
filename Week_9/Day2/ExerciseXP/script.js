// 🌟 Exercise 1 : Comparison

function compareToTen(num) {
    const promise = new Promise((resolve, reject) => {
        if(num <= 10){
            resolve(`${num} is less or equal to 10`) 
        }
        else{
            reject(`${num} is greater than 10`)
        }
        
    })
    return promise
}

compareToTen(15)
.then(result => console.log(result))
.catch(error => console.log(error))


compareToTen(7)
.then(result => console.log(result))
.catch(error => console.log(error))


// 🌟 Exercise 2 : Promises

const promise2 = new Promise((resolve) => {
    setTimeout(() => resolve(console.log('I am resolve')), 4000);
})


// 🌟 Exercise 3 : Resolve & Reject

const promise3 = Promise.resolve(3)

promise3.then((value) => {
    console.log(value);
})


const promise4 = Promise.reject('Boo!')

promise3.catch((error) => {
    console.log(error);
})