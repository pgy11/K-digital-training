import React, { Component } from 'react'
import InputText from './component/InputText'
import InputTextArea from './component/InputTextArea'
import Select from './component/Select'
import MultiInput from './component/MultiInput'
import { Container } from 'semantic-ui-react'
import './App.css';
import './component/Button.css'
import Header from './component/Header'
import Footer from './component/Footer'

export default class App extends Component {
  render() {
    return (
      <div className='app'>
        <Header />

        <div className='app__container'>
          <Container>
            <div className='app__margin'>
              <InputText />
            </div>

            <div className='app__margin'>
              <InputTextArea />
            </div>

            <div className='app__margin'>
              <Select />
            </div>

            <div className='app__margin'>
              <MultiInput />
            </div>

          </Container>
          <div className='app__container__wrapper' />
        </div>
        <Footer />
      </div>
    )
  }
}
