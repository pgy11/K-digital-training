# 비즈니스 로직 처리
from exception.userexcept import DuplicateException, IDNotFoundException, StudentNotFoundException
from dao.filedao import load_list_from_file, save_list_to_file

NOT_FOUND = -1
line = '='*6

# 학생이 한명이라도 존재하는지 알아보는 함수
def has_any_students():
    if StudentService.students: return True
    
    return False

# 수강생 존재여부 : id 검색해서 students list의 index 값 리턴
def has_student_id(std_id):
    for i, std in enumerate(StudentService.students):
        if std.sid == std_id: return i
        
    return NOT_FOUND


class StudentService:

    # 클래스 변수, 프로그램 시작시 파일에서 Student객체 읽어서 한번 초기화
    students = [] 

    # 수강생 등록 : list students에 정보 저장, 만약 학번이 중복되는 경우 DuplicationException 발생
    @classmethod
    def register(cls, student):
        index = has_student_id(student.sid)

        if index == NOT_FOUND:
            cls.students.append(student)
            return '{0}이(가) 등록 됐습니다.\n'.format(student.name)
        
        else:
            return str(DuplicateException(student.sid))
         
    
    # 수강생 수정 : id를 검색해서 전공정보 수정, 존재하지 않는 경우, IDNotFoundException 발생
    @classmethod
    def update(cls, sid, major):
        index = has_student_id(sid)

        if index != NOT_FOUND:
            cls.students[index].major = major
            name = cls.students[index].name
            return '{0}의 전공이 {1}으로 수정됐습니다.\n'.format(name, major)
        
        else: return str(IDNotFoundException(sid))

    
    # 수강생 삭제 : id를 검색해서 수강생 정보 삭제, 존재하지 않는 경우, IDNotFoundException 발생
    @classmethod
    def remove(cls, sid):
        index = has_student_id(sid)

        if index != NOT_FOUND:
            name = cls.students[index].name
            del cls.students[index]
            return '{0}의 정보가 삭제됐습니다.\n'.format(name)
        
        else: return str(IDNotFoundException(sid))

    # 수강생 조회
    @classmethod
    def display_students(cls):
        if not has_any_students():
            return str(StudentNotFoundException())

        else:
            print(line + ' 수강생목록 ' + line)

            for std in cls.students:
                print(std) # Student 클래스에서 재정의한 __str__() 호출

            return '조회를 완료하였습니다.\n'

        
    @classmethod
    def read_file(cls):
        cls.students = load_list_from_file()


    @classmethod
    def write_file(cls):
        save_list_to_file(cls.students)
        

