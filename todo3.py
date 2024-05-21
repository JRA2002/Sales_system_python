# Form implementation generated from reading ui file 'todo3.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(628, 546)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_add = QtWidgets.QPushButton(parent=self.centralwidget,)
        self.btn_add.setGeometry(QtCore.QRect(20, 100, 161, 91))
        self.btn_add.setObjectName("btn_add")
        self.btn_delete = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(20, 190, 161, 91))
        self.btn_delete.setObjectName("btn_delete")
        self.btn_clear_all = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_clear_all.setGeometry(QtCore.QRect(20, 280, 161, 91))
        self.btn_clear_all.setObjectName("btn_clear_all")
        self.listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(230, 380, 241, 121))
        self.listWidget.setObjectName("listWidget")
        self.btn_save = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(20, 370, 161, 91))
        self.btn_save.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.btn_save.setObjectName("btn_save")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(180, 30, 431, 291))
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.tabWidget.addTab(self.tab2, "")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.tabWidget.addTab(self.tab1, "")
        self.btn_add.clicked.connect(self.cambiar_a_pestaña)  # Reemplaza 'tabNombre' con el nombre de la pestaña
        self.line_add = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.line_add.setGeometry(QtCore.QRect(230, 310, 301, 31))
        self.line_add.setObjectName("line_add")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 628, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.grab_all()
        
    def cambiar_a_pestaña(self):
        self.tabWidget.setCurrentWidget(self.tab1)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_add.setText(_translate("MainWindow", "ADD ITEM TO LIST"))
        self.btn_delete.setText(_translate("MainWindow", "DELETE ITEM"))
        self.btn_clear_all.setText(_translate("MainWindow", "CLEAR LIST"))
        self.btn_save.setText(_translate("MainWindow", "SAVE DATABASE"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "Tab 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Tab 1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
