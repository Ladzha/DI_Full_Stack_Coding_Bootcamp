import './App.css';
import UserFavoriteAnimals from './UserFavoriteAnimals'
import Exercise from './Exercise3'


const myelement = <h1>I Love JSX!</h1>
const sum = (5+5)

const user = {
  firstName: 'Bob',
  lastName: 'Dylan',
  favAnimals : ['Horse','Turtle','Elephant','Monkey']
};

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>Exercise 1</p>

        <p>Hello World!</p>
        <p>{myelement}</p>
        <p> {`React is ${sum} times better with JSX`}</p>

        <p>Exercise 2</p>
        <h3>{`First Name: ${user.firstName}. Last Name: ${user.lastName}`}</h3>
       <UserFavoriteAnimals favAnimals = {user.favAnimals} key = {user.id}/>
       
       <p>Exercise 3</p>
       <h4><Exercise/></h4>
        

      </header>
    </div>
  );
}

export default App;
