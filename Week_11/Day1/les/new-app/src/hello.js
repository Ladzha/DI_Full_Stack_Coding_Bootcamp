const Hello=(props)=>{
    console.log(props)
    const {name, email} =props
return (
<>
    <h1>Hello {props.name} </h1>
    <h2> {email} </h2>
</> 
);
};

export default Hello