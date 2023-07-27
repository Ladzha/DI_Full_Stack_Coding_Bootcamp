import data2 from './data2.json'
import React from 'react';

class Example2 extends React.Component {
constructor(props){
    super(props);
};
    render() { 
        return (
            <div>
            <h2>This is Skills from JSON</h2>

            {this.props.data2.Skills.map((item, index) =>{
                    return(
                    <div key={index}>
                    <h6>{item.Area}</h6>

                    <ul>
                    {item.SkillSet.map(skill=>{
                      return (
                        <li>
                     {skill.Name}
                        </li>
                      )
                    })}
                    </ul>

                    </div>
                    )
                })}
            </div>
        );
    }
}
 
export default Example2;