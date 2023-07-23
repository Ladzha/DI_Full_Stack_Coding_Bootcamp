import React from "react"
import './Exercise.css'

const style = {
    color: "red",
    backgroundColor: "lightblue"
}

const style_header = {
    color: "white",
    backgroundColor: "DodgerBlue",
    padding: "10px",
    fontFamily: "Arial"
  };

class Exercise extends React.Component{
    render(){
        return (<div>
            create a paragraph, a link, a form, an image and a list.
            <h1 style={style_header}>Hello</h1>
            <p class = {'para'} >This is a paragraph</p>
            <a href={"https://react.dev/learn/react-developer-tools"} >This is a link</a>
            <form>
                <label for="search">Enter your name</label> <br/>
                <input name="search"/>
                <button>Search</button><br/>
            </form>
            <img src={'https://robohash.org/5?size=150x150'}></img>
            <ul style={style} >This is a list
                <li>
                    Coffee
                </li>
                <li>
                    Tea
                </li>
                <li>
                    Milk
                </li>
            </ul>

        </div>

        )
    }
}

export default Exercise