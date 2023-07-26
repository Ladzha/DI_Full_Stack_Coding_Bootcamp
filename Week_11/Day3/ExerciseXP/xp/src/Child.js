import React from 'react'

class Child extends Component {
    constructor(props) {
        super(props);
    }
    state = {  }

    update=()=>{
        alert("")
    }
    render() { 
        return (

            <div>
                <h1>Hello Wold</h1>
                <button onClick ={update}>Delete Header</button>
            </div>


         );
    }
}
 
export default Child;