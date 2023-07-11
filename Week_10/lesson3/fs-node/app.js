const fs = require('fs').promises;
console.log('before');

const read = async()=>{
    const data = await fs.readFile('info.json', 'utf-8')
    console.log(data);
}

/*
update info json

// */

// fs.readFile('info.json', 'utf-8', (err, data)=>{
//     if(err) return console.log(err);
//     const products = JSON.parse(data);
//     const index = products.findIndex((item) => item.id ==3);
//     products[index] = {
//         ...products[index],
//         price:700,
//     }
//     fs.writeFile('info.json', JSON.stringify(products), 'utf-8', (err, data)=>{
//         if(err) return console.log(err);
        
//     })
// })




// // fs.readFile('info.json', 'utf-8', (err, data)=>{
// //     if(err) return console.log(err);
// //     console.log(data);
// // })

// // try{
// //     const data = fs.readFileSync('info.js', 'utf-8');
// //     console.log(data);


// // }catch(error){
// //     console.log(error);
// // }

// const product = {
//     name: "Iphone",
//     price: 1000
// }

// fs.writeFile('info.json', JSON.stringify(product), 'utf-8', (err, data)=>{
//     if(err) return console.log(err);
//     console.log(data);
// })

// fs.appendFile('text.txt', JSON.stringify(product), 'utf-8', (err)=>{
//     if(err) return console.log(err);
//     // console.log(data);
// })

// fs.unlink('text.txt', (err)=>{
//     if(err) return console.log(err);
//     // console.log(data);
// })

// console.log('after');