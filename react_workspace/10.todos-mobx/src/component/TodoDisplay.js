import { inject, observer } from 'mobx-react';
import React, { Component } from 'react'

@inject('TodoStore')
@observer
class TodoDisplay extends Component {

    render() {
        const {deleteTodo, todos} = this.props.TodoStore;
        const todoDisplay = todos.map((todo) => {
            return(            
            <div key={todo[0]}> {todo[1]}
             <button type='submit' onClick={() => deleteTodo(todo[0])}>delete</button></div>
             )
        })

        return (
            <div>
                {todoDisplay}
            </div>
        )
    }
}

export default TodoDisplay;
