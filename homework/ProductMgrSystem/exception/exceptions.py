class DuplicationException(Exception):

    def __init__(self, pid):
        super().__init__(self, '상품번호 {0}은 이미 존재하는 상품번호입니다.\n'.format(pid))

class RecordNotFoundException(Exception):

    def __init__(self, pid):
        super().__init__(self, '상품번호 {0}은 존재하지 않은 상품번호입니다.\n'.format(pid))

class UnvalidPIDException(Exception):

    def __init__(self, pid):
        super().__init__(self, '{0}은 유효하지 않는 상품번호입니다.\n'.format(pid))

class UnvalidPnameExceptrion(Exception):

    def __init__(self, pname):
        super().__init__(self, '{0}은 유효하지 않는 상품명입니다.\n'.format(pname))

class UnvalidPriceExceptrion(Exception):

    def __init__(self, price):
        super().__init__(self, '{0}은 유효하지 않는 가격입니다.\n'.format(price))

class UnvalidDescExcpetion(Exception):

    def __init__(self, desc):
        super().__init__(self, '{0}은 유효하지 않는 상품설명입니다.\n'.format(desc))

class UnvalidOptionExceptrion(Exception):

    def __init__(self, menu):
        super().__init__(self, '{0}은 유효하지 않는 메뉴번호입니다.\n'.format(menu))