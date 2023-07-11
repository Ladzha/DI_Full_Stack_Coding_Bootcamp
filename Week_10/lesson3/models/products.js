import{db} from '../config/db.js'

export const getAllProduct =>(){
    return db('products')
    .select('id', 'name')

}