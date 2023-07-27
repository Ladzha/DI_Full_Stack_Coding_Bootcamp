import data2 from './data2.json'
import React from 'react';

class Example1 extends React.Component {
constructor(props){
    super(props);
};
    render() { 
        return (
            <div>
            <h2>This is media from JSON</h2>
            {this.props.data2.SocialMedias.map(item =>{
                    return(
                    <div key={item.id}>
                    <h6>{item}</h6>
                    </div>
                    )
                })}
            </div>
        );
    }
}
 
export default Example1;