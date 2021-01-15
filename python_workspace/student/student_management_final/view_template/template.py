from entity.student import Student

line = '='*6

# 메뉴 화면 출력
def display_menu():

    print(line + ' Cloud MSA 반 수강생 관리 시스템 ' + line)
    print('1. 수강생 정보 등록')
    print('2. 수강생 목록 보기')
    print('3. 수강생 정보 수정')
    print('4. 수강생 정보 삭제')
    print('0. 종료')
    print()
   

# 학생 정보 입력 화면을 보여준다.
def input_info():
    sid = input('학번: ')
    name = input('이름: ')
    age = input('나이: ')

    while not age.isdigit():
        print('숫자를 입력하세요')
        age = input('나이: ')
    
    major = input('전공: ')
    
    return Student(sid, name, age, major)


# 업데이트 입력 화면을 보여준다.
def input_update_info():
    sid = input('수정할 수강생 학번 : ')
    major = input('수정할 전공 : ')
    return sid, major


def input_remove_info():
    sid = input('삭제할 수강색 학번 : ')
    return sid

# 메세지를 출력한다.
def display_msg(msg):
    print(msg)

def input_menu():
    return input('메뉴 선택 : ')
