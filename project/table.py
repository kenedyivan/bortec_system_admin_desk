# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector


class Ui_MainWindow(object):
    def load_data(self):
        conn = mysql.connector.connect(user='root', password='root', host='localhost', database='bortec_inv_system_db')
        cursor = conn.cursor()
        cursor.execute('select inventory_stocks.id,items.product_name,inventory_stocks.received,inventory_stocks.sales,'
                       'inventory_stocks.stocks, inventory_stocks.total_expenditure_cost,'
                       'inventory_stocks.total_sales_cost, inventory_stocks.created_at,'
                       'inventory_stocks.updated_at from inventory_stocks '
                       'left join items on items.id = inventory_stocks.item_id')
        data_list = cursor.fetchall()
        print(data_list)
        rows = 1
        for row_number, d in enumerate(data_list):
            self.tableWidget.setRowCount(rows)
            self.tableWidget.insertRow(rows)
            for column_number, data in enumerate(d):
                self.tableWidget.setItem(rows, column_number, QtWidgets.QTableWidgetItem(str(data)))
                print(data)
            rows = rows + 1
        conn.close()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(965, 598)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setObjectName("tableWidget")

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 8, item)

        self.horizontalLayout_2.addWidget(self.tableWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 965, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "Stock ID"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "Product Name"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "Received"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "Sales"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("MainWindow", "Stocks"))
        item = self.tableWidget.item(0, 5)
        item.setText(_translate("MainWindow", "Expenditure Cost"))
        item = self.tableWidget.item(0, 6)
        item.setText(_translate("MainWindow", "Sales Cost"))
        item = self.tableWidget.item(0, 7)
        item.setText(_translate("MainWindow", "Created At"))
        item = self.tableWidget.item(0, 8)
        item.setText(_translate("MainWindow", "Updated At"))

        # Loads the inventory data
        self.load_data()

        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.menuFile.setTitle(_translate("MainWindow", "File"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
