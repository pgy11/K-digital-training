from view.views import menu_display, input_display, menu_select_display, msg_display
from controller.prodcontroller import ProductController
from utils.utils import REGISTER, DISPLAY, UPDATE, REMOVE, CLEAR, EXIT

controller = ProductController()
controller.read_file()

while True:

    menu_display()
    menu = menu_select_display()

    if menu == REGISTER:
        info = input_display()
        controller.register(info)
    
    elif menu == DISPLAY:
        controller.display_all_products()
    
    elif menu == UPDATE:
        controller.update()
    
    elif menu == REMOVE:
        controller.remove()
    
    elif menu == CLEAR:
        controller.clear()
    
    elif menu == EXIT:
        controller.write_file()
        break

    else:
        msg_display('1~6번을 입력하세요')


