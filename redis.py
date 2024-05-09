import redis

class Redis():

    def __init__(self):
        self._ = True
        while True:
            print("")
            self.menu()
            self._ = False



    def menu(self):
        if self._:
            print('=========Products Manager==============-->Redis')
            print('Select a option: ')
            print('1 - List the Products.')
            print('2 - Insert Products.')
            print('3 - Update Products.')
            print('4 - Delete Products.')
            print('5 - Disconnect from Database')
            op = int(input())
        else:
            print('1 - List the Products.')
            print('2 - Insert Products.')
            print('3 - Update Products.')
            print('4 - Delete Products.')
            print('5 - Disconnect from Database')
            op = int(input())

        if op in [1, 2, 3, 4, 5]:
            if op == 1:
                self.list()
            elif op == 2:
                self.insert()
            elif op == 3:
                self.update()
            elif op == 4:
                self.delete()
            elif op == 5:
                self.disconnect(self.connect())
        else:
            print('Invalid option')


    def connect(self):
        try:
            conn = redis.Redis(host='localhost', port=6379)
            return conn
        except:
            return print(f"\nDoes not possible establishment a connection"), exit()

    def disconnect(self, conn):
        if conn:
            conn.connection_pool.disconnect()
            return print('Disconnecting from the Database...'), quit()

    def generator_id(self):
        try:
            conn = self.connect()
            key = conn.get('key')
            if key:
                key = conn.incr('key')
                return key
            else:
                conn.set('key', 1)
                return 1
        except:
            print('Likely did there is a error')

    def chekey(self, key):
        conn = self.connect()
        data = conn.keys(pattern='products:*')
        data = [str(name, 'utf-8', 'ignore') for name in data]
        if key not in data:
            print(f'Chave Inválida: {key} ')
            return False
        else:
            return True

    def list(self):
        conn = self.connect()
        try:
            data = conn.keys(pattern='products:*')
            if len(data) > 0:
                print('Listing products....')
                for key in data:
                    product = conn.hgetall(key)  # Binary string
                    print(f" ID: {str(key, 'utf-8', 'ignore')}")
                    print(f" Product: {str(product[b'name'], 'utf-8', 'ignore')}")
                    print(f" Price: {str(product[b'price'], 'utf-8', 'ignore')}")
                    print(f" Stock: {str(product[b'stock'], 'utf-8', 'ignore')}")
                    print('--------------------------------------------------')
            else:
                print("There is not products")
        except:
            print(f'Likely did there is a error')


    def insert(self):
        conn = self.connect()
        name = (input("Name of product: "))
        price = (float(input("Price of product: ")))
        stock = (int(input("Stock of product: ")))

        product = {"name": name, "price": price, "stock": stock}
        key = f'produtos:{self.generator_id()}'

        try:
            res = conn.hmset(key, product)  # product:1 {x}
            if res:
                print(f'The product {name} has been inserted with success')
            else:
                print("Did not possible insert the product")
        except:
            print(f'Likely did there is a error')


    def update(self):
        conn = self.connect()
        _id = (int(input("Id of product: ")))
        name = (input("The new name of product: "))
        price = (float(input("The new price of product: ")))
        stock = (int(input("The new stock of product: ")))
        product = {"name": name, "price": price, "stock": stock}

        _ = self.checkey(_id)

        if _:
            try:
                res = conn.hmset(_id, product)  # produto:1 {x}
                if res:
                    print(f"The product {name} has been Updated")
            except:
                print("Did not possible Update the product")
        else:
            print("There is not documents with this id to Update")


    def delete(self):
        conn = self.connect()
        _id = (input("Report the id of which product you wanna to delete: "))
        try:
            res = conn.delete(_id)
            if res == 1:
                print(f'The product has been deleted with success')
            else:
                print("Without products to be deleted")
        except:
            print("Did not possible delete the product")




