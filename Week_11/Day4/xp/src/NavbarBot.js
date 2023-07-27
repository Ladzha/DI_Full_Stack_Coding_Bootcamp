import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import { BrowserRouter, Routes, Route, NavLink, Link,  Router } from "react-router-dom";


function NavbarBot() {
  return (
    <>

      <Navbar bg="primary" data-bs-theme="dark">
        <Container>
          <Nav className="me-auto">
            <Nav.Link ><Link to="/">Home</Link></Nav.Link>
            <Nav.Link ><Link to="/profile">Profile</Link></Nav.Link>
            <Nav.Link ><Link to="/shop">Shop</Link></Nav.Link>
          </Nav>
        </Container>
      </Navbar>

      <br />

    </>
  );
}

export default NavbarBot;