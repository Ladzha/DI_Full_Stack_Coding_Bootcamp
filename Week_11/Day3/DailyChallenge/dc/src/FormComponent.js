const FormComponent =(props)=>{
    return(
        <>
        <h1>Entered information</h1>
        <h3>You name: {props.fname} {props.lname} </h3>
        <h3>You age: {props.age} </h3>
        <h3>You gender: {props.gender} </h3>
        <h3>You destination: {props.destination} </h3>
        <h3>You dietary: </h3>

        <p>**Nuts free {props.nuts}</p>
        <p>**Lactose free {props.lacto}</p>
        <p>**Vegan free {props.vegan}</p>  
  
        </> 

    )
}


export default FormComponent 