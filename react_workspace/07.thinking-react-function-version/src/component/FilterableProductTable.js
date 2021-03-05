import React, { useState } from 'react'
import { Grid } from 'semantic-ui-react';
import ProductTable from './ProductTable'
import SearchBar from './SearchBar'

function FilterableProductTable(props) {
    const [filterText, setFilterTest] = useState('');
    const [inStockOnly, setInStockOnly] = useState(false);

    const handleFilterTextChange = (filterText) => {
        setFilterTest(filterText);
    }
    const handleInStockChange = (inStockOnly) => {
        setInStockOnly(inStockOnly);
    }

    return (
        <Grid columns={1}>
            <Grid.Row>
                <SearchBar filterText={filterText}
                    inStockOnly={inStockOnly} onFilterTextChange={handleFilterTextChange}
                    onInStockChange={handleInStockChange} />
            </Grid.Row>
            
            <Grid.Row>
                <ProductTable products={props.products} filterText={filterText} inStockOnly={inStockOnly} />
            </Grid.Row>
        </Grid>
    )
}

export default FilterableProductTable
