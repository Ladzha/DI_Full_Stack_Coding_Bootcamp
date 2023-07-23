import logo from './logo.svg';
import './App.css';
import Hello from './hello.js';
import users from './users.json';
import User from './components/User';

//PROPS

// const users = [
//   {name: 'Marry', age: 4},
//   {name: 'Carl', age: 8},
//   {name: 'Gill', age: 5},
// ]



function App() {
  return (
    <div className="App">
      {/* <header className="App-header">
        {
          users.map(item=>{
            return <Hello name={item.email} age = {item.age}/>
          })
        }
        <Hello name = "John" age="3"/>

        <Hello name ={users[0].name} age={users[1].email}/>


      </header> */}

      {users.map((item, inx)=>{
            return <User userinfo={item} key = {item.id}/>
      })}

    </div>
  );
}

export default App;
