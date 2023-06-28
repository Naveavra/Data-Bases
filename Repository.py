import atexit
import os
import sqlite3

from DAO import *


class Repository:
    def __init__(self,dbPath):
        self.conn = sqlite3.connect(dbPath)
        self.hats = Hats(self.conn)
        self.suppliers = Suppliers(self.conn)
        self.orders = Orders(self.conn)
        self.toppings = []
        self.supp = []
        self.location = []
        self.maxNumOfOrders = 0
    def close(self):
        self.conn.commit()
        self.conn.close()

    def createTables(self):
        self.conn.executescript("""
            CREATE TABLE IF NOT EXISTS hats(
                id INTEGER PRIMARY KEY,
                topping STRING NOT NULL,
                supplier INTEGER REFERENCES suppliers(id),
                quantity INTEGER NOT NULL
            );
        
                CREATE TABLE IF NOT EXISTS suppliers(
                id INTEGER PRIMARY KEY,
                name STRING NOT NULL
            );    
                CREATE TABLE IF NOT EXISTS orders(
                id INTEGER PRIMARY KEY,
                location STRING NOT NULL,
                hat INTEGER REFERENCES hats(id)
                );""")
        self.conn.commit()

    def setNumOrders(self,num):
        self.maxNumOfOrders = num

    def parseOrders(self,path):
        file = open(path,'r')
        content = file.read()
        lines = content.split("\n")
        idx = 1
        for line in lines:
            line = line.split(",")
            if line[1]!="":
                id = self.hats.findSupplierByTopping(line[1])
                self.orders.insert(order(idx,line[0],self.hats.findByToppingAndSupID(id,line[1])))
                # print(f"ORDERS:{idx}, {line[0]}, {line[1]}")
                idx+=1
                supName = self.suppliers.find(id)
                if self.maxNumOfOrders>0 and id!= None:
                    self.hats.order(int(id),line[1])
                    self.maxNumOfOrders-=1
                self.toppings.append(line[1])
                self.supp.append(supName)
                self.location.append(line[0])

    def configPath(self,path):
        file = open(path, 'r')
        content = file.read()
        lines = content.split("\n")
        totalNumOfOrders = 0
        for i in range(len(lines)):
            if i==0:
                line = lines[i].split(",")
                numOfhats = int(line[0])
                numOfSuppliers = line[1]
                continue
            line = lines[i].split(",")
            if(i<=int(numOfhats)):
                self.hats.insert(hat(line[0],line[1],line[2],line[3]))
                totalNumOfOrders += int(line[3])
            else:
                self.suppliers.insert(supplier(line[0],line[1]))
        self.setNumOrders(totalNumOfOrders)

    def output(self,path):
        output = open("output.txt","a")
        for i in range(len(self.toppings)):
            line = str(self.toppings[i]) + "," + str(self.supp[i])+","+str(self.location[i])
            output.write(line+"\n")
        output.close()


# atexit.register(repo.close)


