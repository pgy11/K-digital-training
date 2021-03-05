import React from 'react'
import { Grid } from 'semantic-ui-react';
import ProductCategoryRow from './ProductCategoryRow';
import ProductRow from './ProductRow';

function ProductTable(props) {
    const filterText = props.filterText;
    const inStockOnly = props.inStockOnly;
    const products = props.products;
    const productList = [];
    let lastCategory = null;

    products.forEach(product => {
        if (product.name.indexOf(filterText) === -1) {
            return;
        }
        if (inStockOnly && !product.stocked) {
            return;
        }
        if (product.category !== lastCategory) {
            lastCategory = product.category;
            productList.push(
                <ProductCategoryRow category={product.category} key={product.category} />
            );
        }

        productList.push(
            <ProductRow product={product} key={product.name} />
        );
    });

    return (
        <Grid columns={2}>
            <Grid.Row>
                <Grid.Column>Name</Grid.Column>
                <Grid.Column>Price</Grid.Column>
            </Grid.Row>

            {productList}

        </Grid>
    )
}

export default ProductTable
