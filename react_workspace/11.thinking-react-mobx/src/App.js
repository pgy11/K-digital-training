import React, { Component } from 'react'
import FilterableProductTable from './component/FilterableProductTable';
import products from './Product';


export default class App extends Component {
  render() {
    return (
      <div>
        <FilterableProductTable products={products}/>        
      </div>
    )
  }
}
