import React, { Component } from 'react'
import TodoManagement from './component/TodoManagement'
import './App.css'
import { Container } from 'semantic-ui-react'

export default class App extends Component {
  render() {
    return (
      <Container>
        <TodoManagement />        
      </Container>
    )
  }
}
