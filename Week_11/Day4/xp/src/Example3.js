import data2 from './data2.json'
import React from 'react';

class Example3 extends React.Component {
constructor(props){
    super(props);
};
    render() { 
        return (
            <div>
            <h2>This is Experiences from JSON</h2>
            
            {this.props.data2.Experiences.map((item, index) =>{
                    return(
                    <div key={index}>
                    <img src={item.logo}/>
                    <h6> <a href={item.url}>{item.companyName}</a></h6>
                    <h6>{item.roles[0].title}</h6>
                    <h6>{item.roles[0].description}</h6>
                    <h6>{item.roles[0].endDate}</h6>
                    <h6>{item.roles[0].location}</h6>
                    </div>
                    )
                })}
            </div>
        );
    }
}
 
export default Example3;