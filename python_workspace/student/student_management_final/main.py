from view_template.template import display_menu, input_menu, input_info, input_update_info
from view_template.template import input_remove_info
from controller_view.stdcontroller import StudentController

REGISTER = '1'
DISPLAY_STUDENTS = '2'
UPDATE = '3'
REMOVE = '4'
EXIT = '0'

stdcontroller = StudentController()
stdcontroller.read_file()

while True:
    display_menu()

    menu = input_menu()

    if menu == REGISTER:
        std = input_info()
        stdcontroller.register(std)
        
    elif menu == DISPLAY_STUDENTS:
        stdcontroller.display_students()
        
    elif menu == UPDATE:
        sid, major = input_update_info()
        stdcontroller.update(sid, major)

    elif menu == REMOVE:
        sid = input_remove_info()
        stdcontroller.remove(sid)       

    elif menu == EXIT: 
        stdcontroller.write_file()
        break

    else: 
        print()
        print('1, 2, 3, 4, 0 번 중 선택하세요')


