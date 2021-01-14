import os
from entity.product import Product

FILE_PATH = 'dao/products.dat'

def load_data():
    products = []

    if os.path.isfile(FILE_PATH):
        with open(FILE_PATH, 'r') as f:
            while True:
                data = f.readline()

                if not data: break

                info = data.rstrip().split(', ')
                if len(info) == 4:
                    pid, pname = info[0], info[1]
                    price, desc = info[2], info[3]
                    product = Product(pid, pname, int(price), desc)
                    products.append(product)
    
    return products



def save_data(products):

    with open(FILE_PATH, 'w') as f:
        for prod in products:
            pid, pname  = prod.get_pid(), prod.get_pname()
            price, desc = prod.get_price(), prod.get_desc()
            
            f.write('{0}, {1}, {2}, {3}\n'.format(pid, pname, price, desc))