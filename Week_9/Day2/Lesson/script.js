function myFunc(data){
    const promise = new Promise((resolve, reject)=> {
    setTimeout(() => {
        if(typeof data == "string" ){
            resolve(data.toUpperCase())
        } else{
            reject(data)
        }
    }, 5000)
    
    })
    return promise
}
    
myFunc("hhh")

.then((result)=> console.log(result, result))
.catch((error)=>console.log(error))
.finally(() => console.log("congratulation"))

