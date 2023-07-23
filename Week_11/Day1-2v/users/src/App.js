import {useState} from "react"
import './App.css';

const handleClick = async (name)=>{
  console.log("Yep")
  // try{
  //   const res = await fetch('https://jsonplaceholder.typicode.com/users')
  //   const users = await res.json();
  //   console.log(users)
  //   setUsers(users)
  // }catch(err){
  //   console.log(err)
  // }
  name = 'Marry'
} 

const handleInput = (event)=>{

  const value = event.target.value;
  console.log(value)
}

function App() {
// const [state, setSate] = useState()
const [name, setName] = useState('John')
const [users, setUsers] = useState()

  return (
    <div className="App">

      <input type="text" onInput={(event)=>handleInput(event)}/>

      {/* <button onClick={()=>handleClick()}>Click</button> */}

      <button onClick={()=>setName("Sara")}>Click</button>
      <h1>{name}</h1>
    
    </div>
  );
}

export default App;
