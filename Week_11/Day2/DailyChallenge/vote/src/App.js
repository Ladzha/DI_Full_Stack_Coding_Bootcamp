import './style.css';
import {useState} from "react"

function App() {

  const [languages, setLanguages] = useState([
    {name: "Php", votes: 0},
    {name: "Python", votes: 0},
    {name: "JavaSript", votes: 0},
    {name: "Java", votes: 0}
  ])

  const changeVote = (languageFromMap)=>{

    //we should put here an array of objects and return array of objects
    setLanguages(arrayLanguage=>{
      return arrayLanguage.map(oneLanguage=>{
      if(oneLanguage.name === languageFromMap.name){
        oneLanguage.votes = oneLanguage.votes +1
        console.log("hi")
        return oneLanguage
      }
      else{
        console.log("wt")
        return oneLanguage}
      })
    })
  }
  

  const arrLanguages = languages.map((item, index)=>{
    return <button key ={index}> {item.votes} {item.name} <span className='clickText' onClick ={()=> changeVote(item)} >Click here</span> </button>
  })


  return (
    <div className="App">

    {arrLanguages}

    </div>
  );
}


export default App;
