"""
if 조건식1:
    실행문1
    
elif 조건식2: # 조건식 1이 False
     실행문2

else: 실행문3 # 조건식1, 조건식2가 모두 False
"""

month = input('월 입력 : ')

if month.isdigit(): 
    m = int(month)
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m ==12:
        print('{0}월은 31일까지 있습니다.'.format(m))

    elif m == 2: 
        print('{0}월은 28일까지 있습니다.'.format(m))

    elif m == 4 or m == 6 or m == 9 or m == 11:
        print('{0}월은 30일까지 있습니다.'.format(m))

    else: print('1~12사이의 값을 입력해야합니다.')

else: print('1~12사이의 값을 입력해야합니다.')

# list type : [item1, item2, ...]
# arr = ['python', 8, 3.14, true, [7,8,5]]
# +, *(iteration), len()
# append(), insert(), del, pop()
arr1 = [1,2,3]
arr2 = ['a', 'b', 'c']
print(arr1 + arr2)
print(arr1*3)
print((arr1+arr2)*2)

print(arr1)
arr1.append(4) # last index + 1에 아이템을 추가
print(arr1) 

arr1.insert(1, 7) # 해당 index에 아이템을 삽입
print(arr1)

arr1.pop(1) # 해당 index의 아이템을 삭제
print(arr1)

arr1.append(1)
arr1.remove(1) # 배열을 처음부터 조회하여, 첫번째로 탐색된 item을 삭제한다.  
print(arr1)

arr1.clear() # 모든 아이템들을 제거
print(arr1)

# for 반복자 in 반복 할 수 있는 데이터(list, dictionary, string, range()) : 
# 실행문
index = 0
for data in arr2: 
    print('arr2[{0}] = {1}'.format(index, data))
    index += 1