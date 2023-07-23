import {useState} from "react"
const Events = ()=>{

    const [isToggleOn , setToggle] = useState(true)
    const [buttonText , setButtonText] = useState('ON')
    const [buttonCollor, setbuttonCollor] = useState('red')

    const onOff = ()=>{
        if(isToggleOn===true){
            setToggle(false)
            setButtonText("OFF")
            setbuttonCollor('green')
            // buttonText = "ON"
        }
        else{
            setToggle(true)
            setButtonText("ON")
            setbuttonCollor('red')
            // buttonText = "OFF"
        }     
        console.log(isToggleOn);
    }

    const clickMe = ()=>{
        alert('I was clicked')
    }

    const handleKeyDown = (event) =>{
        const input = document.getElementById('input').value

        if(event.code==='Enter'){
            alert(`The Enter key was pressed, your input is "${input}!"`)

        }

        console.log("Input", input);


        console.log(event.key);
        console.log(event.code==='Enter');

    } 
    
    return(
        <div>
            <button onClick={clickMe}>Click me</button>
            <input onKeyDown={handleKeyDown} placeholder="Press the Enter key" id="input"/>
            <button style ={{backgroundColor:buttonCollor}} onClick={onOff}>{buttonText}</button>
            <p>{isToggleOn}</p>

        </div>
        
    )
}


export default Events