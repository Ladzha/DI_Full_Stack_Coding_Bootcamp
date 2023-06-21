let allBooks = [{
    title: 'House of Many Ways',
    author: 'Diana Wynne Jones',
    image: 'https://m.media-amazon.com/images/I/51Gx3EpWqbL._SX333_BO1,204,203,200_.jpg',
    alreadyRead: true
},
{
    title: 'The Two Dianas',
    author: 'Alexandre Dumas',
    image: 'https://d3525k1ryd2155.cloudfront.net/h/344/533/72533344.0.m.jpg',
    alreadyRead: false
}
]

const section = document.querySelector('section');

for (let i = 0; i< allBooks.length; i++){

    const div =document.createElement('div')
    const p1 =document.createElement('p');
    const p2 =document.createElement('p');
    const p3 =document.createElement('p');


    const img =document.createElement('img');
    img.src = allBooks[i].image;
    img.setAttribute('width', '100px');
    const alreadyRead = document.createTextNode(allBooks[i].alreadyRead);
    const aboutBook = document.createTextNode(`${allBooks[i].title} written by ${allBooks[i].author}`);

    p1.appendChild(aboutBook);
    p2.appendChild(img);
    p3.appendChild(alreadyRead);

    div.appendChild(p1);
    div.appendChild(p2);
    div.appendChild(p3);

    section.appendChild(div);

    if(allBooks[i].alreadyRead ==true){

    p1.style.color = 'red';
    }
    else{
        p1.style.color = 'blue'
    };
}



