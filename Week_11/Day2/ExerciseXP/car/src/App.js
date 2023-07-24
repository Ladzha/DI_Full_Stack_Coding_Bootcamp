import './App.css';
import Car from './components/Car.js';
import Events from './components/Events';
import Phone from './components/Phone';
import Color from './components/Color';


function App() {
  const carinfo = {name: "Ford", model: "Mustang"};
  return (
    <div className="App">

      <Car carModel={carinfo.model} />
      <Events/>
      <Phone/>
      <Color/>

    </div>
  );
}

export default App;
