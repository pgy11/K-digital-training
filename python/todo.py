import os

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

FILE_PATH = 'todos.dat'


def display_menu():
    print(line + ' 일정관리 시스템 ' + line)
    print('1. 일정 등록')
    print('2. 일정 수정')
    print('3. 일정 삭제')
    print('4. 일정 조회')
    print('5. 일정 전체삭제')
    print('6. 종료')


def register(title):
    global todo_num, todos
    todo_dict = {}

    todo_dict['todo_id'] = todo_num
    todo_dict['title'] = title
    todos.append(todo_dict)

    print('일정이 등록됐습니다.')
    todo_num += 1


def has_any_todos():
    global todos

    if todos: return True
    
    return False


def get_todo_index(num):
    global todos

    for i, todo in enumerate(todos):
        if todo['todo_id'] == num: return i

    return NOT_FOUND


def input_num():
    _todo_num = input('일정번호를 입력하세요 : ')

    while not _todo_num.isdigit():
        print('숫자를 입력하세요.')
        _todo_num = input('번호를 입력하세요. : ')

    return int(_todo_num) 


def update(index):
    global todos

    title = input('일정을 입력하세요 : ')
    todos[index]['title'] = title


def remove(index):
    global todos
    _num, _title = todos[index]['todo_id'], todos[index]['title']
    
    del todos[index]

    return _num, _title


def display_todos():
    global todos

    for todo in todos:
        print('일정 {0}. {1}'.format(todo['todo_id'], todo['title']))

def remove_all_todos():
    global todos

    todos.clear()


def save_to_file():
    global todos

    with open(FILE_PATH, 'w') as f:
        for todo in todos:
            f.write('{0},{1}\n'.format(todo['todo_id'], todo['title']))

    print('데이터를 저장합니다.')


def init_load_file():
    global todos, todo_num

    if os.path.isfile(FILE_PATH):
        with open(FILE_PATH, 'r') as f:
            while True:
                data = f.readline()

                if not data: break

                todo_info = data.rstrip().split(',')

                if len(todo_info) == 2:
                    todos.append({'todo_id': int(todo_info[0]), 'title': todo_info[1]})
            
            if has_any_todos(): todo_num = todos[-1]['todo_id'] + 1
            print('로딩 완료')


init_load_file()

while True:

    display_menu()
    menu = input('메뉴를 선택하세요. : ')
    
    if menu == REGISTER:
        title = input('일정을 입력하세요. : ')
        register(title)

    elif menu == UPDATE:
        if not has_any_todos():
            print('일정이 하나도 없습니다.\n')
            continue

        num = input_num()
        index = get_todo_index(num)

        if index != -1:
            update(index)
            print('수정 완료됐습니다.')
        
        else: print('존재하지 않는 일정번호입니다.')

              
    elif menu == REMOVE:
        if not has_any_todos():
            print('일정이 하나도 없습니다.\n')
            continue

        num = input_num()
        index = get_todo_index(num)

        if index != -1:
            removed_num, removed_title = remove(index)
            print('일정{0}. {1} 삭제완료.'.format(removed_num, removed_title))
        
        else: print('존재하지 않는 일정번호입니다.')


    elif menu == DISPLAY:
        if not has_any_todos():
            print('일정이 하나도 없습니다.\n')
            continue

        display_todos()


    elif menu == REMOVE_ALL:
        if not has_any_todos():
            print('일정이 하나도 없습니다.\n')
            continue

        remove_all_todos()
        print('전체 삭제 완료 했습니다.')

    elif menu == '6':
        save_to_file()
        print('일정관리 시스템을 종료합니다.')
        break

    else: print('1 ~ 6사이의 값을 입력하세요.')
    
    print()