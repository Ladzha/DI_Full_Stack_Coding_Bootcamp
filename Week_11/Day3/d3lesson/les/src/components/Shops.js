import { useState, useEffect } from "react";
const [products, setProducts] = useState([])


const Shop =(props)=>{

    useEffect(()=>{

       const getData = async () =>{
        const res = await fetch('')
        const data = await res.json()
        setProducts(data)
       }

    }, [])


    return (
        <> 
            {

                    products.map(item => {

                        return(

                            <div key ={item.id}>

                                {item.name}
                                {item.price}

                            </div>
                        )
                        

                    })
         
            
            
            }

        </>
    )
}