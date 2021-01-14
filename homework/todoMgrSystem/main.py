from view.view import menu_display, input_display, input_menu_display, update_input_display
from view.view import remove_input_display, unvalid_display
from controller.todo_controller import TodoController
todos = []
todo_num = 1
line = '='*6

NOT_FOUND = -1
REGISTER = '1'
UPDATE = '2'
REMOVE = '3'
DISPLAY = '4'
REMOVE_ALL = '5' 
EXIT = '6'

controller = TodoController()
controller.read_file()

while True:

    menu_display()

    menu = input_menu_display()
    
    if menu == REGISTER:
        todo = input_display()
        controller.register(todo)


    elif menu == UPDATE:
        num, content = update_input_display()
        controller.update(num, content)


    elif menu == REMOVE:
        num = remove_input_display()
        controller.remove(num)


    elif menu == DISPLAY:
        controller.display_all_todos()


    elif menu == REMOVE_ALL:
        controller.clear()

    elif menu == EXIT:
        controller.write_file()
        break

    else: unvalid_display()
    