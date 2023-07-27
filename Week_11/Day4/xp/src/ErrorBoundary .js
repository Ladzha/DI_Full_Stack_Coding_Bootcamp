import React, { Component } from 'react';


class ErrorBoundary extends React.Component{
    constructor(){
        super();
        this.state = {hasError: false, error: "An error has occurred"}
    }

    componentDidCatch(err){
        this.setState({hasError:true})
   
    }

    render(){
        if(this.state.hasError){
            return (
                <h1>"An error has occurred"</h1>
            )
        }
        
            return this.props.children;
        


    }
}

export default ErrorBoundary;