import React, { Component } from 'react'

export default class TodosClear extends Component {
    handleClearBtn = () => {
        this.props.onClearTodo()
    }

    render() {
        return (
            <div>
                <button type='submit' onClick={() => this.handleClearBtn()}>clear</button>
            </div>
        )
    }
}
