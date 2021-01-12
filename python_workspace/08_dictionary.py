# dictionary type : variable_name = {'name' : 'value', ...} value : int, float, boolean, str, list
# value access : variable_name['name'] 
student = {'name' : 'Gil-dong', 'age' : 26, 'major' : '컴공'}
print("이름 : {0}, 나이 : {1}, 전공 : {2}".format(student['name'], student['age'], student['major']))
students = []
students.append({'name' : 'Chul-soo', 'age' : 26, 'major' : '컴공'})
students.append({'name' : 'Min-soo', 'age' : 25, 'major' : '정보보호'})

# value에 접근 할 때, 유효한 name(key)이여야 함
# id = student['student_id'] # key error 

for s in students:
    print("이름 : {0}, 나이 : {1}, 전공 : {2}".format(s['name'], s['age'], s['major']))

# dictionary 추가 수정 : 'name':value 쌍으로 추가 수정 ("name"이 존재하면, 수정한다. 존재하지 않으면 추가한다.)
students[0]['student_id'] = 'CloudMSA01'
print(students[0])

students[0]['major'] = '컴퓨터 공학'
print(students[0])

# dictionary 삭제
del students[0]['student_id']
print(students[0])

# get() : key check. 없는 경우 : None 반환
key = input('student 속성 입력(name, age, major) : ')
while students[0].get(key) is None:
    key = input('student 속성 입력(name, age, major) : ')
else: print('{0} key의 value 값 : {1}'.format(key, students[0][key]))
