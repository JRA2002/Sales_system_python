# Form implementation generated from reading ui file 'ventas5.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt6.QtWidgets import QMessageBox
import connection as conn

conn.Connection()

class Ui_Sales_System(object):

    def setupUi(self, Sales_System):
        Sales_System.setObjectName("Sales_System")
        Sales_System.resize(780, 450)
        self.centralwidget = QtWidgets.QWidget(parent=Sales_System)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_tab1 = QtWidgets.QPushButton(parent=self.centralwidget,clicked=lambda: self.change_tab1())
        self.btn_tab1.setGeometry(QtCore.QRect(0, 70, 181, 71))
        self.btn_tab1.setStyleSheet("background-color: rgb(180, 167, 255);")
        self.btn_tab1.setObjectName("btn_tab1")
        self.TabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.TabWidget.setGeometry(QtCore.QRect(180, 0, 611, 431))
        self.TabWidget.setObjectName("TabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.btn_save_product = QtWidgets.QPushButton(parent=self.tab1,clicked=lambda: self.save_product())
        self.btn_save_product.setGeometry(QtCore.QRect(70, 280, 75, 41))
        self.btn_save_product.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"font: 700 10pt \"Segoe UI\";")
        self.btn_save_product.setObjectName("btn_save_product")
        self.label_2 = QtWidgets.QLabel(parent=self.tab1)
        self.label_2.setGeometry(QtCore.QRect(70, 160, 49, 16))
        self.label_2.setObjectName("label_2")
        self.ln_name = QtWidgets.QLineEdit(parent=self.tab1)
        self.ln_name.setGeometry(QtCore.QRect(70, 120, 191, 31))
        self.ln_name.setObjectName("ln_name")
        self.ln_price = QtWidgets.QLineEdit(parent=self.tab1)
        self.ln_price.setGeometry(QtCore.QRect(70, 180, 191, 31))
        self.ln_price.setObjectName("ln_price")
        self.label = QtWidgets.QLabel(parent=self.tab1)
        self.label.setGeometry(QtCore.QRect(70, 100, 121, 16))
        self.label.setObjectName("label")
        self.btn_delete_product = QtWidgets.QPushButton(parent=self.tab1,clicked=lambda: self.delete_product())
        self.btn_delete_product.setGeometry(QtCore.QRect(120, 330, 75, 41))
        self.btn_delete_product.setObjectName("btn_delete_product")
        self.btn_update_product = QtWidgets.QPushButton(parent=self.tab1,clicked=lambda: self.update_product())
        self.btn_update_product.setGeometry(QtCore.QRect(180, 280, 75, 41))
        self.btn_update_product.setObjectName("btn_update_product")
        self.combo_supplier = QtWidgets.QComboBox(parent=self.tab1)
        self.combo_supplier.setGeometry(QtCore.QRect(70, 240, 69, 31))
        self.combo_supplier.setObjectName("combo_supplier")
        self.label_3 = QtWidgets.QLabel(parent=self.tab1)
        self.label_3.setGeometry(QtCore.QRect(70, 220, 81, 16))
        self.label_3.setObjectName("label_3")
        self.listWidget = QtWidgets.QListWidget(parent=self.tab1)
        self.listWidget.setGeometry(QtCore.QRect(280, 40, 281, 341))
        self.listWidget.setObjectName("listWidget")
        self.label_5 = QtWidgets.QLabel(parent=self.tab1)
        self.label_5.setGeometry(QtCore.QRect(70, 30, 91, 16))
        self.label_5.setObjectName("label_5")
        self.ln_pro_id = QtWidgets.QLineEdit(parent=self.tab1)
        self.ln_pro_id.setGeometry(QtCore.QRect(70, 50, 191, 31))
        self.ln_pro_id.setObjectName("ln_pro_id")
        self.TabWidget.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.label_4 = QtWidgets.QLabel(parent=self.tab2)
        self.label_4.setGeometry(QtCore.QRect(70, 90, 61, 16))
        self.label_4.setObjectName("label_4")
        self.ln_supplier = QtWidgets.QLineEdit(parent=self.tab2)
        self.ln_supplier.setGeometry(QtCore.QRect(70, 120, 191, 31))
        self.ln_supplier.setObjectName("ln_supplier")
        self.btn_add_supplier = QtWidgets.QPushButton(parent=self.tab2,clicked=lambda: self.add_supplier())
        self.btn_add_supplier.setGeometry(QtCore.QRect(70, 160, 75, 41))
        self.btn_add_supplier.setObjectName("btn_add_supplier")
        self.label_6 = QtWidgets.QLabel(parent=self.tab2)
        self.label_6.setGeometry(QtCore.QRect(70, 20, 81, 16))
        self.label_6.setObjectName("label_6")
        self.ln_supp_id = QtWidgets.QLineEdit(parent=self.tab2)
        self.ln_supp_id.setGeometry(QtCore.QRect(70, 50, 191, 31))
        self.ln_supp_id.setObjectName("ln_supp_id")
        self.listWidget_supp = QtWidgets.QListWidget(parent=self.tab2)
        self.listWidget_supp.setGeometry(QtCore.QRect(285, 20, 281, 271))
        self.listWidget_supp.setObjectName("listWidget_supp")
        self.btn_supp_delete = QtWidgets.QPushButton(parent=self.tab2,clicked=lambda: self.delete_supplier())
        self.btn_supp_delete.setGeometry(QtCore.QRect(130, 220, 75, 41))
        self.btn_supp_delete.setObjectName("btn_supp_delete")
        self.btn_supp_update = QtWidgets.QPushButton(parent=self.tab2,clicked=lambda: self.update_supplier())
        self.btn_supp_update.setGeometry(QtCore.QRect(180, 160, 75, 41))
        self.btn_supp_update.setObjectName("btn_supp_update")
        self.TabWidget.addTab(self.tab2, "")
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")
        self.label_10 = QtWidgets.QLabel(parent=self.tab3)
        self.label_10.setGeometry(QtCore.QRect(40, 110, 49, 16))
        self.label_10.setObjectName("label_10")
        self.ln_name_cus = QtWidgets.QLineEdit(parent=self.tab3)
        self.ln_name_cus.setGeometry(QtCore.QRect(40, 130, 191, 31))
        self.ln_name_cus.setObjectName("ln_name_cus")
        self.ln_last_cus = QtWidgets.QLineEdit(parent=self.tab3)
        self.ln_last_cus.setGeometry(QtCore.QRect(40, 200, 191, 31))
        self.ln_last_cus.setObjectName("ln_last_cus")
        self.label_11 = QtWidgets.QLabel(parent=self.tab3)
        self.label_11.setGeometry(QtCore.QRect(40, 180, 81, 16))
        self.label_11.setObjectName("label_11")
        self.ln_doc = QtWidgets.QLineEdit(parent=self.tab3)
        self.ln_doc.setGeometry(QtCore.QRect(40, 70, 191, 31))
        self.ln_doc.setObjectName("ln_doc")
        self.label_12 = QtWidgets.QLabel(parent=self.tab3)
        self.label_12.setGeometry(QtCore.QRect(40, 40, 49, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(parent=self.tab3)
        self.label_13.setGeometry(QtCore.QRect(40, 240, 49, 16))
        self.label_13.setObjectName("label_13")
        self.ln_phone_cus = QtWidgets.QLineEdit(parent=self.tab3)
        self.ln_phone_cus.setGeometry(QtCore.QRect(40, 260, 191, 31))
        self.ln_phone_cus.setText("")
        self.ln_phone_cus.setObjectName("ln_phone_cus")
        self.btn_reg_cus = QtWidgets.QPushButton(parent=self.tab3,clicked=lambda: self.add_customer())
        self.btn_reg_cus.setGeometry(QtCore.QRect(40, 310, 75, 41))
        self.btn_reg_cus.setObjectName("btn_reg_cus")
        self.listWidget_cust = QtWidgets.QListWidget(parent=self.tab3)
        self.listWidget_cust.setGeometry(QtCore.QRect(290, 61, 256, 221))
        self.listWidget_cust.setObjectName("listWidget_cust")
        self.btn_upd_cus = QtWidgets.QPushButton(parent=self.tab3,clicked=lambda: self.update_customer())
        self.btn_upd_cus.setGeometry(QtCore.QRect(160, 310, 75, 41))
        self.btn_upd_cus.setObjectName("btn_upd_cus")
        self.btn_del_cus = QtWidgets.QPushButton(parent=self.tab3,clicked=lambda: self.delete_customer())
        self.btn_del_cus.setGeometry(QtCore.QRect(280, 310, 75, 41))
        self.btn_del_cus.setObjectName("btn_del_cus")
        self.TabWidget.addTab(self.tab3, "")
        self.tab4 = QtWidgets.QWidget()
        self.tab4.setObjectName("tab4")
        self.label_7 = QtWidgets.QLabel(parent=self.tab4)
        self.label_7.setGeometry(QtCore.QRect(40, 30, 91, 16))
        self.label_7.setObjectName("label_7")
        self.ln_search = QtWidgets.QLineEdit(parent=self.tab4)
        self.ln_search.setGeometry(QtCore.QRect(40, 50, 113, 31))
        self.ln_search.setObjectName("ln_search")
        self.btn_search = QtWidgets.QPushButton(parent=self.tab4,clicked=lambda: self.search_product())
        self.btn_search.setGeometry(QtCore.QRect(170, 50, 75, 31))
        self.btn_search.setObjectName("btn_search")
        self.tableWidget_sale = QtWidgets.QTableWidget(parent=self.tab4)
        self.tableWidget_sale.setGeometry(QtCore.QRect(40, 91, 531, 241))
        self.tableWidget_sale.setObjectName("tableWidget_sale")
        self.tableWidget_sale.setColumnCount(0)
        self.tableWidget_sale.setRowCount(0)
        self.btn_sale = QtWidgets.QPushButton(parent=self.tab4,clicked=lambda: self.purchase())
        self.btn_sale.setGeometry(QtCore.QRect(480, 350, 75, 31))
        self.btn_sale.setObjectName("btn_sale")
        self.label_8 = QtWidgets.QLabel(parent=self.tab4)
        self.label_8.setGeometry(QtCore.QRect(290, 30, 71, 16))
        self.label_8.setObjectName("label_8")
        self.btn_qty = QtWidgets.QLineEdit(parent=self.tab4)
        self.btn_qty.setGeometry(QtCore.QRect(290, 50, 71, 31))
        self.btn_qty.setObjectName("btn_qty")
        self.btn_cancel = QtWidgets.QPushButton(parent=self.tab4,clicked=lambda: self.cancel_sale())
        self.btn_cancel.setGeometry(QtCore.QRect(310, 350, 75, 31))
        self.btn_cancel.setObjectName("btn_cancel")
        self.label_9 = QtWidgets.QLabel(parent=self.tab4)
        self.label_9.setGeometry(QtCore.QRect(480, 30, 49, 16))
        self.label_9.setObjectName("label_9")
        self.btn_total = QtWidgets.QLineEdit(parent=self.tab4)
        self.btn_total.setGeometry(QtCore.QRect(480, 50, 81, 31))
        self.btn_total.setObjectName("btn_total")
        self.TabWidget.addTab(self.tab4, "")
        self.tab5 = QtWidgets.QWidget()
        self.tab5.setObjectName("tab5")
        self.tableWidget_report = QtWidgets.QTableWidget(parent=self.tab5)
        self.tableWidget_report.setGeometry(QtCore.QRect(25, 101, 541, 251))
        self.tableWidget_report.setObjectName("tableWidget_report")
        self.tableWidget_report.setColumnCount(0)
        self.tableWidget_report.setRowCount(0)
        self.date_from = QtWidgets.QDateEdit(parent=self.tab5)
        self.date_from.setGeometry(QtCore.QRect(30, 40, 110, 22))
        self.date_from.setObjectName("date_from")
        self.date_to = QtWidgets.QDateEdit(parent=self.tab5)
        self.date_to.setGeometry(QtCore.QRect(150, 40, 110, 22))
        self.date_to.setObjectName("date_to")
        self.label_14 = QtWidgets.QLabel(parent=self.tab5)
        self.label_14.setGeometry(QtCore.QRect(30, 20, 49, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(parent=self.tab5)
        self.label_15.setGeometry(QtCore.QRect(150, 20, 49, 16))
        self.label_15.setObjectName("label_15")
        self.btn_report = QtWidgets.QPushButton(parent=self.tab5)
        self.btn_report.setGeometry(QtCore.QRect(480, 30, 75, 31))
        self.btn_report.setObjectName("btn_report")
        self.TabWidget.addTab(self.tab5, "")
        self.btn_tab2 = QtWidgets.QPushButton(parent=self.centralwidget,clicked=lambda: self.change_tab2())
        self.btn_tab2.setGeometry(QtCore.QRect(0, 140, 181, 71))
        self.btn_tab2.setStyleSheet("background-color: rgb(135, 255, 211);")
        self.btn_tab2.setObjectName("btn_tab2")
        self.btn_tab3 = QtWidgets.QPushButton(parent=self.centralwidget,clicked=lambda: self.change_tab3())
        self.btn_tab3.setGeometry(QtCore.QRect(0, 210, 181, 71))
        self.btn_tab3.setStyleSheet("background-color: rgb(155, 182, 255);")
        self.btn_tab3.setObjectName("btn_tab3")
        self.btn_tab4 = QtWidgets.QPushButton(parent=self.centralwidget,clicked=lambda: self.change_tab4())
        self.btn_tab4.setGeometry(QtCore.QRect(0, 280, 181, 71))
        self.btn_tab4.setStyleSheet("background-color: rgb(236, 255, 206);")
        self.btn_tab4.setObjectName("btn_tab4")
        self.btn_tab5 = QtWidgets.QPushButton(parent=self.centralwidget,clicked=lambda: self.change_tab5())
        self.btn_tab5.setGeometry(QtCore.QRect(0, 350, 181, 71))
        self.btn_tab5.setStyleSheet("background-color: rgb(255, 125, 225);")
        self.btn_tab5.setObjectName("btn_tab5")
        self.TabWidget.raise_()
        self.btn_tab2.raise_()
        self.btn_tab3.raise_()
        self.btn_tab4.raise_()
        self.btn_tab5.raise_()
        self.btn_tab1.raise_()
        Sales_System.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Sales_System)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 780, 22))
        self.menubar.setObjectName("menubar")
        Sales_System.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Sales_System)
        self.statusbar.setObjectName("statusbar")
        Sales_System.setStatusBar(self.statusbar)

        self.retranslateUi(Sales_System)
        self.TabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Sales_System)
        
        self.grab_all()
        self.grab_supplier()
        self.grab_customer()
        self.listWidget.itemClicked.connect(self.grab_one)
        self.listWidget_supp.itemClicked.connect(self.grab_one_supplier)
        self.listWidget_cust.itemClicked.connect(self.grab_one_customer)
        self.get_supplier()
        self.report_sales()
        self.ln_pro_id.textChanged.connect(self.validate_id)
        self.ln_price.textChanged.connect(self.validate_price)
        self.ln_name.textChanged.connect(self.validate_string)
        #self.ln_supp_id.textChanged.connect(self.validate_digit)
        self.ln_supplier.textChanged.connect(self.validate_string)
        #self.ln_doc.textChanged.connect(self.validate_digit)
        self.ln_name_cus.textChanged.connect(self.validate_string)
        self.ln_last_cus.textChanged.connect(self.validate_string)
        #self.ln_phone_cus.textChanged.connect(self.validate_digit)
        #self.btn_qty.textChanged.connect(self.validate_digit)
        
    def grab_all(self):
        conn = sqlite3.connect('sales_system.db')
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM products")
        
        items = cur.fetchall()
        
        conn.commit()
        conn.close()
        
        for item in items:
        
            self.listWidget.addItem(str(item[1]))
             
    def validate_price(self):
        
        price = self.ln_price.text()

        if price.isdigit() or not price:
            print(price)
            self.ln_price.setStyleSheet("background-color: white;")
            return True
        else:
            self.ln_price.setStyleSheet("background-color: red;")
            return False
    def validate_id(self):
        
        _id = self.ln_pro_id.text()
        
        if _id.isdigit() or not _id:
            self.ln_pro_id.setStyleSheet("background-color: white;")
            return True
        else:
            self.ln_pro_id.setStyleSheet("background-color: red;")
            return False
        
        
    def validate_string(self):
        name = self.ln_name.text()
        if name.isalpha() or not name:
            self.ln_name.setStyleSheet("background-color: white;")
            return True
        else:
            self.ln_name.setStyleSheet("background-color: red;")
            return False
        
    def grab_one(self):
        conn = sqlite3.connect('sales_system.db')
        cur = conn.cursor()
        
        name = self.listWidget.currentItem().text()
    
        cur.execute("SELECT _id,name,price,supplier_name FROM products WHERE name = ?", (name,))
        item = cur.fetchone()
        conn.commit()
        
        if item:
            self.ln_pro_id.setText(str(item[0]))
            self.ln_name.setText(item[1])
            self.ln_price.setText(str(item[2]))
            self.combo_supplier.setCurrentText(item[3])
        
        conn.close()
        
        
    def save_product(self):
        conn = sqlite3.connect('sales_system.db')
        cur = conn.cursor()
        
        _id = int(self.ln_pro_id.text())
        name = self.ln_name.text()
        price = int(self.ln_price.text())
        supplier_name = self.combo_supplier.currentText()      

        
        cur.execute("INSERT INTO products VALUES (?, ?,?,?)", (_id,name, price,supplier_name))
    
        conn.commit()
        cur.close()
        
        self.ln_name.setText("")
        self.ln_price.setText("")
        self.ln_pro_id.setText("")
        
        self.messageBox()
        
    def delete_product(self):
        
        conn = sqlite3.connect('sales_system.db')
        cur = conn.cursor()
        
        clicked = self.listWidget.currentRow()
        name = self.listWidget.takeItem(clicked).text()

        cur.execute("DELETE FROM products WHERE name = ?", (name,))
        conn.commit()
        
        self.ln_pro_id.setText("")
        self.ln_name.setText("")
        self.ln_price.setText("")
        
        cur.close()
        conn.close()
        
    def update_product(self):
        
        conn = sqlite3.connect('sales_system.db')
        cur = conn.cursor()
        
        name = self.ln_name.text()
        price = self.ln_price.text()
        supplier_name = self.combo_supplier.currentText()
        
        cur.execute("UPDATE products SET price=?, supplier_name=? WHERE name = ?", (price,supplier_name,name))
        conn.commit()
        
        cur.close()
        conn.close()
        
        self.ln_pro_id.setText("")
        self.ln_name.setText("")
        self.ln_price.setText("")
        
    def add_supplier(self):
        conn = sqlite3.connect('sales_system.db')
        cur = conn.cursor()
        
        name = self.ln_supplier.text()
        _id = self.ln_supp_id.text()
        
        cur.execute("INSERT INTO supplier VALUES (?,?)", (_id,name,))
        conn.commit()
    
        cur.close()
        conn.close()
        
        self.ln_supplier.setText("")
        self.ln_supp_id.setText("")
        self.messageBox()
        
    def get_supplier(self):
        conn = sqlite3.connect('sales_system.db')
        cur = conn.cursor()
        
        cur.execute("SELECT name FROM supplier")
        items = cur.fetchall()
        conn.commit()
        conn.close()
        
        for item in items:
            self.combo_supplier.addItem(item[0])
            
    def grab_supplier(self):
        conn = sqlite3.connect('sales_system.db')
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM supplier")
        
        supplier = cur.fetchall()
        
        conn.commit()
        conn.close()
        
        for item in supplier:
        
            self.listWidget_supp.addItem(str(item[1]))
            
    def grab_one_supplier(self):
        conn = sqlite3.connect('sales_system.db')
        cur = conn.cursor()
        
        name = self.listWidget_supp.currentItem().text()
    
        cur.execute("SELECT _id,name FROM supplier WHERE name = ?", (name,))
        item = cur.fetchone()
        conn.commit()
        
        if item:
            self.ln_supp_id.setText(str(item[0]))
            self.ln_supplier.setText(item[1])
        
        conn.close()
        
    def delete_supplier(self):
        
        conn = sqlite3.connect('sales_system.db')
        cur = conn.cursor()
        
        clicked = self.listWidget_supp.currentRow()
        name = self.listWidget_supp.takeItem(clicked).text()

        cur.execute("DELETE FROM supplier WHERE name = ?", (name,))
        conn.commit()
        
        self.ln_supp_id.setText("")
        self.ln_supplier.setText("")
        
        cur.close()
        conn.close()
    
    def update_supplier(self):
        
        conn = sqlite3.connect('sales_system.db')
        cur = conn.cursor()
        
        name = self.ln_supplier.text()
        _id = int(self.ln_supp_id.text())
        
        cur.execute("UPDATE supplier SET name=? WHERE _id = ?", (name,_id))
        conn.commit()
        
        cur.close()
        conn.close()
        
        self.ln_supp_id.setText("")
        self.ln_supplier.setText("")
        
    def add_customer(self):
        conn = sqlite3.connect('sales_system.db')
        cur = conn.cursor()
        
        _id = self.ln_doc.text()
        name = self.ln_name_cus.text()
        last_name = self.ln_last_cus.text()
        phone = self.ln_phone_cus.text()
        
        cur.execute("INSERT INTO customers VALUES (?, ?,?,?)", (_id, name, last_name, phone))
        conn.commit()
        cur.close()
        
        self.ln_doc.setText("")
        self.ln_name_cus.setText("")
        self.ln_last_cus.setText("")
        self.ln_phone_cus.setText("")
        
        conn.close()
        self.messageBox()
        
    def update_customer(self):
        
        conn = sqlite3.connect('sales_system.db')
        cur = conn.cursor()
        
        _id = int(self.ln_doc.text())
        name = self.ln_name_cus.text()
        last_name = self.ln_last_cus.text()
        phone = int(self.ln_phone_cus.text())
        
        
        cur.execute("UPDATE customers SET name=?, last_name=?, phone=? WHERE _id = ?", (name,last_name,phone,_id))
        conn.commit()
        
        cur.close()
        conn.close()
        
        self.ln_doc.setText("")
        self.ln_name_cus.setText("")
        self.ln_last_cus.setText("")
        self.ln_phone_cus.setText("")
        
    def grab_customer(self):
        conn = sqlite3.connect('sales_system.db')
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM customers")
        
        customers = cur.fetchall()
        
        conn.commit()
        conn.close()
        
        for item in customers:
        
            self.listWidget_cust.addItem(str(item[1]))
            
    def grab_one_customer(self):
        conn = sqlite3.connect('sales_system.db')
        cur = conn.cursor()
    
        name = self.listWidget_cust.currentItem().text()
    
        cur.execute("SELECT _id,name, last_name, phone FROM customers WHERE name = ?", (name,))
        item = cur.fetchone()
        conn.commit()
        
        if item:
            self.ln_doc.setText(str(item[0]))
            self.ln_name_cus.setText(item[1])
            self.ln_last_cus.setText(item[2])
            self.ln_phone_cus.setText(str(item[3]))
            
        conn.close()
        
    def delete_customer(self):
        
        conn = sqlite3.connect('sales_system.db')
        cur = conn.cursor()
        
        clicked = self.listWidget_cust.currentRow()
        name = self.listWidget_cust.takeItem(clicked).text()

        cur.execute("DELETE FROM customers WHERE name = ?", (name,))
        conn.commit()
        
        self.ln_doc.setText("")
        self.ln_name_cus.setText("")
        self.ln_last_cus.setText("")
        self.ln_phone_cus.setText("")
        
        cur.close()
        conn.close()
        
    def search_product(self):
        conn = sqlite3.connect('sales_system.db')
        cur = conn.cursor()
        
        name = self.ln_search.text()
        quantity = int(self.btn_qty.text())
        
        cur.execute("SELECT * FROM products WHERE name = ?", (name,))
        
        product = cur.fetchone()

        conn.commit()
        
        self.tableWidget_sale.setColumnCount(5)
        self.tableWidget_sale.setHorizontalHeaderLabels(['PRODUCT_ID','NAME', 'PRICE', 'SUPPLIER','SUB_TOTAL'])
        print(product)
        if product:
            
            sub_total = product[2] * quantity
            
            self.tableWidget_sale.insertRow(0)
            self.tableWidget_sale.setItem(0,0,QtWidgets.QTableWidgetItem(str(product[0])))
            self.tableWidget_sale.setItem(0,1,QtWidgets.QTableWidgetItem(str(product[1])))
            self.tableWidget_sale.setItem(0,2,QtWidgets.QTableWidgetItem(str(product[2])))
            self.tableWidget_sale.setItem(0,3,QtWidgets.QTableWidgetItem(str(product[3])))
            self.tableWidget_sale.setItem(0,4,QtWidgets.QTableWidgetItem(str(sub_total)))
        
        self.ln_search.setText("")   
        self.btn_qty.setText("1")
        total = self.total_sale()
        self.btn_total.setText(str(total))
        
        conn.close()
        
    def cancel_sale(self):
        self.tableWidget_sale.setRowCount(0)
        self.btn_total.setText("0")
        self.ln_search.setText("")
        
    def purchase(self):
        conn = sqlite3.connect('sales_system.db')
        cur = conn.cursor()
        rows = self.tableWidget_sale.rowCount()
        for row in range(rows):
            cur.execute("INSERT INTO sales VALUES (NULL,?,?)", (int(self.tableWidget_sale.item(row,0).text()),self.btn_total.text(),))
            conn.commit()
        
        cur.close()
        conn.close()
        self.tableWidget_sale.clearContents()
        self.messageBox_venta()
        
    def report_sales(self):
        conn = sqlite3.connect('sales_system.db')
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM sales")
        
        sales = cur.fetchall()
        print(sales)
        conn.commit()
        conn.close()
        
        self.tableWidget_report.setColumnCount(2)
        self.tableWidget_report.setHorizontalHeaderLabels(['PRODUCT_ID', 'TOTAL'])
        
        if sales:
            for i,item in enumerate(sales):
                self.tableWidget_report.insertRow(0)
                for j in range(len(item)):
                    self.tableWidget_report.setItem(0,j,QtWidgets.QTableWidgetItem(str(item[j])))
                
    def messageBox(self):
            msg = QMessageBox()
            msg.setWindowTitle("Message")
            msg.setText("Saved to Database")
            msg.setIcon(QMessageBox.Icon.Information)
            x = msg.exec()  
            
    def messageBox_venta(self):
            msg = QMessageBox()
            msg.setWindowTitle("Message")
            msg.setText("Sale Done! ")
            msg.setIcon(QMessageBox.Icon.Information)
            x = msg.exec()
                       
        
    def total_sale(self):
        total = 0
        for row in range(self.tableWidget_sale.rowCount()):
            total += int(self.tableWidget_sale.item(row,4).text())
        return total
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
        self.label_5.setText(_translate("Sales_System", "PRODUCT ID"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab1), _translate("Sales_System", "Tab 1"))
        self.label_4.setText(_translate("Sales_System", "NAME"))
        self.btn_add_supplier.setText(_translate("Sales_System", "ADD"))
        self.label_6.setText(_translate("Sales_System", "SUPPLIER ID"))
        self.btn_supp_delete.setText(_translate("Sales_System", "DELETE"))
        self.btn_supp_update.setText(_translate("Sales_System", "UPDATE"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab2), _translate("Sales_System", "Tab 2"))
        self.label_10.setText(_translate("Sales_System", "NAME"))
        self.label_11.setText(_translate("Sales_System", "LAST_NAME"))
        self.label_12.setText(_translate("Sales_System", "DNI/RUT"))
        self.label_13.setText(_translate("Sales_System", "PHONE"))
        self.btn_reg_cus.setText(_translate("Sales_System", "REGISTER"))
        self.btn_upd_cus.setText(_translate("Sales_System", "UPDATE"))
        self.btn_del_cus.setText(_translate("Sales_System", "DELETE"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab3), _translate("Sales_System", "tab 3"))
        self.label_7.setText(_translate("Sales_System", "ID or NAME"))
        self.btn_search.setText(_translate("Sales_System", "SEARCH"))
        self.btn_sale.setText(_translate("Sales_System", "SALE"))
        self.label_8.setText(_translate("Sales_System", "QUANTITY"))
        self.btn_cancel.setText(_translate("Sales_System", "CANCEL"))
        self.label_9.setText(_translate("Sales_System", "TOTAL"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab4), _translate("Sales_System", "tab 4"))
        self.label_14.setText(_translate("Sales_System", "FROM"))
        self.label_15.setText(_translate("Sales_System", "TO"))
        self.btn_report.setText(_translate("Sales_System", "REPORT"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab5), _translate("Sales_System", "tab 5"))
        self.btn_tab2.setText(_translate("Sales_System", "SUPPLIER"))
        self.btn_tab3.setText(_translate("Sales_System", "CUSTOMER"))
        self.btn_tab4.setText(_translate("Sales_System", "SALES"))
        self.btn_tab5.setText(_translate("Sales_System", "REPORTS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Sales_System = QtWidgets.QMainWindow()
    ui = Ui_Sales_System()
    ui.setupUi(Sales_System)
    Sales_System.show()
    sys.exit(app.exec())
