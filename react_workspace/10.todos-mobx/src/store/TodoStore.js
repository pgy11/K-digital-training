import {action, makeAutoObservable, observable} from 'mobx'

class TodoStore {
  @observable id = 0;
  @observable todo = '';
  @observable todos = [];

    // ES6 이상은 이 부분을 명시해야한다.
    constructor() {
      makeAutoObservable(this);
    }

  @action
  addTodo = () => {
    this.todos.push([this.id, this.todo]);
    this.todo = '';
    this.id++;        
  }

  @action
  onChange = (e) => {
    this.todo = e.target.value;
  }

  @action
  deleteTodo = (id) => {
    this.todos = this.todos.filter(item => item[0] !== id);
  }

  @action
  clearTodo = () => {
    this.todos = [];
  }

}

export default new TodoStore();
