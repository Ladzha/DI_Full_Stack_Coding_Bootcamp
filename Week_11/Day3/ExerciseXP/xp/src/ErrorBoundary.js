import React, { Component } from 'react';


class ErrorBoundary extends React.Component{
    constructor(){
        super();
        this.state = {hasError: false, error: null, errorInfo: "I crashed. Oh No!"}
    }

    componentDidCatch(err, errInfo){
        this.setState({error:"I crashed"})
        console.log("Error: ", err )
        this.setState({hasError:true})
        this.setState({errorInfo:errInfo})
        console.log("Error Info: ", errInfo )

    }

    render(){
        if(this.state.hasError){
            return (
            <details style={{ whiteSpace: 'pre-wrap' }}>
            {this.state.error && this.state.error.toString()}
            <br />
            {this.state.errorInfo.componentStack}
            </details>)
        }
        else{
            return this.props.children;
        }


    }
}

export default ErrorBoundary;