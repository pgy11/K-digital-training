import Books from '../Books'
import {observable, action, makeAutoObservable} from 'mobx'

class BookStore  {
  @observable books = Books;
  @observable book = Books[0];

  // ES6 이상은 이 부분을 명시해야한다.
  constructor() {
    makeAutoObservable(this);
  }

  @action
  bookSelect = (book) => {
    this.book = book;
  }

    
}

export default new BookStore();