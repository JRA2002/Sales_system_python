# Form implementation generated from reading ui file 'ventas3.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import sqlite3

conn = sqlite3.connect('sales_system.db')

cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS products
    (name TEXT, price INTEGER)''')
cur.execute('''CREATE TABLE IF NOT EXISTS supplier
    (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)''')

conn.commit()

cur.close()
conn.close()


class Ui_Sales_System(object):
    def setupUi(self, Sales_System):
        Sales_System.setObjectName("Sales_System")
        Sales_System.resize(903, 600)
        self.centralwidget = QtWidgets.QWidget(parent=Sales_System)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_tab1 = QtWidgets.QPushButton(parent=self.centralwidget,clicked=lambda: self.change_tab1())
        self.btn_tab1.setGeometry(QtCore.QRect(0, 70, 181, 71))
        self.btn_tab1.setObjectName("btn_tab1")
        self.TabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.TabWidget.setGeometry(QtCore.QRect(180, 10, 611, 511))
        self.TabWidget.setObjectName("TabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.btn_save_product = QtWidgets.QPushButton(parent=self.tab1,clicked=lambda: self.save_product())
        self.btn_save_product.setGeometry(QtCore.QRect(70, 250, 75, 41))
        self.btn_save_product.setObjectName("btn_save_product")
        self.label_2 = QtWidgets.QLabel(parent=self.tab1)
        self.label_2.setGeometry(QtCore.QRect(70, 110, 49, 16))
        self.label_2.setObjectName("label_2")
        self.ln_name = QtWidgets.QLineEdit(parent=self.tab1)
        self.ln_name.setGeometry(QtCore.QRect(70, 60, 191, 31))
        self.ln_name.setObjectName("ln_name")
        self.ln_price = QtWidgets.QLineEdit(parent=self.tab1)
        self.ln_price.setGeometry(QtCore.QRect(70, 130, 191, 31))
        self.ln_price.setObjectName("ln_price")
        self.label = QtWidgets.QLabel(parent=self.tab1)
        self.label.setGeometry(QtCore.QRect(70, 40, 121, 16))
        self.label.setObjectName("label")
        self.btn_delete_product = QtWidgets.QPushButton(parent=self.tab1,clicked=lambda: self.delete_product())
        self.btn_delete_product.setGeometry(QtCore.QRect(120, 300, 75, 41))
        self.btn_delete_product.setObjectName("btn_delete_product")
        self.btn_update_product = QtWidgets.QPushButton(parent=self.tab1,clicked=lambda: self.update_product())
        self.btn_update_product.setGeometry(QtCore.QRect(180, 250, 75, 41))
        self.btn_update_product.setObjectName("btn_update_product")
        self.combo_supplier = QtWidgets.QComboBox(parent=self.tab1)
        self.combo_supplier.setGeometry(QtCore.QRect(70, 190, 69, 31))
        self.combo_supplier.setObjectName("combo_supplier")
        self.label_3 = QtWidgets.QLabel(parent=self.tab1)
        self.label_3.setGeometry(QtCore.QRect(70, 170, 81, 16))
        self.label_3.setObjectName("label_3")
        self.listWidget = QtWidgets.QListWidget(parent=self.tab1)
        self.listWidget.setGeometry(QtCore.QRect(310, 40, 281, 391))
        self.listWidget.setObjectName("listWidget")
        self.TabWidget.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.TabWidget.addTab(self.tab2, "")
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")
        self.TabWidget.addTab(self.tab3, "")
        self.tab4 = QtWidgets.QWidget()
        self.tab4.setObjectName("tab4")
        self.TabWidget.addTab(self.tab4, "")
        self.tab5 = QtWidgets.QWidget()
        self.tab5.setObjectName("tab5")
        self.TabWidget.addTab(self.tab5, "")
        self.btn_tab2 = QtWidgets.QPushButton(parent=self.centralwidget,clicked=lambda: self.change_tab2())
        self.btn_tab2.setGeometry(QtCore.QRect(0, 140, 181, 71))
        self.btn_tab2.setObjectName("btn_tab2")
        self.btn_tab3 = QtWidgets.QPushButton(parent=self.centralwidget,clicked=lambda: self.change_tab3())
        self.btn_tab3.setGeometry(QtCore.QRect(0, 210, 181, 71))
        self.btn_tab3.setObjectName("btn_tab3")
        self.btn_tab4 = QtWidgets.QPushButton(parent=self.centralwidget,clicked=lambda: self.change_tab4())
        self.btn_tab4.setGeometry(QtCore.QRect(0, 280, 181, 71))
        self.btn_tab4.setObjectName("btn_tab4")
        self.btn_tab5 = QtWidgets.QPushButton(parent=self.centralwidget,clicked=lambda: self.change_tab5())
        self.btn_tab5.setGeometry(QtCore.QRect(0, 350, 181, 71))
        self.btn_tab5.setObjectName("btn_tab5")
        Sales_System.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Sales_System)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 903, 22))
        self.menubar.setObjectName("menubar")
        Sales_System.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Sales_System)
        self.statusbar.setObjectName("statusbar")
        Sales_System.setStatusBar(self.statusbar)

        self.retranslateUi(Sales_System)
        self.TabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Sales_System)
        
        self.grab_all()
        self.listWidget.itemClicked.connect(self.grab_one)
        
        
    def grab_all(self):
        conn = sqlite3.connect('sales_system.db')
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM products")
        
        items = cur.fetchall()
        
        conn.commit()
        conn.close()
        
        for item in items:
        
            self.listWidget.addItem(str(item[0]))
             
    def grab_one(self):
        conn = sqlite3.connect('sales_system.db')
        cur = conn.cursor()
        
        name = self.listWidget.currentItem().text()
    
        cur.execute("SELECT name,price FROM products WHERE name = ?", (name,))
        item = cur.fetchone()
        conn.commit()
        
        if item:
            self.ln_name.setText(item[0])
            self.ln_price.setText(str(item[1]))
        
        conn.close()
        
        
    def save_product(self):
        conn = sqlite3.connect('sales_system.db')
        cur = conn.cursor()
        
        name = self.ln_name.text()
        price = self.ln_price.text()
        
        cur.execute("INSERT INTO products VALUES (?, ?)", (name, price))
        conn.commit()
        cur.close()
        
        self.ln_name.setText("")
        self.ln_price.setText("")
        
    def delete_product(self):
        
        conn = sqlite3.connect('sales_system.db')
        cur = conn.cursor()
        
        clicked = self.listWidget.currentRow()
        print(clicked)
        name = self.listWidget.takeItem(clicked).text()
        print(name)
        cur.execute("DELETE FROM products WHERE name = ?", (name,))
        conn.commit()
        
        cur.close()
        conn.close()
        
    def update_product(self):
        
        conn = sqlite3.connect('sales_system.db')
        cur = conn.cursor()
        
        name = self.ln_name.text()
        price = self.ln_price.text()
        
        cur.execute("UPDATE products SET price = ? WHERE name = ?", (price, name))
        conn.commit()
        
        cur.close()
        conn.close()
        
    def add_supplier(self):
        conn = sqlite3.connect('sales_system.db')
        cur = conn.cursor()
        
        name = self.ln_supplier.text()
        
        cur.execute("INSERT INTO supplier VALUES (?)", (name,))
        conn.commit()
        
        cur.close()
        conn.close()
    
    def change_tab1(self):
        # Cambia a la pestaña 2
        self.TabWidget.setCurrentWidget(self.tab1)
    def change_tab2(self):
        # Cambia a la pestaña 2
        self.TabWidget.setCurrentWidget(self.tab2)
        
    def change_tab3(self):
        # Cambia a la pestaña 2
        self.TabWidget.setCurrentWidget(self.tab3)
        
    def change_tab4(self):
        # Cambia a la pestaña 2
        self.TabWidget.setCurrentWidget(self.tab4)
        
    def change_tab5(self):
        # Cambia a la pestaña 2
        self.TabWidget.setCurrentWidget(self.tab5)
        
    

    def retranslateUi(self, Sales_System):
        _translate = QtCore.QCoreApplication.translate
        Sales_System.setWindowTitle(_translate("Sales_System", "Sales_System"))
        self.btn_tab1.setText(_translate("Sales_System", "PRODUCTS"))
        self.btn_save_product.setText(_translate("Sales_System", "SAVE"))
        self.label_2.setText(_translate("Sales_System", "PRICE"))
        self.label.setText(_translate("Sales_System", "NAME"))
        self.btn_delete_product.setText(_translate("Sales_System", "DELETE"))
        self.btn_update_product.setText(_translate("Sales_System", "UPDATE"))
        self.label_3.setText(_translate("Sales_System", "SUPPLIER"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab1), _translate("Sales_System", "Tab 1"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab2), _translate("Sales_System", "Tab 2"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab3), _translate("Sales_System", "tab 3"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab4), _translate("Sales_System", "tab 4"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab5), _translate("Sales_System", "tab 5"))
        self.btn_tab2.setText(_translate("Sales_System", "SUPPLIER"))
        self.btn_tab3.setText(_translate("Sales_System", "COSTUMER"))
        self.btn_tab4.setText(_translate("Sales_System", "SALES"))
        self.btn_tab5.setText(_translate("Sales_System", "USERS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Sales_System = QtWidgets.QMainWindow()
    ui = Ui_Sales_System()
    ui.setupUi(Sales_System)
    Sales_System.show()
    sys.exit(app.exec())
