
DEFAULT_NUM = '-1'

class Todo:

    def __init__(self, name, content):
        self.num = DEFAULT_NUM
        self.name = name
        self.content = content


    # 객체를 표현하는 문자열
    def __str__(self):
        return 'No.{0} {1} 작성자: {2}'.format(self.num, self.content, self.name)
    
    # 번호 설정, 서비스에서 처리
    def set_num(self, num):
        self.num = num

    # 번호를 가져온다
    def get_num(self):
        return self.num
    
    # 일정내용 설정
    def set_content(self, content):
        self.content = content

    # 일정내용 가져오기
    def get_content(self):
        return self.content

    # 작성자 가져오기
    def get_name(self):
        return self.name