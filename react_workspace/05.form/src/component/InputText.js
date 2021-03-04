import React, { Component } from 'react'
import { Form } from 'semantic-ui-react';

export default class InputText extends Component {
    constructor(props){
        super(props);
        this.state = {value: ''};
    }

    handleChange = (e) => {
        this.setState({
            value: e.target.value            
        });
    };

    handleSubmit = (e) => {
        alert(this.state.value);
        e.preventDefault();
    }


    render() {
        return (
            <Form onSubmit={this.handleSubmit}>
            <label>
              Name:
              <input type="text" value={this.state.value} onChange={this.handleChange} />
            </label>
            <input id='input' type="submit" value="Submit" />
          </Form>
        )
    }
}
