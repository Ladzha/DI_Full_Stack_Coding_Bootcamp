import express from 'express';
import { _register } from '../controllers/userController.js'

import { _login } from '../controllers/userController.js'


const u_router = express.Router(); // kogda ispolsuem structur proekta
u_router.post('/register', _register)

u_router.post('/login', _login)

export default u_router