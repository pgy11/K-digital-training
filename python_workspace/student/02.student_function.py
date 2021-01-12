# 수강생 관리 시스템
students = []
sid = 1
line = '='*6
NOT_FOUND = -1


# 수강생 등록 : list students에 정보 저장
def register(name, id, major):
    global sid, students

    student = {'id':sid, 'name':name, 'age': int(age), 'major': major}
    students.append(student)
    sid += 1
    print('{0}이 성공적으로 등록됐습니다.'.format(name))


# 수강생 목록 : list students 목록 리턴
def display_students():
    global students

    for std in students:
        print('id: {0}, name: {1}, age: {2}, major: {3}'.format(std['id'],
         std['name'], std['age'], std['major']))


# update(), remove()에서 공통적으로 사용되는 id 입력 함수 
def enter_id():
    _sid = input('학생의 전공을 수정할 ID를 입력하세요 : ')
        
    while not _sid.isdigit():
        print('숫자를 입력하세요')
        _sid = input('ID를 입력하세요. : ')
    
    return int(_sid)


# 수강생 수정 : id를 검색해서 전공정보 수정하고 message 리턴
def update(std_index):
    _major = input('변경할 {0}의 전공을 입력하세요. : '.format(students[std_index]['name']))
    _name = students[std_index]['name']
    students[std_index]['major'] = _major
    print('{0}의 전공이 {1}으로 수정됐습니다.'.format(_name, _major))

 
# 수강생 삭제 : id를 검색해서 수강생 정보 삭제 message 리턴
def remove(std_index):
    global students

    _name = students[std_index]['name']
    del students[std_index]
    print('{0}의 정보가 삭제됐습니다.'.format(_name))
    

# 학생이 한명이라도 존재하는지 알아보는 함수
def has_any_students():
    global students

    if students: return True
    return False

# 수강생 존재여부 : id 검색해서 students list의 index 값 리턴
def has_student_id(std_id):
    global students

    for i, std in enumerate(students):
        if std['id'] == std_id: return i
    
    return NOT_FOUND

# 메뉴 출력
def display_menu():
    print(line + ' Cloud MSA 반 수강생 관리 시스템 ' + line)
    print('1. 수강생 정보 등록')
    print('2. 수강생 목록 보기')
    print('3. 수강생 정보 수정')
    print('4. 수강생 정보 삭제')
    print('0. 종료')
    print()


while True:
    display_menu()

    menu = input('메뉴를 선택하세요 : ')

    if menu == '1':
        name = input('이름 : ')
        age = input('나이 : ')
        
        while not age.isdigit(): 
            print('나이는 숫자로 입력하세요.')
            age = input('나이 : ')

        major = input('전공 : ')
        register(name, age, major)

    elif menu == '2':
        if not has_any_students():
            print('등록된 학생이 한명도 없습니다.')
            continue

        display_students()
        
    elif menu == '3':
        if not has_any_students():
            print('등록된 학생이 한명도 없습니다.')
            continue
        
        _sid = enter_id()
        std_index = has_student_id(_sid)

        if std_index == NOT_FOUND:
            print('존재하지 않는 ID입니다.')
            continue

        update(std_index)
        

    elif menu == '4':
        if not has_any_students():
            print('등록된 학생이 한명도 없습니다.')
            continue

        _sid = enter_id()
        std_index = has_student_id(_sid)

        if std_index == NOT_FOUND:
            print('존재하지 않는 ID 입니다.')
            continue

        remove(std_index)
        

    elif menu == '0': 
        print('수강생 관리 프로그램을 종료합니다.')
        break

    else: 
        print()
        print('1, 2, 3, 4, 0 번 중 선택하세요')