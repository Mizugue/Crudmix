import socket
import couchdb

class CouchDB():

    def __init__(self):
        self._ = True
        while True:
            print("")
            self.menu()
            self._ = False



    def menu(self):
        if self._:
            print('=========Products Manager==============-->CouchDB')
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
        user = 'jc'
        password = 'jc'
        conn = couchdb.Server(f'http://{user}:{password}@localhost:5984')
        base = 'pcouch'
        if base in conn:
            db = conn[base]
            return db
        else:
            try:
                db = conn.create(base)
                return db
            except socket.gaierror as e:
                print(f'Failed to connect in the database {e}')
            except couchdb.http.Unauthorized as f:
                print(f'Without permission {f}')
            except ConnectionRefusedError as g:
                print(f'Did not possible access the database {g}')

    def disconnect(self):
        return print('Disconnecting from the Database...'), quit()


    def list(self):
        db = self.connect()
        if db:
            if db.info()['doc_count'] > 0:
                print("Listing...")
                print('--------------------------')
                for doc in db:
                    print(f"ID: {db[doc]['_id']}")
                    print(f"Rev: {db[doc]['_rev']}")
                    print(f"Name: {db[doc]['name']}")
                    print(f"Price: {db[doc]['price']}")
                    print(f"Stock: {db[doc]['stock']}")
                    print("--------------------------")
            else:
                print("There is not products ")
        else:
            print("Did not possible list the products")

    def insert(self):
        db = self.connect()
        if db:
            name = (input("Name of product: "))
            price = (float(input("Price: ")))
            stock = (int(input("Stock: ")))
            product = {"name": name, "price": price, "stock": stock}
            res = db.save(product)

            if res:
                print(f"The product {name} has been inserted with success")
            else:
                print("Did not possible insert the product")
        else:
            print("Did not possible connect to database")

    def update(self):
        db = self.connect()
        if db:
            id = (input("Id: "))

            try:
                doc = db[id]
                name = (input("Name: "))
                price = (float(input("Price: ")))
                stock = (int(input("Stock: ")))

                doc['name'] = name
                doc['price'] = price
                doc['stock'] = stock
                db[doc.id] = doc
                print(f"The product {name} has been updated with success")
            except:
                print("The product did not found")
        else:
            print("Did not possible to connect in the database")


    def delete(self):
        db = self.connect()
        if db:
            _id = (input("Id: "))

            try:
                db.delete(db[_id])
                print("The product has been deleted with success")
            except:
                print("There is not product with this id")
        else:
            print("Did not possible to connect in the database")



