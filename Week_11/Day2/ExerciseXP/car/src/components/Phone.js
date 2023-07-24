import {useState} from "react"

const Phone = ()=>{
    const [brand, setBrand] = useState("Samsung");
    const [model, setModel] = useState("Galaxy S20");
    const [color, setColor] = useState("black");
    const [year, setYear] = useState(2020);

    const changeColor = ()=>{
        setColor("blue")
    }


    return(
        <div>
            <h2>`My phone is {brand}`</h2>
            <h4>'It is <span style={{color: color}}>{color}</span> {model} from {year}'</h4>
            <button onClick={changeColor}>Change Color</button>
        </div>
    )
}


export default Phone