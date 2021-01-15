class DuplicateException(Exception):

    def __init__(self, info):
        super().__init__(self, '{0}은 이미 등록된 학번입니다.'.format(info))

class IDNotFoundException(Exception):
    
    def __init__(self, info):
        super().__init__(self, '{0}은 존재하지 않는 학번입니다.'.format(info))

class StudentNotFoundException(Exception):

    def __init__(self):
        super().__init__(self, '학생이 한명도 없습니다.')
