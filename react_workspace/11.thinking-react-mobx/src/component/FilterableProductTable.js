import React, { Component } from 'react'
import ProductTable from './ProductTable'
import SearchBar from './SearchBar'

export default class FilterableProductTable extends Component {    
      render() {
        return (
          <div>
            <SearchBar            
            />
            <ProductTable
              products={this.props.products}
            />
          </div>
        );
      }
}
