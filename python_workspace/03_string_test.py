hello = '안녕하세요' # 문자열 배열 index 0 ~ len(hello)-1
print(hello[1:3]) # index 1부터 (3-1)개 문자열
print(len(hello)) # 문자열 길이

# 형식 지정 시 index error 주의 {} > format의 인수 개수로 설정되면 에러 발생
# IndexError: Replacement index 1 out of range for positional args tuple
#print("문자열 '안녕하세요' 길이는 {0}입니다. {1}".format(len(hello)))
print("문자열 '안녕하세요' 길이는 {0}입니다.", len(hello), hello)

hello = 'Hello Python'
print(hello.lower())
print(hello.upper())
hello = '  Hello Python  '
print(hello.strip() + '!!')

num_string = input('숫자 입력')
print('{0}이 숫자인가? {1}'.format(num_string,num_string.isdigit(), end = ' '))

hello = 'Hello Python'
print("'l'문자열 검색", hello.find('l')) # find string from first index
print("'l'문자열 검색", hello.rfind('l')) # find string from last index
print("'l'문자열 포함여부", ('l' in hello)) # 문자열 포함 여부

print(hello.split(' ')) # split token으로 문자열을 나누어 list로 반환

