const promise1 = Promise.resolve(3);
const promise2 = 42;
const promise3 = new Promise((resolve, reject) => {
  setTimeout(resolve, 3000, 'foo');
});


// expected output: Array [3, 42, "foo"]

Promise.all([promise1, promise2, promise3])
.then((result)=>{
    console.log(result); 
})
.catch((error) =>console.log(error));

// Promise.all waits every promise to complete and execute them


// Exercise 2 : Analyse Promise.All()

//Get a argument and multiply to 2
function timesTwoAsync(x) {
    return new Promise(resolve => resolve(x * 2)); 
  }
  
  const arr = [1, 2, 3];
  //put to array of promises the result of timesTwoAsync function
  const promiseArr = arr.map(timesTwoAsync); 
  
  // get an array of promises and console log result of each promise
  Promise.all(promiseArr)
    .then(result => {
      console.log(result);
    });

