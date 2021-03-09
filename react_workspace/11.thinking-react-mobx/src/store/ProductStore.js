import {observable, action, makeAutoObservable} from 'mobx';

class ProductStore {
  @observable filterText = '';
  @observable inStockOnly = false;

  constructor(){
    makeAutoObservable(this);
  }

  @action
  onFilterTextChange = (e) => {
    this.filterText = e.target.value;
  }

  @action
  onStockOptionChange = (e) => {
    this.inStockOnly = e.target.checked;
  }

  

}

export default new ProductStore();
