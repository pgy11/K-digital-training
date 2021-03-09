import { inject, observer } from 'mobx-react';
import React, { Component } from 'react'

@inject('ProductStore')
@observer
class SearchBar extends Component {
    render() {
        const {filterText, onFilterTextChange, inStockOnly, onStockOptionChange} = this.props.ProductStore;
        return (
            <form>
                <input
                    type="text"
                    placeholder="Search..."
                    value={filterText}
                    onChange={onFilterTextChange}
                />
                <p>
                    <input
                        type="checkbox"
                        checked={inStockOnly}
                        onChange={onStockOptionChange}
                    />
                    {' '}
              Only show products in stock
            </p>
            </form>
        );
    }
}

export default SearchBar;
