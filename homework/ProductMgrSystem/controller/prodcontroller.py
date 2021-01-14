from service.product_service import ProductService 
from utils.utils import NOT_FOUND, PID_UPDATE, PNAME_UPDATE, PRICE_UPDATE, DESC_UPDATE, EXIT
from view.views import msg_display, list_display, update_info_display, menu_select_display
from view.views import update_pid_input_display, update_pname_input_display, update_price_input_display
from view.views import update_desc_input_display, pid_input_display, remove_input_display
from exception.exceptions import *
from entity.product import Product
from dao.files import load_data, save_data

def has_pid(pid):
    for i, prod in enumerate(ProductService.products):
        if prod.get_pid() == pid: return i
    return NOT_FOUND

def is_valid_pid(pid):
    if pid == '': return False
    return True

def is_valid_pname(pname):
    if pname == '': return False
    return True

def is_valid_price(price):
    if price.isdigit():
        if int(price) > 0: return True
        return False
        
    return False

def is_valid_desc(desc):
    if desc == '': return False
    return True

def is_valid_menu(menu, end):
    if not menu.isdigit(): return False
    if 1 <= int(menu) <= end: return True
    return False

class ProductController:

    def register(self, info):
        pid, pname, price, desc = info[0], info[1], info[2], info[3]

        if not is_valid_pid(pid):
            msg_display(str(UnvalidPIDException(pid)))
            return
        
        if not is_valid_pname(pname):
            msg_display(str(UnvalidPnameExceptrion(pname)))
            return
        
        if not is_valid_price(price):
            msg_display(str(UnvalidPriceExceptrion(price)))
            return
        
        if not is_valid_desc(desc):
            msg_display(str(UnvalidDescExcpetion(desc)))
            return
        
        if has_pid(pid) != NOT_FOUND:
            msg_display(str(DuplicationException(pid)))
            return

        product = Product(pid, pname, int(price), desc)
        msg = ProductService.register(product)
        msg_display(msg)


    def display_all_products(self):
        if ProductService.products:
            list_display(ProductService.products)
            msg_display('모든 상품을 조회하였습니다.\n')
        
        else:
            msg_display('상품이 하나도 없습니다.\n')


    def update(self):
        if not ProductService.products:
            msg_display('상품이 하나도 없습니다.\n')
            return
        
        pid = pid_input_display()

        if not is_valid_pid(pid):
            msg_display(str(UnvalidPIDException(pid)))
            return

        index = has_pid(pid)

        if index == NOT_FOUND:
            msg_display(str(RecordNotFoundException(pid)))
            return
        
        update_info_display()
        menu = menu_select_display()
        
        if not is_valid_menu(menu, 5):
            msg_display(str(UnvalidOptionExceptrion(menu)))
            return
        
        if menu == PID_UPDATE:
            new_pid = update_pid_input_display()

            if not is_valid_pid(pid):
                msg_display(str(UnvalidPIDException(pid)))
                return

            if has_pid(new_pid) == NOT_FOUND:
                msg = ProductService.update(index, PID_UPDATE, new_pid)
                msg_display(msg)
    
            else:
                msg_display(str(DuplicationException(pid)))

        elif menu == PNAME_UPDATE:
            new_pname = update_pname_input_display()

            if not is_valid_pname(new_pname):
                msg_display(str(UnvalidPnameExceptrion(new_pname)))
                return

            msg = ProductService.update(index, PNAME_UPDATE, new_pname)
            msg_display(msg)
        
        elif menu == PRICE_UPDATE:
            new_price = update_price_input_display()

            if not is_valid_price(new_price):
                msg_display(str(UnvalidPriceExceptrion(new_price)))
                return
            
            msg = ProductService.update(index, PRICE_UPDATE, int(new_price))
            msg_display(msg)

        elif menu == DESC_UPDATE:
            new_desc = update_desc_input_display()

            if not is_valid_desc(new_desc):
                msg_display(str(UnvalidDescExcpetion(new_desc)))
                return
            
            msg = ProductService.update(index, DESC_UPDATE, new_desc)
            msg_display(msg)
        
        elif menu == EXIT:
            msg_display('초기화면으로 돌아갑니다.\n')


    def remove(self):
        pid = remove_input_display()
        
        if not is_valid_pid(pid):
            msg_display(str(UnvalidPIDException(pid)))
            return
        
        index = has_pid(pid)
        if index == NOT_FOUND:
            msg_display(str(RecordNotFoundException(pid)))
            return
        
        msg = ProductService.remove(index)
        msg_display(msg)


    def clear(self):
        if ProductService.products:
            msg = ProductService.clear()
            msg_display(msg)
        
        else:
            msg_display('상품이 하나도 없습니다.\n')


    def read_file(self):
        ProductService.read_file()
        

    def write_file(self):
        ProductService.write_file()
        msg_display('정보를 저장합니다.')

