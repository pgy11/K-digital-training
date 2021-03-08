import { inject } from 'mobx-react';
import { observer } from 'mobx-react';
import React, { Component } from 'react';
import {Item} from 'semantic-ui-react';
import BookItem from '../view/BookItemView';

@inject('BookStore')
@observer
class BookListContainer extends Component {

    render() {
        const {books, bookSelect} = this.props.BookStore;
        console.log(books);
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

export default BookListContainer;