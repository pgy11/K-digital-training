# 사용자 예외처리 클래스

class NumNotFoundException(Exception):

    def __init__(self, num):
        super().__init__(self, '{0}번째 일정을 찾을 수 없습니다.\n'.format(num))
