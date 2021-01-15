import os
from entity.student import Student

# 프로그램 시작시 student.dat 파일을 불러온다.

def load_list_from_file():
    students = []
    has_file = os.path.isfile('students.dat')
    
    if has_file:
        with open('students.dat', 'r') as f:
            while True:
                data = f.readline()

                if not data: break

                if len(data.split('|')) == 2:
                    std_info = data.split('|')[1].strip().rstrip().split(',')

                    students.append(Student(std_info[0], std_info[1], std_info[2], std_info[3]))
            
    return students


# 프로그램 종료시 students.dat 파일에 저장.
def save_list_to_file(students):

    with open('students.dat', 'w') as f:
        for i, std in enumerate(students):
            f.write('{0}번째 | {1},{2},{3},{4}\n'.format(i, std.sid,
             std.name, std.age, std.major))