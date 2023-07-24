import React from 'react'

class Test extends React.Component{
    constructor(){
        super()
        this.state={title: 'Test'}
        console.log("Hi");

    }

    // componentWillUnmount
    

    componentDidMount =()=>{
        console.log("render");
    }

    componentDidUpdate =()=>{

        console.log("change");

    }

    handle=()=>{
        console.log("onChange")
    }

    render(){
        return(
            <div>

                <h1>
                    {this.state.title}
                </h1>
                {/* <input onChange={handle}/> */}

                

            </div>

        )
    }
}

export default Test