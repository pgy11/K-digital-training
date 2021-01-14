
line = '=' * 20

def menu_display():
    print(line + ' 상품관리 시스템 ' + line)
    print('1. 상품정보 등록')
    print('2. 상품정보 조회')
    print('3. 상품정보 수정 ')
    print('4. 상품정보 삭제')
    print('5. 상품정보 전체삭제')
    print('6. 종료')
    print()

def input_display():
    pid = input('상품번호 입력: ')
    pname = input('상품명 입력: ')
    price = input('가격입력: ')
    desc = input('상품설명 입력: ')

    return [pid, pname, price, desc]


def list_display(products):
    for prod in products:
        print(prod)

def remove_input_display():
    return input('삭제할 상품번호 입력: ')

def pid_input_display():
    return input('변경할 상품번호 입력: ')

def update_info_display():
    print(line + ' 변경하고 싶은 정보 ' + line)
    print('1. 상품번호')
    print('2. 상품명')
    print('3. 가격')
    print('4. 상품설명')
    print()

def update_pid_input_display():
    return input('상품번호 입력: ')

def update_pname_input_display():
    return input('상품명 입력: ')

def update_price_input_display():
    return input('가격입력: ')

def update_desc_input_display():
    return input('상품설명 입력')

def menu_select_display():
    return input('메뉴선택: ')


def msg_display(msg):
    print(msg)