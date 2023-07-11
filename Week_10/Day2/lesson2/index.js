// const http = require('http');

// const server = http.createServer((request, response) =>{
//     console.log('get');
//     response.end("hello")
// })

// server.listen(3001, ()=>{
//     console.log('run on 3001');
// })

const express = require('express');

const { products } = require('./config/data.js');

const app = express();


// parse application/x-www-form-urlencoded
app.use(express.urlencoded({ extended: true }))

// parse application/json
app.use(express.json())


app.use('/', express.static(__dirname+'/public'))

app.get('/about', (req, res) => {
    res.sendFile(__dirname+'/public/about.html')
})


app.listen(3001, () =>{
    console.log("server listen");
})

// get one products
app.get('/api/products', (req, res) => {
    res.json(products)
})

// get one product with id

app.get('/api/products/:id', (req, res) => {
    console.log(req.params);
    const productid = req.params.id;  
    const product  = products.find((item) => item.id ==productid)
    if(!product) return res.status(404).json({msg: "Product not found"})
    res.json(product)

})

// search request search  a product with quary 

app.get('/api/search', (req, res) => {
    console.log(req.query);
    const name = req.query.name;  
    const filtered  = products.filter((item) => {
        return item.name.toLowerCase().includes(name.toLowerCase());      
        })
        
    if(filtered.length ===0) {
        return res.status(404).json({msg: "No product match in search"})
    }       
    res.json(filtered)
})

//create post request {"name":iKey, "price":900}

app.post('/api/products', (req, res) =>{
    
   console.log(req.body); 
   products.push(req.body)
   res.json(products)

})


// UPDATE one product with id as params json as body

app.put('/api/products/:id', (req, res) => {
    console.log(req.params);
    const id = req.params.id;  
    const index  = products.findIndex((item) => item.id ==id)
    if(index===-1) return res.status(404).json({msg: "Not Found: no such index"})
    products[index] = {...products[index], name: req.body.name, price: req.body.price,}
    
    res.json(products)
})


// delete product

app.delete('/api/products/:id', (req, res) => {
    const id = req.params.id;  
    const index  = products.findIndex((item) => item.id ==id)
    if(index===-1) return res.status(404).json({msg: "Not Found: no such index"})
    products.splice(index, 1)
    res.json(products)
})