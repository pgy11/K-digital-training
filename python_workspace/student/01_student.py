# 수강생 관리 시스템
students = []
sid = 1

line = '='*6

while True:
    print(line + ' Cloud MSA 반 수강생 관리 시스템 ' + line)
    print('1. 수강생 정보 등록')
    print('2. 수강생 목록 보기')
    print('3. 수강생 정보 수정')
    print('4. 수강생 정보 삭제')
    print('0. 종료')
    print()

    menu = input('메뉴를 선택하세요 : ')

    if menu == '1':
        name = input('이름 : ')
        age = input('나이 : ')
        
        while not age.isdigit(): 
            print('나이는 숫자로 입력하세요.')
            age = input('나이 : ')

        major = input('전공 : ')

        student = {'id':sid, 'name':name, 'age': int(age)}
        students.append(student)
        sid += 1
        print('{0}이 성공적으로 등록됐습니다.'.format(name))

    elif menu == '2':
        print(line + '수강생 목록 보기' + line)
        print(students)
        
    elif menu == '3':
        _sid = input('학생의 전공을 수정할 ID를 입력하세요 : ')
        has_id = False
        k = 0
        
        while not _sid.isdigit():
            print('숫자를 입력하세요')
            _sid = input('ID를 입력하세요. : ')
        
        for std in students:
            if std['id'] == int(_sid):
                has_id = True
                break
            k += 1
        
        if not has_id:
            print('존재하지 않는 ID 입니다.')

        else:
            _major = input('전공을 입력하세요. : ')
            _name = students[k]['name']
            students[k]['major'] = _major
            print('{0}의 전공이 {1}으로 수정됐습니다.'.format(_name, _major))

    elif menu == '4':
        _sid = input('삭제할 학생의 ID를 입력하세요. : ')
        has_id = False
        k = 0

        while not _sid.isdigit():
            print('숫자를 입력하세요.')
            _sid = input('ID를 입력하세요. : ')

        for std in students:
            if std['id'] == int(_sid):
                has_id = True
                break
            k += 1
        
        if not has_id:
            print('존재하지 않는 ID 입니다.')
        
        else:
            _name = students[k]['name']
            del students[k]
            print('{0}의 정보가 삭제됐습니다.'.format(_name))

    elif menu == '0': 
        print('수강생 관리 프로그램을 종료합니다.')
        break

    else: 
        print()
        print('1, 2, 3, 4, 0 번 중 선택하세요')

# Today homework
# github : python_workshop repository 생성 - 01.todos.py 작성해보기
# 01_todos.py
# {'todoNum':todoNum, 'title':title}
# 등록, 수정, 삭제, 일정목록, 전체삭제