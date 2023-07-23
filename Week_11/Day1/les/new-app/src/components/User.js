import './User.css'

const User = (props)=>{
    const{userinfo} =props;
    // const style = //v peremennuy
    return (
        <div className = 'userstyle' style ={
        {
                display:'inline-block', color:'red',
                textAlign: 'center',
                margin: '30px',
                border: '10px solid blue',
                borderRadius: '18px'
        }
        
        }>
            <img src ={`https://robohash.org/${userinfo.id}?size=150x150`}/>
                <h2>{userinfo.name}</h2>
                <h4>{userinfo.email}</h4>
                <p>{userinfo.username}</p>
        </div>


    )
}

export default User