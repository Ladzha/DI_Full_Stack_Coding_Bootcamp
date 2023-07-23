const UserFavoriteAnimals = (props)=>{
    const animals = props.favAnimals
    return (
        <div>
            <ul>
               
                {
                animals.map((item, index) =>{

                return  <li> {item} </li>
                })
                }
                
            </ul>

            
        </div>
    )
    



}

export default UserFavoriteAnimals