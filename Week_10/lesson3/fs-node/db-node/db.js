const knex = require('knex');
const db = knex({
    client:'pg',
    connection: {
        host: 'stampy.db.elephantsql.com',
        port: '5432',
        user: 'lorcobbn',
        database: 'lorcobbn',
        password: '0VM8zsbiPXjSqQhKi_g9uqzQR8NT1lhg',
    }

})

db
.select('id', 'name', 'price')
.from('products')
.then(rows =>{
    console.log(rows);
})


db.raw('select id, name, price from products').then(row=>{
console.log(row.rows);
});

// db('products')
// .insert([
//     {name:'p1', price:700},
//     {name:'p2', price:700}
// ])
// .returning("*")
// .then((row)=>{
//     console.log(row);
// })
// .catch((err)=>{
//     console.log(err);
// })

// db('products')
// .update({name:'p1'})
// .where({id:6})
// .returning("*")
// .then((row)=>{
//     console.log(row);
// })
// .catch((err)=>{
//     console.log(err);
// })

db('products')
// .update({name:'p1'})
.where({id:6})
.del()
.returning("*")
.then((row)=>{
    console.log(row);
})
.catch((err)=>{
    console.log(err);
})