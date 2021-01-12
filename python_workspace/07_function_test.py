# def 함수명([paramter1[, parameter2[, ...]]):
#  실행문
#  [return data]
# 함수 정의 --> 함수 호출
# 함수 호출 시, 정의된 함수의 argument들을 맞춰줘야한다.
# 가변 매개변수(*argument)를 사용하여 함수 호출 시마다 argument를 다르게 줄 수 있다.
# 기본 매개변수(argument=값) 사용하여 호출 시 해당 argument에 값을 주지않고 사용 할 수 있다.
# 함수정의
def print_3_times(*values, data = 'test'):
    for value in values:
        print('{0} : hello function {1}'.format(value, data))

# 함수 호출
print_3_times('test')
print_3_times('test', 'test')
print_3_times()
print_3_times(data = 'test5')

def test_arguments(a, b=10, c=20):
    print('{0}: {1} : {2}'.format(a,b,c))

test_arguments(5) # b, c는 기본값-> 5 : 10 : 20
test_arguments(b=10, a=4, c=7) # 순서상관없이 변수에 값 매핑 -> 4 : 10 : 7
test_arguments(1, 2, 3) # 순서대로 매핑 -> 1 : 2 : 3

def test_return_none():
    return # return : function 종료 - 이 함수로 호출한 곳으로 값 또는 None 반환

print(test_return_none()) # return data가 없는 경우 None 반환

def test_return(a, b):
    total = a + b
    return total

print(test_return(4,5))

def mul(*values):
    total = 1

    for value in values:
        total *= value
    
    return total

print(mul(5,7,9,10))

# tuple : list와 유사하지만, 값 변경 불가 변수명 = (value1, value2, ...)
tuple_data = (1,2,3,4,5)
list_data = [1,2,3,4,5]

for tdata in tuple_data:
    print(tdata, end = ' ')
print()

for ldata in list_data:
    print(ldata, end = ' ')

# TypeError: 'tuple' object does not support item assignment
# tuple_data[1] = 1 # type error, 값 변경 할 수 없음
# 함수에서 여러개의 값을 반환 할 때 사용 
print()

def test_tuple():
    return 10, 20

a, b = test_tuple()
print('{0} + {1} = {2}'.format(a, b, a + b))

# 람다 : lambda argumentlist : return - 1회성 익명함수
list_input = [1,2,3,4,5]
output_list = map(lambda x: x*x, list_input)
print(list_input)
print(list(output_list))

output_filter = filter(lambda data: data<3, list_input)
print(list_input)
print(list(output_filter))
