class Person:

    def __init__(self, pid, name):
        self.pid = pid
        self.name = name
    
    def display_info(self):
        print('ID: {0}, 이름: {1}, '.format(self.pid, self.name), end = '')
    


class Student(Person):

    def __init__(self, sid, name, major):
        super().__init__(sid, name)
        self.major = major
    
    def display_std_info(self):
        super().display_info()
        print('전공: {0}'.format(self.major))

    