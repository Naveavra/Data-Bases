from DTO import *

class Hats:
    def __init__(self, conn):
        self.conn = conn
        self.repo = self

    def insert(self, hat):
        self.conn.execute("""
                            INSERT INTO hats(id, topping, supplier, quantity) VALUES (?, ?, ?, ?)
                            """, [hat.id,hat.topping,hat.supplier,hat.quantity])
    def findByTopping(self,topping):
        c=self.conn.execute("""SELECT id FROM hats WHERE topping = ? AND quantity > 0 """,[topping])
        res = c.fetchall()
        empty = []
        for i in range(len(res)):
            empty.append(res[i][0])
        empty.sort()
        if(len(empty)>0):
            print(f"THE ID FOUND BY TOPPING IN HATS IS: {empty[0]}")
            return empty[0]
    def findByToppingAndSupID(self,supID,topp):
        c = self.conn.cursor()
        c.execute("""SELECT id FROM hats WHERE supplier = ? AND topping = ?""",(supID,topp))
        res = c.fetchall()
        empty = []
        for i in range(len(res)):
            empty.append(res[i][0])
        if(len(empty)>0):
            return empty[0]

    def find(self, id):
        c = self.conn.cursor()
        c.execute("""
                SELECT * FROM hats WHERE id = ?
                """, [id])
        return c.fetchone()[0]

    def findSupplierByTopping(self,topping):
        c=self.conn.cursor()
        c.execute("""SELECT supplier FROM hats WHERE topping = ? and quantity > 0""",[topping])
        res = c.fetchall()
        empty = []
        for i in range(len(res)):
            empty.append(res[i][0])
        empty.sort()
        if(len(empty)>0):
            return empty[0]

    def findAll(self):
        c = self.conn.cursor()
        all = c.execute("""
                SELECT * FROM hats order by
                 id asc
                """).fetchall()
        return [Hats(*row) for row in all]

    def order(self,suppID,topping):
        c= self.conn.cursor()
        # print(f"id we got in order is{suppID}")
        c.execute("""SELECT quantity FROM hats WHERE supplier =? AND topping = ?""",(suppID,topping))
        prev = c.fetchone()
        if(prev!=None):
            prev = prev[0]
            # print(f"{prev} is the previous quantity of id : {suppID}, current amount is :{int(prev)-1}")
            c.execute("""UPDATE hats
            SET quantity = ?
            WHERE supplier = ? AND topping = ?""",(int(prev)-1,suppID,topping))
            self.conn.commit()

    def selectAll(self):
        c=self.conn.cursor()
        c.execute("""SELECT * FROM hats""")
        temp = list(c.fetchall())
        print(temp)


class Suppliers:
    def __init__(self, conn):
        self.conn = conn

    def insert(self,supplier):
        self.conn.execute("""
                          INSERT INTO suppliers(id, name) VALUES (?, ?)
                          """, [supplier.id,supplier.name])
        self.conn.commit()
    def find(self,id):
        c = self.conn.cursor()
        c.execute("""
                SELECT * FROM suppliers WHERE id = ?
                """, [id])
        res = c.fetchone()
        if res!= None:
            return res[1]

    def findAll(self):
        c = self.conn.cursor()
        all = c.execute("""
                Select * FROM suppliers order by id asc
                """).fetchall()
        return [Suppliers(*row) for row in all]

class Orders:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, order):
        self.conn.execute("""
                     INSERT INTO orders(id, location, hat) VALUES (?, ?, ?)
                     """, [order.id, order.location, order.hat])
        self.conn.commit()
    def find(self):
        c = self.conn.cursor()
        c.execute("""
                SELECT * FROM orders WHERE id = ?
                """, [id])
        return order(*c.fetchone())

    def findAll(self):
        c = self.conn.cursor()
        all = c.execute("""
                Select * FROM orders order by id asc
                """).fetchall()
        return [order(*row) for row in all]

