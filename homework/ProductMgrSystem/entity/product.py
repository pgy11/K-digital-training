class Product:

    def __init__(self, pid, pname, price, desc):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.desc = desc
    

    def __eq__(self, pid):
        if self.pid == pid: return True
        return False
    

    def __str__(self):
        return '상품번호: {0}, 상품명: {1}, 가격: {2}, 설명: {3}'.format(self.pid,
         self.pname, self.price, self.desc)

    def set_pid(self, pid):
        self.pid = pid
    
    def get_pid(self):
        return self.pid
    
    def set_pname(self, pname):
        self.pname = pname
    
    def get_pname(self):
        return self.pname
    
    def set_price(self, price):
        self.price = price
    
    def get_price(self):
        return self.price
    
    def set_desc(self, desc):
        self.desc = desc
    
    def get_desc(self):
        return self.desc