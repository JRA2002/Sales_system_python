import sqlite3

class Connection:
    def __init__(self):
        try:
            self.conn = sqlite3.connect('sales_system.db')
            self.createTables()
        except Exception as ex:
            print(ex)
         
    def createTables(self):
        try:
            self.cur = self.conn.cursor()

            self.cur.execute('''CREATE TABLE IF NOT EXISTS supplier
                (_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT)''')
            self.cur.execute('''CREATE TABLE IF NOT EXISTS products
                (_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT, price INTEGER,supplier_name TEXT)''')
            self.cur.execute('''CREATE TABLE IF NOT EXISTS customers
                (_id INTEGER PRIMARY KEY UNIQUE, name TEXT, last_name TEXT, phone INTEGER)''')
            self.cur.execute('''CREATE TABLE IF NOT EXISTS sales
                (_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, product_id INTEGER, 
                total INTEGER, FOREIGN KEY(product_id) REFERENCES products(_id))''')

            self.conn.commit()

            self.cur.close()
            
        except Exception as ex:
            print(ex)
        self.conn.close()
        
        