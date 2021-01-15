# 입력 데이터 유효성 검사, service 비즈니스 로직 호출, data 저장, view(template) 선택
from service.stdservice import StudentService
from view_template.template import display_msg

def has_info(info):
    if info == '': return False
    return True

class StudentController:

    def register(self, student):
        if not has_info(student.sid) or not has_info(student.name) or not has_info(student.major):
            display_msg('유효한 입력이 아닙니다.')
            return

        msg = StudentService.register(student)
        display_msg(msg)

    def display_students(self):
        msg = StudentService.display_students()
        display_msg(msg)

    def update(self, sid, major):
        if not has_info(sid) or not has_info(major):
            display_msg('유효한 입력이 아닙니다.')
            return

        msg = StudentService.update(sid, major)
        display_msg(msg)

    def remove(self, sid):
        if not has_info(sid):
            display_msg('유효한 입력이 아닙니다.')
            return

        msg = StudentService.remove(sid)
        display_msg(msg)

    def read_file(self):
        StudentService.read_file()
        

    def write_file(self):
        StudentService.write_file()