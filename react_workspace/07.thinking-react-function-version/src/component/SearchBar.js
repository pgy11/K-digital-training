import React from 'react'
import { Grid, Input, Search } from 'semantic-ui-react';

function SearchBar(props) {
    const filterText = props.filterText;
    const inStockOnly = props.inStockOnly;

    const handleFilterTextChange = (e) => {
        props.onFilterTextChange(e.target.value);
    };
    const handleInStockChange = (e) => {
        props.onInStockChange(e.target.checked);
    }

    return (
        <Grid columns={1}>
            <Grid.Row>
                <Input type='text' onChange={handleFilterTextChange} />
            </Grid.Row>

            <Grid.Row>
                <Input type='checkbox' onChange={handleInStockChange} />
                {' '}
                Only show products in stock
            </Grid.Row>
        </Grid>
    )
}

export default SearchBar
