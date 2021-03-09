import React, { Component } from 'react'
import TodoDisplay from './TodoDisplay';
import TodosClear from './TodosClear';
import TodoInput from './TodoInput';

class TodoManagement extends Component {

    render() {
        return (
            <div>
                <TodoInput />
                <TodoDisplay />
                <TodosClear />
            </div>
        )
    }
}

export default TodoManagement;