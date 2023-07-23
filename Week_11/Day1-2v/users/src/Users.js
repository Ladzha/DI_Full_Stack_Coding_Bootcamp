import "./Users.css"
const User = ()=>{
    const styling = {color:'red'}
    const userList = [
    {name: "John1", email: 'john1@mail.com', isEmail: true},
    {name: "John2", email: 'john2@mail.com', isEmail: true},
    {name: "John3", email: 'john3@mail.com', isEmail: true},
]

    // if(user.isEmail){
    //     return <h2>{user.email}</h2>
    // }
    // else{
    //     return <h3>{user.name}</h3>
    // }

    // {user.isEmail ? <h2>{user.email}</h2> : <h3>{user.name}</h3>}
    // {user.isEmail ?? <h2>{user.email}</h2>}

    return(
        <>
        {userList.map((item, index)=>{

            return <h1 style={styling} key={index}> Hello World {item.name} </h1>
            
        })}
        </>
    );
}
export default User;