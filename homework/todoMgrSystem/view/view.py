from entity.todo import Todo

line = '=' * 6

# 메뉴화면 출력
def menu_display():
    print(line + ' 일정관리 시스템 ' + line)
    print('1. 일정 등록')
    print('2. 일정 수정')
    print('3. 일정 삭제')
    print('4. 일정 조회')
    print('5. 일정 전체삭제')
    print('6. 종료')


# 이름, 내용 등록 화면 출력
def input_display():
    name = input('작성자: ')
    content = input('내용: ')

    return Todo(name, content)


# 메뉴입력 화면 출력
def input_menu_display():
    return input('메뉴 선택: ')


# 수정 정보입력 화면 출력
def update_input_display():
    num = input('수정할 일정번호 입력: ')
    content = input('수정할 내용: ')
    return num, content


# 삭제 정보입력 화면 출력
def remove_input_display():
    return input('삭제할 일정번호 입력: ')


# 결과를 message로 화면에 출력
def msg_display(msg):
    print(msg)

# 유효하지 않는 메뉴 선택시 나오는 출력
def unvalid_display():
    print('1 ~ 6사이의 값을 입력하세요.')

# 모든 일정 출력
def list_display(todos):
    print(line + ' 일정 목록 ' + line)

    for todo in todos: 
        print(todo)


