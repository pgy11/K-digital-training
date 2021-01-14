import os
from entity.todo import Todo

PATH = 'dao/'
FILE_PATH = PATH + 'todos.dat'

def load_todos():
    todos = []

    if os.path.isfile(FILE_PATH):
        with open(FILE_PATH, 'r') as f:
            while True:
                data = f.readline()

                if not data: break

                todo_info = data.rstrip().split(',')

                if len(todo_info) == 3:
                    todo = Todo(todo_info[1], todo_info[2])
                    todo.set_num(todo_info[0])
                    todos.append(todo)
    
    return todos
            

def save_todos(todos):

    with open(FILE_PATH, 'w') as f:
        for todo in todos:
            f.write('{0},{1},{2}\n'.format(todo.get_num(), todo.get_name(), todo.get_content()))
