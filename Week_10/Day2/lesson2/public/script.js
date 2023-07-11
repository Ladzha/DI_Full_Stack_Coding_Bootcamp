fetch('/api/products')
.then((response) =>response.json())
.then((data) =>{
    console.log(data);
    render(data);
})
.catch((error)=>{
    console.log(error);
})

const render =(arr) =>{
    const html = arr.map((item) =>{
        return `<div>
        <h2>${item.name}<h2>
        <h4>${item.price}<h4>
        <div>`
    });
    console.log(html);
    document.getElementById("root").innerHTML = html.join("");
};