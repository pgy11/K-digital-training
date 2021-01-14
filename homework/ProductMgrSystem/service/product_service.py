from utils.utils import PID_UPDATE, PNAME_UPDATE, PRICE_UPDATE, DESC_UPDATE
from dao.files import save_data, load_data


class ProductService:

    products = []
    
    @classmethod
    def register(cls, product):
        cls.products.append(product)
        return '상품등록이 완료됐습니다.\n'

    @classmethod
    def update(cls, index, attr, info):
        if attr == PID_UPDATE: cls.products[index].set_pid(info)
        elif attr == PNAME_UPDATE: cls.products[index].set_pname(info)
        elif attr == PRICE_UPDATE: cls.products[index].set_price(info)
        elif attr == DESC_UPDATE: cls.products[index].set_desc(info)

        return '변경이 완료됐습니다.\n'

    @classmethod
    def remove(cls, index):
        pid = cls.products[index].get_pid()
        pname = cls.products[index].get_pname()
        del cls.products[index]

        return '상품번호 {0}, 상품명 {1}이(가) 삭제됐습니다.\n'.format(pid, pname)

    @classmethod
    def clear(cls):
        cls.products.clear()
        return '모든 상품들이 삭제됐습니다.\n'
    
    @classmethod
    def read_file(cls):
        cls.products = load_data()


    @classmethod
    def write_file(cls):
        save_data(cls.products) 
