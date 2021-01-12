"""
try:
    # 예외 발생 가능성이 있는 실행문
    정상흐름 구현

except:
    #예외 발생 할 때 실행하는 실행문
    pass

finally:
    # 예외 발생 여부와 상관없이 실행하는 실행문 
"""

arr = [1,2,3,4,5]
div_sum = 0

try:
    r = int(input('반지름 입력 : ')) # ValueError
    #for num in arr: # from index 0 to index len(arr) - 1
    #    print(num)

    for i in range(len(arr)+1):
        div_sum += arr[i] / r # ZeroDivisionError
        print('{0}번째 데이터 : {1}'.format(i, arr[i])) # IndexError

    print('원의 반지름 :', r)
    print('원 둘레 :', 2*3.14*r)
    print('원 넓이 :', 3.14 * (r**2))

# multi exception 처리시, 구체적인 예외부터 작성하고 이후 범용적인 예외를 작성한다.
# i.e. 자식 클래스부터 처리

except ValueError:
    print('ValueError : 숫자로 입력해야합니다.')

except IndexError:
    print('IndexError : 리스트의 인덱스 0 ~ {0}까지 접근가능'.format(len(arr)))

except Exception as error:
    print(error,'프로그램 비정상 종료')

finally:
    print('예외 여부 관계 없이 출력합니다.')

# 사용자 정의 예외 - 클래스
# 1. Exception을 상속받는 사용자 정의 예외 클래스 정의
# 2. 함수 예외 상황이 발생 시, raise 이용하여 예외 발생
# 3. 호출하는 쪽에서 처리 
# try: 
#  사용자 정의 예외 발생하는 함수 호출
# except 사용자 정의 예외클래스 타입:
#  예외처리 실행문
# finally:
#  무조건 실행되는 실행문   