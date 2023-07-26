import './App.css';
import React from 'react'
import ErrorBoundary from './ErrorBoundary'

class BuggyCounter extends React.Component {
  constructor() {
    super();
    this.state = { counter : 0 }
  }

  handleClick=()=>{

    this.state.counter++ 
    this.setState({counter: this.state.counter})

    
  }

  render() { 
    if(this.state.counter>=5){
      console.log("I crashed!");
      throw Error("I crashed!")
    } else {
      return (  

      <h2 onClick={this.handleClick}>Counter {this.state.counter}</h2>

    )};
  }
}
 
// export default ;

function App() {
  return (
    <div className="App">
      
      {/* Simulation 1: */}
        <ErrorBoundary>
             <BuggyCounter/>
             <BuggyCounter/>
        </ErrorBoundary>

      {/* Simulation 2: */}
        <ErrorBoundary>
             <BuggyCounter/>
        </ErrorBoundary>

        <ErrorBoundary>
             <BuggyCounter/>
        </ErrorBoundary>

        <BuggyCounter/>


    </div>
  );
}

export default App;
