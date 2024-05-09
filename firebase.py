import pyrebase

class Firebase():

    def __init__(self):
        self._ = True
        while True:
            print("")
            self.menu()
            self._ = False



    def menu(self):
        if self._:
            print('=========Products Manager==============-->Firebase')
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
                self.disconnect()
        else:
            print('Invalid option')


    def connect(self):
        config = {
            "apiKey": "AIzaSyDdQ9H6_tdHRY_-0Ke3Did0ZsK1p5Ye14E",
            "authDomain": "https://mzgbd-fbe28-default-rtdb.firebaseio.com",
            "projectId": "mzgbd-fbe28",
            "databaseURL": "https://mzgbd-fbe28-default-rtdb.firebaseio.com",
            "storageBucket": "mzgbd-fbe28.appspot.com",
            "messagingSenderId": "362878525155",
            "appId": "1:362878525155:web:0575bd846ef5312c3eefd6",
            "measurementId": "G-GBT7NK6E7H"
        }

        try:
            conn = pyrebase.initialize_app(config)
            db = conn.database()
            return db
        except:
            print(f'Failed to connect in the database')

    def disconnect(self):
        return print('Disconnecting from the Database...'), quit()


    def list(self):
        db = self.connect()
        products = db.child("products").get()
        if products.val():
            print("Listing produtcs...")
            print("..........")
            for product in products.each():
                print(f"ID: {product.key()}")
                print(f"Name: {product.val()['name']}")
                print(f"Price: {product.val()['price']}")
                print(f"Stock: {product.val()['stock']}")
                print('---------------------------------------')
        else:
            print("There is not products ")


    def insert(self):
        db = self.connect()
        name = (input("Name of product: "))
        price = (float(input("Price: ")))
        stock = (int(input("Stock: ")))
        product = {"name": name, "price": price, "stock": stock}
        res = db.child("products").push(product)
        if 'name' in res:
            print(f"The product {name} has been inserted with success")
        else:
            print("Did not possible insert the product")

    def update(self):
        db = self.connect()
        _id = (input("Id: "))
        product = db.child('products').child(_id).get()

        if product.val():
            name = (input("Name: "))
            price = (float(input("Price: ")))
            stock = (int(input("Stock: ")))
            new_product = {"name": name, "price": price, "stock": stock}
            db.child('produtos').child(_id).update(new_product)
            print(f"The product {name} has been updated with success")
        else:
            print("The product did not found")

    def delete(self):
        db = self.connect()
        _id = (input("Id: "))
        product = db.child('products').child(_id).get()

        if product.val():
            db.child("products").child(_id).remove()
            print("The product has been deleted with success")
        else:
            print("There is not product with this id")


