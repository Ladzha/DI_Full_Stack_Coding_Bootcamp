import { useState, useEffect } from "react";

const Color =()=>{
    const [favoriteColor, setFavoriteColor ] = useState('red')
    const changeFavoriteColor =()=>{
        setFavoriteColor("blue")
    }

    useEffect(()=>{
        alert("useEffect reached")
        setFavoriteColor("yellow")

    },[])

    return(
        <div>
            <header>My Favorite Color is {favoriteColor}</header>
            <button onClick={changeFavoriteColor}>Change Favorite Color</button>
            
        </div>
    )
}

export default Color