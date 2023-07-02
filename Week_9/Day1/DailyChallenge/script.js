const form = document.getElementById("myForm")


form.addEventListener('submit', retrieveData)

function retrieveData(event){
    event.preventDefault()
    const firstName =form.elements.namedItem("firstName");
    const lastName = form.elements.namedItem("lastName");
    if(firstName != '' && lastName != '' ){

        const data = {name: firstName.value, lastname: lastName.value}
        console.log(form.elements)
        console.log(firstName.value)
        console.log(lastName.value)
        const text = JSON.stringify(data);
        const content = document.createTextNode(text)
        const div = document.createElement('div');
        div.appendChild(content);
        const body = document.querySelector("body");
        body.appendChild(div);

    }
    else{
        alert("Enter you name and last name")
    }



}