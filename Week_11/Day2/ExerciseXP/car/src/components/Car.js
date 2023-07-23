import {useState} from "react"
import Garage from './Garage.js'

const Car = (carInfo)=>

{
    const [color, setColor] = useState("black")
    
    console.log(carInfo)
    return(
        <div>
            <Garage size="small"/>
            <header>This car is a {color} {carInfo.carModel} </header>
        </div>
    )
}
export default Car