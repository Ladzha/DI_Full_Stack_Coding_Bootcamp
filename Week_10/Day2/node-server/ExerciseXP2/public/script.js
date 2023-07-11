fetch('/users')
.then(response => response.json())
.then(data =>{
    console.log(`I am data from script file ${data}`);
    const divForData = document.getElementById('obj')
    divForData.innerText = JSON.stringify(data)
    console.log(data);

})
.catch(error =>{
    console.log(error)
}) 


fetch('/:id')
.then(response => response.json())
.then(data =>{
    console.log(`I am data from script file ${data}`);
    const divIdData = document.getElementById('iddata')
    divIdData.innerText = JSON.stringify(data)
    console.log(data);

})
.catch(error =>{
    console.log(error)
})


const button = document.getElementById('button')
button.addEventListener('click', showMessage)

function showMessage(){
    alert('Click on me')
}