const form = document.getElementById('form')

form.addEventListener('submit', sendFunc)

function sendFunc(event)
{ event.preventDefault()
    const email = form.elements.email.value;
    const message = form.elements.message.value;
    console.log(`Form submit. Email: ${email} Message: ${message}`);

    const body = {
        email: email,
        message: message
    };

    const options = {
        method: "POST",
        headers: {
            "Content-type": "application/json"
        },
        body: JSON.stringify(body)
    };

    fetch('/formData', options)
    .then((res)=> res.json)
    .then((res)=>console.log(res)
    .catch((er)=>console.log(er))
}