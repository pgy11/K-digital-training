import React from 'react'
import { Grid } from 'semantic-ui-react';

function ProductCategoryRow(props) {
    const category = props.category;
    return (
        <Grid.Row>
            <Grid.Column>
                {category}
            </Grid.Column>
        </Grid.Row>
    )
}

export default ProductCategoryRow
