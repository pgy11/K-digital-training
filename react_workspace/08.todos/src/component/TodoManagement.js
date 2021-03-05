import React, { Component } from 'react'
import TodoDisplay from './TodoDisplay';
import TodosClear from './TodosClear';


export default class TodoManagement extends Component {
    constructor(props) {
        super(props);
        this.state = {
            id: 0,
            todo: '',
            todos: []
        };
    }

    handleInputChange = (e) => {
        this.setState({
            todo: e.target.value
        });
    }

    handleClickAddBtn = () => {
        let _id = this.state.id + 1;
        this.state.todos.push([_id, this.state.todo]);
        this.setState({
            id: _id,
            todo: ''
        })
    }

    onDeleteTodo = (_todos) => {
        this.setState({
            todos: _todos
        })
    }

    onClearTodo = () => {
        this.setState({
            todos: []
        })
    }

    render() {
        return (
            <div>

                <input type='text' value={this.state.todo} onChange={this.handleInputChange} />
                <button type='submit' onClick={() => this.handleClickAddBtn()}>Add todo</button>
                <TodoDisplay todos={this.state.todos} onDeleteTodo={this.onDeleteTodo} />
                <TodosClear todos={this.state.todos} onClearTodo={this.onClearTodo} />
            </div>
        )
    }
}
