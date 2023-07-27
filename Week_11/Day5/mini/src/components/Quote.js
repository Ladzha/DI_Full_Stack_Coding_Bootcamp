import './style.css'
import quotes from './quotes'
import colors from './colors'
import {useState, useEffect} from 'react'


const Quote = ()=>{
    const [num, setNum] = useState(0)

    console.log(quotes.length);

    const random = ((min, max)=>{
        let random;
        do {
           random = Math.floor(Math.random()*(max-min+1));
        }while(
            random===num
        )
        return random;
    })
    
    const ranIndex =random(0, quotes.length);

    const handleClick= ()=>{
        setNum(ranIndex)
    }

    return(
        <div className="container" >
            <div className="card">
                <h3 className="quote">"{quotes[num].quote}"</h3>
                <p className="author">{quotes[num].author}</p>
                <button className="button" onClick={handleClick}>Generate</button>

            </div>
        </div>


    )

}

export default Quote