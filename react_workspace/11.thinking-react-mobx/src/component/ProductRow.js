import React, { Component } from 'react'

export default class ProductRow extends Component {
    render() {
        const { name, price, stocked } = this.props.product;

        return (
            <tr>
                <td>
                    {stocked ? name  : <span style={{ color: 'red' }}>{name}</span>}
                </td>

                <td>
                    {price}
                </td>
            </tr>
        )
    }
}
