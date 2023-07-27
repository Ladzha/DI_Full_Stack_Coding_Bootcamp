const PostList = ({data})=>{
    return(
        <>
            <h1>Hi This is a Title</h1>
            {data.map(item =>{
                    return(
                    <div key={item.id}>
                    <h2>{item.title}</h2>
                    <p>{item.content}</p>
                    </div>
                    )
                })}

        </>
        
    )   
}
export default PostList


    // {data.map((item, index)=>{

    //     return (
    //         <div key={index}>
    //         <h1>{props.title}</h1>
    //         <h6>{props.content}</h6>
    //         </div>
    //     )}
