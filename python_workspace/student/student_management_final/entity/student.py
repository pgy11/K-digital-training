class Student:
    
    # 생성자: student id, name, age, major
    def __init__(self, sid, name, age, major):
        self.sid = sid
        self.name = name
        self.age = age
        self.major = major
    
    def __eq__(self, sid):
        if self.sid == id: return True

        return False
    
    # 객체를 대표하는 문자열
    def __str__(self):
        return '학번: {0}, 이름: {1}, 나이: {2}, 전공: {3}'.format(self.sid, self.name, self.age, self.major)
        
    