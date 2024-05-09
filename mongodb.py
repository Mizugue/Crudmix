from bson import errors as beeros
from pymongo import MongoClient, errors
from bson.objectid import ObjectId

class MongoDB():

    def __init__(self):
        self._ = True
        while True:
            print("")
            self.menu()
            self._ = False



    def menu(self):
        if self._:
            print('=========Products Manager==============-->MongoDB')
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
            conn = MongoClient('localhost', 27017)
            return conn
        except errors.PyMongoError as e:
            return print(f"\nDoes not possible establishment a connection {e}"), exit()

    def disconnect(self, conn):
        if conn:
            conn.close()
            return print('Disconnecting from the Database...'), quit()


    def list(self):
        conn = self.connect()
        db = conn.pmongo
        try:
            if db.products.count_documents({}) > 0:
                products = db.products.find()
                print('  Listing products  ')
                print("--------------------------")
                for product in products:
                    print(f"ID: {product['_id']}")
                    print(f"Name: {product['name']}")
                    print(f"Price: {product['price']}")
                    print(f"Stock: {product['stock']}")
                    print("--------------------------")
            else:
                print("There is not products")
        except errors.PyMongoError as e:
            print(f'Likely did there is a error {e}')


    def insert(self):
        conn = self.connect()
        db = conn.pmongo
        name = (input("Name of product: "))
        price = (float(input("Price of product: ")))
        stock = (int(input("Stock of product: ")))
        try:
            db.products.insert_one({
                "name": name,
                "price": price,
                "stock": stock
            })
            print(f'The product {name} has been inserted with success')
        except errors.PyMongoError as e:
            print(f'Likely did there is a error {e}')



    def update(self):
        conn = self.connect()
        db = conn.pmongo
        _id = (int(input("Id of product: ")))
        name = (input("The new name of product: "))
        price = (float(input("The new price of product: ")))
        stock = (int(input("The new stock of product: ")))
        try:
            if db.products.count_documents({}) > 0:
                res = db.products.update_one(
                    {"_id": ObjectId(_id)},
                    {"$set": {"name": name, "price": price, "stock": stock}})

                if res.modified_count == 1:
                    print(f"The product {name} has been Updated")
                else:
                    print("Did not possible Update the product")
            else:
                print("There is not documents to Update")
        except errors.PyMongoError as e:
            print(f'Likely did there is a error {e}')
        except beeros.InvalidId as f:
            print(f"Invalid ID {f}")

    def delete(self):
        conn = self.connect()
        db = conn.pmongo
        _id = (input("Report the id of which product you wanna to delete: "))
        try:
            if db.products.count_documents({}) > 0:
                res = db.products.delete_one({
                    "_id": ObjectId(_id)
                })

                if res.deleted_count > 0:
                    print(f'The product has been deleted with success')
                else:
                    print("Did not possible delete the product")
            else:
                print("Without products to be deleted")
        except errors.PyMongoError as e:
            print(f'Likely did there is a error {e}')
        except beeros.InvalidId as f:
            print(f"Invalid ID {f}")




