from service.todo_service import TodoService
from view.view import msg_display, list_display

DEFAULT_NUM = -1
DEFAULT_STR = ''

def is_valid_num(num):
    if num.isdigit(): return True
    return False

def is_valid_content(content):
    if content == '': return False
    return True

def is_valid_name(name):
    if name == '': return False
    return True

class TodoController:

    def register(self, todo):
        if not is_valid_name(todo.get_name()):
            msg_display('작성자 입력에 공백을 입력하지 마세요\n')
        
        if not is_valid_content(todo.get_content()):
            msg_display('일정내용 입력에 공백을 입력하지 마세요.\n')
            return

        msg = TodoService.register(todo)
        msg_display(msg)
    

    def display_all_todos(self):
        todos = TodoService.get_todos()

        if not todos:
            msg_display('일정목록이 하나도 없습니다.\n')
            return

        list_display(todos)
        msg_display('조회를 완료하였습니다.\n')
    

    def update(self, num, content):
        if not is_valid_num(num):
            msg_display('유효하지 않는 일정 번호입니다.\n')
            return
        
        if not is_valid_content(content):
            msg_display('유효하지 않는 일정 내용입니다.\n')
            return
        
        msg = TodoService.update(num, content)
        msg_display(msg)
    

    def remove(self, num):
        if not is_valid_num(num):
            msg_display('유효하지 않는 일정 번호입니다.\n')
            return

        msg = TodoService.remove(num)
        msg_display(msg)
    

    def clear(self):
        msg = TodoService.clear()
        msg_display(msg)

    def read_file(self):
        TodoService.read_file()
    

    def write_file(self):
        TodoService.write_file()
    
