const robots = [
    {
      id: 1,
      name: 'Leanne Graham',
      username: 'Bret',
      email: 'Sincere@april.biz',
      image: 'https://robohash.org/1?200x200'
    },
    {
      id: 2,
      name: 'Ervin Howell',
      username: 'Antonette',
      email: 'Shanna@melissa.tv',
      image: 'https://robohash.org/2?200x200'
    },
    {
      id: 3,
      name: 'Clementine Bauch',
      username: 'Samantha',
      email: 'Nathan@yesenia.net',
      image: 'https://robohash.org/3?200x200'
    },
    {
      id: 4,
      name: 'Patricia Lebsack',
      username: 'Karianne',
      email: 'Julianne.OConner@kory.org',
      image: 'https://robohash.org/4?200x200'
    },
    {
      id: 5,
      name: 'Chelsey Dietrich',
      username: 'Kamren',
      email: 'Lucio_Hettinger@annie.ca',
      image: 'https://robohash.org/5?200x200'
    },
    {
      id: 6,
      name: 'Mrs. Dennis Schulist',
      username: 'Leopoldo_Corkery',
      email: 'Karley_Dach@jasper.info',
      image: 'https://robohash.org/6?200x200'
    },
    {
      id: 7,
      name: 'Kurtis Weissnat',
      username: 'Elwyn.Skiles',
      email: 'Telly.Hoeger@billy.biz',
      image: 'https://robohash.org/7?200x200'
    },
    {
      id: 8,
      name: 'Nicholas Runolfseedottir V',
      username: 'Maxime_Nienow',
      email: 'Sherwood@rosamond.me',
      image: 'https://robohash.org/8?200x200'
    },
    {
      id: 9,
      name: 'Glenna Reeichert',
      username: 'Delphine',
      email: 'Chaim_McDermott@dana.io',
      image:'https://robohash.org/9?200x200'
    },
    {
      id: 10,
      name: 'Clementina DuBuque',
      username: 'Moriah.Stanton',
      email: 'Rey.Padberg@karina.biz',
      image:'https://robohash.org/10?200x200'
    }
    ];

function showCards(){
  robots.forEach(element =>{
   let {id, name, username, email, image} = element;
   createCard(name, email, image);
  })

}

showCards();

function createCard(name, email, image){

  const paragraphName = document.createElement('p');
  paragraphName.classList.add('robot-name');
  const robotNameText = document.createTextNode(name);
  paragraphName.appendChild(robotNameText);

  const paragraphEmail = document.createElement('p');
  paragraphEmail.classList.add('email');
  const robotEmailText = document.createTextNode(email);
  paragraphEmail.appendChild(robotEmailText);

  const imgRobot = document.createElement('img');
  imgRobot.classList.add('robot-img');
  imgRobot.setAttribute('src', image)

  const divCardContent = document.createElement('div');
 divCardContent.classList.add('card-content');
 divCardContent.appendChild(imgRobot);
 divCardContent.appendChild(paragraphName);
 divCardContent.appendChild(paragraphEmail);

  const divCard = document.createElement('div');
  divCard.classList.add('card');
  divCard.appendChild (divCardContent);
 

  const divContent = document.getElementById('row-content');
  divContent.appendChild(divCard);
};

const row = document.getElementById('row-content');
let inputUser = document.getElementById('search');

function searchRobot(event){
  event.preventDefault();
  row.innerHTML ='';
    if(inputUser.value !=''){
      console.log(inputUser.value);

    robots.forEach(element =>{
      // console.log(element.name);
      let {id, name, username, email, image} = element;
        if(name.toLowerCase().includes(inputUser.value.toLowerCase())){
          
          createCard(name, email, image);
      };


    });

  }
  else{
    showCards()
  }

};

inputUser.addEventListener('input', searchRobot);
