# node stream -> filter stream -> read, write
# console, memory, network, file
# 스트림 형태(byte)로 전달

# text data file 출력
f = open('hello.txt', 'w')
f.write('Hello Python\n')
f.close() # resource 반납

# with을 사용하면 close()를 호출하지 않아도 사용한 자원(파일)을 반납한다
# with open(파일명, mode) as file객체명 :
# mode에는 'w'(overwrite), 'a'(append write), 'r'(read)이 있다.
with open('hello.txt', 'a') as f:
    f.write('content has been added.\n')

# file read => console 출력
with open('hello.txt', 'r') as f:
    for line in f: print(line, end = '')

# console 입력 => file write
data = input('파일에 쓸 내용을 입력하세요. : ')
with open('hello.txt', 'a') as f:
    f.write(data + '\n')

# file read => file write(file copy)
read_f = open('hello.txt', 'r')
write_f = open('hello_copy.txt', 'w')
write_f.write(read_f.read())

read_f.close()
write_f.close()

import random

kors = list('가나다라마바사아자차카타파하')

with open('info.txt', 'w') as f:
    for i in range(1000):
        name = random.choice(kors) + random.choice(kors)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)

        f.write('{0}, {1}, {2}\n'.format(name, weight, height))

with open('info.txt', 'r') as f:
    for line in f:
        name, weight, height = line.strip().split(', ')

        if not name or not weight or not height: continue

        bmi = int(weight) / ((int(height)*0.01)**2)
        result = ''

        if bmi >= 25: result = '과체중'
        elif bmi >= 18.5: result = '정상체중'
        else: result = '저체중'

        print('\n'.join([
            '이름: {}',
            '몸무게: {}',
            '키: {}',
            'BMI: {}',
            '결과: {}'
        ]).format(name, weight, height, bmi, result))
        print()

# 파일을 read 할 때, 파일이 존재해야한다.
# FileNotFoundError: [Errno 2] No such file or directory: 'player_list.txt'
f = open('player_list.txt', 'r')