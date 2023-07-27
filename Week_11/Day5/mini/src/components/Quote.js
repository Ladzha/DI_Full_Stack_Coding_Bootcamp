import './style.css'
import quotes from './quotes'
import {useState, useEffect} from 'react'


const Quote = ()=>{
    const [num, setNum] = useState(0)
    const random = ((min, max)=>{
        return Math.floor(Math.random()*(max-min+1))+min;
    })
    
    const handleClick= ()=>{
        setNum(random(1,2)) 
    }

    return(
        <div className="card">
            <h3 className="quote">VOOOOV</h3>
            <p className="author">author</p>
            <button className="button" onClick={handleClick}></button>

        </div>

    )

}