import logo from './logo.svg';
import './App.css';
import User from "./Users" 
import Button from '@mui/material/Button';
import Product from "./components/Product";

const products = [{id:1, name: "IPhon", price: 300},
  {id:2, name: "IPad", price: 900},
  {id:3, name: "IWatch", price: 600}]

function App() {
  return (
    <div className="App">
      <header className="App-header">

        {products.map((item) => {
          return <Product key={item.id} name = {item.name} price = {item.price}/>
        })}

        <User/>
        <Button variant="outlined">Outlined</Button>

        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
