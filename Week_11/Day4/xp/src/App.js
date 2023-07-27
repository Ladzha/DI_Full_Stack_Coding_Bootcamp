import "./App.css";
import {BrowserRouter, Routes, Route, NavLink, Link, Router,
} from "react-router-dom";
import NavbarBot from "./NavbarBot";
import "bootstrap/dist/css/bootstrap.min.css";
import data from "./data.json";
import data2 from "./data2.json";

import ErrorBoundary from "./ErrorBoundary ";
import Example1 from "./Example1";
import Example2 from "./Example2";
import Example3 from "./Example3";

import PostList from "./PostList.js";

function HomeScreen() {
  return <header>Home</header>;
}
function ProfileScreen() {
  return <header>Profile Screen</header>;
}
function ShopScreen() {
  return <header>Shop</header>;
}

const info = {key1: 'myusername',
              email: 'mymail@gmail.com',
              name: 'Isaac',
              lastname: 'Doe',
              age: 27}

const fun = async (info)=>{

  try {
    const res = await fetch("https://webhook.site/55aaaeda-d1db-48fe-9f16-8c95434c38e3", {

        method: "POST",
        headers:{
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(info)
      })

    
    console.log(res);
    
  } catch (error) {
    console.log(error)
    
  }

}
    

function App() {
  console.log(data);
  const parseData = JSON.parse(JSON.stringify(data2));
  console.log(parseData);

  return (
    <div className="App">
      <Routes>
        <Route
          path="/"
          element={
            <ErrorBoundary>
              <HomeScreen />
            </ErrorBoundary>
          }
        />
        <Route
          path="/profile"
          element={
            <ErrorBoundary>
              <ProfileScreen />
            </ErrorBoundary>
          }
        />
        <Route
          path="/shop"
          element={
            <ErrorBoundary>
              <ShopScreen />
            </ErrorBoundary> }/>
      </Routes>
      <NavbarBot />
    <h1>Exercise 2 : Display JSON Data In React JS</h1>
      <PostList data={data} />
    <h1>Exercise 3 : Display JSON Data And Parse It</h1>
      <Example1 data2={parseData} />
      <Example2 data2={parseData} />
      <Example3 data2={parseData} />
      <h1>Exercise 4 : Post JSON Data With React JS</h1>
      <button onClick={()=>fun(info)}>click me</button>
      
    </div>
  );
}

export default App;
