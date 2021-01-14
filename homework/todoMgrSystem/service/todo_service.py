from dao.todo_file import load_todos, save_todos
from exception.user_exception import NumNotFoundException

NOT_FOUND = -1
line = '=' * 6

def get_todos_len():
    return len(TodoService.todos)

def has_todo_num(num):
    for i, todo in enumerate(TodoService.todos):
        if todo.get_num() == num: return i
    
    return NOT_FOUND

def sort_num():

    for i, todo in enumerate(TodoService.todos):
        todo.set_num(str(i+1))


class TodoService:

    todos = []

    # 일정 등록
    @classmethod
    def register(cls, todo):
        num = str(get_todos_len() + 1)
        todo.set_num(num)
        cls.todos.append(todo)

        return '{0}번째 일정이 등록되었습니다.\n'.format(num)


    # 일정 내용 수정
    @classmethod
    def update(cls, num, content):
        index = has_todo_num(num)

        if index != NOT_FOUND:
            cls.todos[index].set_content(content)
            return '{0}번째 일정이 수정되었습니다.\n'.format(num)
        
        return str(NumNotFoundException(num))

    # 일정 삭제
    @classmethod
    def remove(cls, num):
        index = has_todo_num(num)

        if index != NOT_FOUND:
            del cls.todos[index]

            if get_todos_len() > 0: sort_num()

            return '{0}번째 일정이 삭제되었습니다.\n'.format(num)
        
        return str(NumNotFoundException(num))

    @classmethod
    def clear(cls):
        cls.todos.clear()
        return '일정 초기화 완료하였습니다.\n'


    # 모든 일정 조회
    @classmethod
    def display_all_todos(cls):
        if get_todos_len() == 0: return '조회할 일정이 하나도 없습니다.\n'

        print(line + ' 일정 목록 ' + line)

        for todo in cls.todos: 
            print(todo)
        
        return '조회을 완료하였습니다\n'


    # 파일에 있는 일정 불러오기
    @classmethod
    def read_file(cls):
        cls.todos = load_todos()


    # 일정을 파일에 저장
    @classmethod
    def write_file(cls):
        save_todos(cls.todos)
        
