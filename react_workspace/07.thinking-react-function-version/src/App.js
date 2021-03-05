import React from 'react'
import { Container } from 'semantic-ui-react'
import FilterableProductTable from './component/FilterableProductTable'
import products from './Product'
import './App.css'

function App() {
  return (
    <div className='app'>
      <FilterableProductTable products={products}/>     
    </div>
  )
}

export default App
