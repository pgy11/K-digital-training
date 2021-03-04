import React, { Component } from 'react';
import { Grid, Input } from 'semantic-ui-react';
import Books from './Books';
import BookDetail from './component/BookDetail';
import BookList from './component/BookList';
import './App.css'

export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      searchTitle: 'dd',
      books: Books,
      book: Books[0]
    };
  }

  onBookSelect = (selectBook) => {
    this.setState({
      book: selectBook,
    })
  };


  onSearch = () => {
    console.log(this.state.searchTitle);
    Books.map((item, index) => {
      if(item.title === this.state.searchTitle){
        this.setState({
          book: Books[index]
        })
      }
    })
  }

  handleInputChange = (e) => {
    this.setState({
      searchTitle:e.target.value
    })
  }

  render() {
    return (
      <div className='app'>
        <Grid columns={2}>
          <Grid.Row>
            <Grid.Column>
              <BookList books={this.state.books} bookSelect={this.onBookSelect} />
            </Grid.Column>

            <Grid.Row className='app__gridRow__gridRow'>
              <Grid.Column className='app__gridRow__gridRow__gridCol'>
                <Input type='text'
                 action={{icon: 'search', onClick: ()=> this.onSearch()}}
                 placeholder='Search...' onChange={this.handleInputChange}
                 />
              </Grid.Column>

              <Grid.Column>
                <BookDetail book={this.state.book} />
              </Grid.Column>

            </Grid.Row>
          </Grid.Row>
        </Grid>
      </div>
    )
  }
}
