import React, { Component } from 'react'

export default class TodoDisplay extends Component {
    handleClickDeleteBtn = (deleteId) => {
        let _todos = [];
        this.props.todos.forEach(todo => {
            if(todo[0] !== deleteId) _todos.push(todo);
        });

        this.props.onDeleteTodo(_todos);        
    }
    
    render() {
        const {todos} = this.props;
        const todoDisplay = todos.map((todo) => {
            return(            
            <div key={todo[0]}> {todo[1]}
             <button type='submit' onClick={() => this.handleClickDeleteBtn(todo[0])}>delete</button></div>
             )
        })

        return (
            <div>
                {todoDisplay}
            </div>
        )
    }
}
