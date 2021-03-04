import React, { Component } from 'react';
import {Item} from 'semantic-ui-react';
import BookItem from './BookItem';

export default class BookList extends Component {

    render() {
        const {books, bookSelect} = this.props;
        const listItem = books.map(book => {
            return <BookItem key={book.ISBN} book={book} bookSelect={bookSelect}/>
        });

        return (
            <Item.Group>
                {listItem}
            </Item.Group>
        )
    }
}
