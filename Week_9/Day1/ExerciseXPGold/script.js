
    const queryString = window.location.search;
    console.log(queryString);

    const urlParams = new URLSearchParams(queryString);
    console.log(urlParams);

    const firstName = urlParams.get('firstName')
    console.log(firstName);

    const lastName = urlParams.get('lastName')
    console.log(lastName);


    const data = `${firstName} ${lastName}`
    const content = document.createTextNode(data)
    const section = document.querySelector("section");
    section.appendChild(content);



