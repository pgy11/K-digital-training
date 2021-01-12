hello = input('인사말 입력 : ')
print(hello, type(hello))

data = input('숫자 입력 : ')
print(data, type(data))

src = 100

# 문자열과 숫자는 더 할 수 없다. 
total = src + int(data) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(total)

total = 10 + 7.5
print(type(total))

# type cast 사용 시, value error에 유의해야한다.
#x = int('Hello python') # 문자열을 입력하면 value error 발생

# format 함수
x, y = 3, 4
z = x + y
print('{0} + {1} = {2}'.format(x,y,z))
print('{0}의 자료형은 {1}입니다'.format(z, type(z)))