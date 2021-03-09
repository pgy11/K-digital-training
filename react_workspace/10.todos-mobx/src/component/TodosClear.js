import { inject, observer } from 'mobx-react';
import React, { Component } from 'react'

@inject('TodoStore')
@observer
class TodosClear extends Component {
    render() {
        const {clearTodo} = this.props.TodoStore;
        return (
            <div>
                <button onClick={() => clearTodo()}>clear</button>
            </div>
        )
    }
}

export default TodosClear;
