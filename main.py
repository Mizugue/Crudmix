from mysql import Mysql
from postgresql import PostgreSQL
from sqlite import SQLite
from mongodb import MongoDB
from redis import Redis
from couchdbdb import CouchDB
from firebase import Firebase
class Manager:
    def __init__(self):
        self.menu()

    def menu(self):
        print("Which type of database will you choice? ")
        print("1) SQL")
        print("2) NOSQL")
        op = (int(input("----> ")))
        if op in [1, 2]:
            if op == 1:
                opsql = (int(input("< (1)Mysql  (2)PostgreSQL  (3)SQLite > ")))
                if opsql in [1, 2, 3]:
                    if opsql == 1:
                        Mysql()
                    elif opsql == 2:
                        PostgreSQL()
                    elif opsql == 3:
                        SQLite()
                else:
                    return print("Does not exist this option"), self.menu()

            elif op == 2:
                opnosql = (int(input("< (1)MongoDB  (2)Redis  (3)CouchDB  (4)Firebase > ")))
                if opnosql in [1, 2, 3, 4]:
                    if opnosql == 1:
                        MongoDB()

                    elif opnosql == 2:
                        print(1)
                        Redis()

                    elif opnosql == 3:
                        print(1)
                        CouchDB()

                    elif opnosql == 4:
                        print(1)
                        Firebase()

                else:
                    return print("Does not exist this option"), self.menu()

        else:
            return print("Does not exist this option"), self.menu()


Manager()
