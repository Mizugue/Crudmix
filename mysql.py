import MySQLdb

class Mysql():

    def __init__(self):
        self._ = True
        while True:
            print("")
            self.menu()
            self._ = False



    def menu(self):
        if self._:
            print('=========Products Manager==============-->Mysql')
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
            conn = MySQLdb.connect(
                db='pmysql',
                host='localhost',
                user='root',
                passwd='root'
            )
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS products(
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        name VARCHAR(30) NOT NULL,
                        price DECIMAL(8,2) NOT NULL,
                        stock INT NOT NULL);""")
            print('\n')
            return conn
        except MySQLdb.Error as e:
            return print(f"\nDoes not possible establishment a connection {e}"), exit()

    def disconnect(self, conn):
        if conn:
            conn.close()
            return print('Disconnecting from the Database...')

    def list(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM products')
        products = cursor.fetchall()
        if len(products) > 0:
            print('  Listing products  ')
            print("--------------------------")
            for product in products:
                print(f'ID: {product[0]}')
                print(f'Name: {product[1]}')
                print(f'Price: {product[2]}')
                print(f'Stock: {product[3]}')
                print("--------------------------")
        else:
            print("There is not products")

    def insert(self):
        conn = self.connect()
        cursor = conn.cursor()
        name = (input("Name of product: "))
        price = (float(input("Price of product: ")))
        stock = (int(input("Stock of product: ")))
        cursor.execute(f"INSERT INTO products (name, price, stock) VALUES ('{name}', {price}, {stock}) ")
        conn.commit()
        if cursor.rowcount == 1:
            print(f'The product {name} has been inserted with success')
        else:
            print('Did not possible execute the query')


    def update(self):
        conn = self.connect()
        cursor = conn.cursor()
        id = (int(input("Id of product: ")))
        name = (input("The new name of product: "))
        price = (float(input("The new price of product: ")))
        stock = (int(input("The new stock of product: ")))
        cursor.execute(f"UPDATE products SET name='{name}', price={price}, stock={stock} WHERE id={id};")
        conn.commit()

        if cursor.rowcount == 1:
            print(f'The product {name} has been updated with success')
        else:
            print('Did not possible execute the query')


    def delete(self):
        conn = self.connect()
        cursor = conn.cursor()
        id = (int(input("Report the id of which product you wanna to delete: ")))
        cursor.execute(f"DELETE from products WHERE id={id};")
        conn.commit()

        if cursor.rowcount == 1:
            print(f'The product has been deleted with success')
        else:
            print('Did not possible execute the query')



