import './App.css';
import Car from './components/Car.js';
import Events from './components/Events';


function App() {
  const carinfo = {name: "Ford", model: "Mustang"};
  return (
    <div className="App">

      <Car carModel={carinfo.model} />
      <Events/>

    </div>
  );
}

export default App;
