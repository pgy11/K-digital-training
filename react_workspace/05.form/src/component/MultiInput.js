import React, { Component } from 'react'
import { Form } from 'semantic-ui-react';

export default class MultiInput extends Component {
    constructor(props){
        super(props);
        this.state = {
            isGoing: true,
            numberOfGuests: 2
        };
    }

    handleInputChange = (e) => {
        const target = e.target;
        const value = target.type === 'checkbox'? target.checked: target.value;
        const name = target.name;

        this.setState({
            [name]: value
        });
    }

    render() {
        return (
            <Form>
                <Form.Field>
                    <label>is going
                    <input name='isGoing' type='checkbox' checked={this.state.isGoing}
                     onChange={this.handleInputChange} />
                     </label>
                     <br />
                     <label>
                         Number of guest:
                         <input name='numberOfGuests' type='number'
                          value={this.state.numberOfGuests} onChange={this.handleInputChange}/>
                     </label>
                </Form.Field>
            </Form>
        )
    }
}
