import React from 'react'
import { Grid } from 'semantic-ui-react';

function ProductRow(props) {
    const product = props.product;
    const name = product.stocked? product.name: <span style={{color:'red'}}>{product.name}</span>

    return (
        <Grid.Row>
            <Grid.Column>{name}</Grid.Column>
            <Grid.Column>{product.price}</Grid.Column>
        </Grid.Row>
    )
}

export default ProductRow
