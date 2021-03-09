import { inject, observer } from 'mobx-react';
import React, { Component } from 'react'

@inject('TodoStore')
@observer
class TodoInput extends Component {
  render() {
    const {todo, onChange, addTodo} = this.props.TodoStore;
    return (
      <div>
        <input type='text' value={todo} onChange={onChange} />
        <button onClick={() => addTodo()}>Add todo</button>
      </div>
    )
  }
}

export default TodoInput;
