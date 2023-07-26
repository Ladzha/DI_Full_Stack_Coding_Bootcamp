import './style.css'
import FormComponent from './FormComponent.js'
import {useState} from 'react'


function App() {
const [formInputs, setFormsinputs]=useState({
  fname:"",
  lname:"",
  age:"",
  gender:"",
  destination:"",
  nuts:"",
  lacto: "",
  vegan: ""
})

const handleChange = (event)=>{
  const name = event.target.name;
  const value = event.target.type ==="checkbox"? event.target.checked : event.target.value
  console.log(value);
  setFormsinputs({...formInputs, [name]:value})

}

const handleSubmit = (event)=>{
  // const form= event.target
  // const formData = new FormData(form)
  // event.preventDefault()

  // const query = new URLSearchParams(formData).toString();
  // console.log("query=>", query);
}

  return (
    <div className="App">
      <div className="formContainer">
        <h1>Sample form</h1>

        <form onSubmit ={(event)=>{handleSubmit(event)}} method="GET">

          <input type='text' onChange ={(event=>handleChange(event))} name="fname" placeholder='First Name'/><br/>
          <input type='text' onChange ={(event=>handleChange(event))} name="lname" placeholder='Last Name'/><br/>
          <input type='text' onChange ={(event=>handleChange(event))} name="age" placeholder='Age'/><br/>
          <label>Male</label><br/>
          <input type="radio" onChange ={(event=>handleChange(event))} name="gender" value='male'/><br/>
          <label>Female</label><br/>
          <input type="radio" onChange ={(event=>handleChange(event))} name="gender" value='female'/><br/>
          <label>Select your destination</label><br/>
          <select name="destination" onChange ={(event=>handleChange(event))}>
            <option value="Thailand">Thailand</option>
            <option value="Japan">Japan</option>
            <option value="Brazil">Brazil</option>
          </select><br/>
          <label>Dietary restrictions</label><br/>
          <input type="checkbox" onChange ={(event=>handleChange(event))} name="nuts" value="nut"/>
          <label>Nuts Free</label><br/>
          <input type="checkbox" onChange ={(event=>handleChange(event))} name="lacto" value="lacto"/>
          <label>Lactose Free</label><br/>
          <input type="checkbox" onChange ={(event=>handleChange(event))} name="vegan" value="vegan"/>
          <label>Vegan</label><br/>
          <input type="submit" value="Submit"/>
        </form>
      </div>
      <div className="info"> <FormComponent fname={formInputs.fname} lname ={formInputs.lname} age ={formInputs.age} gender = {formInputs.gender} destination={formInputs.destination} nuts={formInputs.nuts ? "Yes" : "No"} lacto={formInputs.lacto? "Yes" : "No"} vegan={formInputs.vegan? "Yes" : "No"} />
</div>
   
   </div>
  );
}

export default App;
