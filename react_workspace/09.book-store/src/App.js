import React, { Component } from 'react';
import { Grid } from 'semantic-ui-react';
import BookDetail from './container/BookContainer';
import BookList from './container/BookListContainer';
import './App.css'
import {observer, inject} from 'mobx-react';

@inject('BookStore')
@observer
class App extends Component {


  render() {
    return (
      <div className='app'>
        <Grid columns={2}>
          <Grid.Row>
            <Grid.Column>
              <BookList />
            </Grid.Column>

            <Grid.Row className='app__gridRow__gridRow'>
              <Grid.Column className='app__gridRow__gridRow__gridCol'>
              </Grid.Column>

              <Grid.Column>
                <BookDetail />
              </Grid.Column>

            </Grid.Row>
          </Grid.Row>
        </Grid>
      </div>
    )
  }
}

export default App;
