# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector


class Ui_MainWindow(object):
    def load_inventory_data(self):
        conn = mysql.connector.connect(user='root', password='root', host='localhost', database='bortec_inv_system_db')
        cursor = conn.cursor()
        cursor.execute('select inventory_stocks.id,items.codes,items.product_name,'
                       'inventory_stocks.received,inventory_stocks.sales,'
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
            rows = rows + 1
        conn.close()

    def load_items_data(self):
        conn = mysql.connector.connect(user='root', password='root', host='localhost', database='bortec_inv_system_db')
        cursor = conn.cursor()
        cursor.execute('select id, codes, product_name, units, unit_price, remarks, created_at, updated_at from items')
        data_list = cursor.fetchall()
        print(data_list)
        rows = 1
        for row_number, d in enumerate(data_list):
            self.tableWidget.setRowCount(rows)
            self.tableWidget.insertRow(rows)
            for column_number, data in enumerate(d):
                self.tableWidget.setItem(rows, column_number, QtWidgets.QTableWidgetItem(str(data)))
            rows = rows + 1
        conn.close()

    def load_sales_data(self):
        conn = mysql.connector.connect(user='root', password='root', host='localhost', database='bortec_inv_system_db')
        cursor = conn.cursor()
        cursor.execute('select sales.id, items.product_name, CONCAT(operators.first_name,\' \', '
                       'operators.last_name) AS '
                       'name, sales.quantity, sales.total_price, sales.created_at, sales.updated_at '
                       'from sales left join items on items.id = sales.item_id left join operators '
                       'on operators.id = sales.operator_id order by created_at desc')
        data_list = cursor.fetchall()
        print(data_list)
        rows = 1
        for row_number, d in enumerate(data_list):
            self.tableWidget.setRowCount(rows)
            self.tableWidget.insertRow(rows)
            for column_number, data in enumerate(d):
                self.tableWidget.setItem(rows, column_number, QtWidgets.QTableWidgetItem(str(data)))
            rows = rows + 1
        conn.close()

    def load_received_data(self):
        conn = mysql.connector.connect(user='root', password='root', host='localhost', database='bortec_inv_system_db')
        cursor = conn.cursor()
        cursor.execute('select received_products.id, items.product_name, CONCAT(operators.first_name,\' \', '
                       'operators.last_name) AS '
                       'name, received_products.quantity, received_products.total_price, '
                       'received_products.created_at, received_products.updated_at '
                       'from received_products left join items on '
                       'items.id = received_products.item_id left join operators '
                       'on operators.id = received_products.operator_id order by created_at desc')
        data_list = cursor.fetchall()
        print(data_list)
        rows = 1
        for row_number, d in enumerate(data_list):
            self.tableWidget.setRowCount(rows)
            self.tableWidget.insertRow(rows)
            for column_number, data in enumerate(d):
                self.tableWidget.setItem(rows, column_number, QtWidgets.QTableWidgetItem(str(data)))
            rows = rows + 1
        conn.close()

    def load_operators_data(self):
        conn = mysql.connector.connect(user='root', password='root', host='localhost', database='bortec_inv_system_db')
        cursor = conn.cursor()
        cursor.execute('select id, first_name, last_name, auth_id, dob, created_at, updated_at from operators')
        data_list = cursor.fetchall()
        print(data_list)
        rows = 1
        for row_number, d in enumerate(data_list):
            self.tableWidget.setRowCount(rows)
            self.tableWidget.insertRow(rows)
            for column_number, data in enumerate(d):
                self.tableWidget.setItem(rows, column_number, QtWidgets.QTableWidgetItem(str(data)))
            rows = rows + 1
        conn.close()

    def inventory_table(self):
        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(10)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 9, item)
        _translate = QtCore.QCoreApplication.translate
        # MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "Stock ID"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "Codes"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "Product Name"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "Received"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("MainWindow", "Sales"))
        item = self.tableWidget.item(0, 5)
        item.setText(_translate("MainWindow", "Stocks"))
        item = self.tableWidget.item(0, 6)
        item.setText(_translate("MainWindow", "Expenditure Cost"))
        item = self.tableWidget.item(0, 7)
        item.setText(_translate("MainWindow", "Sales Cost"))
        item = self.tableWidget.item(0, 8)
        item.setText(_translate("MainWindow", "Created At"))
        item = self.tableWidget.item(0, 9)
        item.setText(_translate("MainWindow", "Updated At"))

        # Loads the inventory data
        self.load_inventory_data()

        self.tableWidget.setSortingEnabled(__sortingEnabled)
        return self.tableWidget

    def items_table(self):
        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(8)
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
        _translate = QtCore.QCoreApplication.translate
        # MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "Stock ID"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "Codes"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "Product name"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "Units"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("MainWindow", "Unit price"))
        item = self.tableWidget.item(0, 5)
        item.setText(_translate("MainWindow", "Remarks"))
        item = self.tableWidget.item(0, 6)
        item.setText(_translate("MainWindow", "Created At"))
        item = self.tableWidget.item(0, 7)
        item.setText(_translate("MainWindow", "Updated At"))

        # Loads the inventory data
        self.load_items_data()

        self.tableWidget.setSortingEnabled(__sortingEnabled)
        return self.tableWidget

    def sales_table(self):
        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(7)
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
        _translate = QtCore.QCoreApplication.translate
        # MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "Sale ID"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "Product"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "Operator"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("MainWindow", "Total price"))
        item = self.tableWidget.item(0, 5)
        item.setText(_translate("MainWindow", "Created At"))
        item = self.tableWidget.item(0, 6)
        item.setText(_translate("MainWindow", "Updated At"))

        # Loads the inventory data
        self.load_sales_data()

        self.tableWidget.setSortingEnabled(__sortingEnabled)
        return self.tableWidget

    def received_table(self):
        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(7)
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
        _translate = QtCore.QCoreApplication.translate
        # MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "Received ID"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "Product"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "Operator"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("MainWindow", "Total price"))
        item = self.tableWidget.item(0, 5)
        item.setText(_translate("MainWindow", "Created At"))
        item = self.tableWidget.item(0, 6)
        item.setText(_translate("MainWindow", "Updated At"))

        # Loads the inventory data
        self.load_received_data()

        self.tableWidget.setSortingEnabled(__sortingEnabled)
        return self.tableWidget

    def operators_table(self):
        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(7)
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
        _translate = QtCore.QCoreApplication.translate
        # MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "Operator ID"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "First name"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "Last name"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "Auth ID"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("MainWindow", "Date of birth"))
        item = self.tableWidget.item(0, 5)
        item.setText(_translate("MainWindow", "Created At"))
        item = self.tableWidget.item(0, 6)
        item.setText(_translate("MainWindow", "Updated At"))

        # Loads the inventory data
        self.load_operators_data()

        self.tableWidget.setSortingEnabled(__sortingEnabled)
        return self.tableWidget

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QFrame.SidebarFrame {\n"
                                         "border-top-left-radius: 10px;\n"
                                         "border-top-right-radius: 10px;\n"
                                         "border: 1px solid black;\n"
                                         "background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                         "stop: 0 #56a, stop: 0.1 #016);\n"
                                         "}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame.setStyleSheet("background:rgb(178, 208, 255)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setProperty("class", "")
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setStyleSheet("border-color:green;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame_4)
        self.pushButton.setStyleSheet("color:red;\n"
                                      "background-color:blue;")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_operators = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_operators.setObjectName("pushButton_operators")
        self.verticalLayout.addWidget(self.pushButton_operators)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.verticalLayout_4.addWidget(self.frame_3)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_4.addWidget(self.frame_5)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("background-color:rgb(207, 255, 180)")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_items_click()
        # self.tableWidget = QtWidgets.QTableWidget(self.frame_2)
        # self.tableWidget.setRowCount(9)
        # self.tableWidget.setColumnCount(10)
        # self.tableWidget.setObjectName("tableWidget")
        # self.verticalLayout_3.addWidget(self.tableWidget)

        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.horizontalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.pushButton.clicked.connect(self.btn_items_click)
        self.pushButton_2.clicked.connect(self.btn_sales_click)
        self.pushButton_3.clicked.connect(self.btn_received_click)
        self.pushButton_4.clicked.connect(self.btn_inventory_click)
        self.pushButton_operators.clicked.connect(self.btn_operators_click)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    '''
    Side menu button events handlers
    '''

    def btn_inventory_click(self):
        for i in reversed(range(self.verticalLayout_3.count())):
            self.verticalLayout_3.itemAt(i).widget().setParent(None)
        self.verticalLayout_3.addWidget(self.inventory_table())

    def btn_items_click(self):
        for i in reversed(range(self.verticalLayout_3.count())):
            self.verticalLayout_3.itemAt(i).widget().setParent(None)
        self.verticalLayout_3.addWidget(self.items_table())

    def btn_sales_click(self):
        for i in reversed(range(self.verticalLayout_3.count())):
            self.verticalLayout_3.itemAt(i).widget().setParent(None)
        self.verticalLayout_3.addWidget(self.sales_table())

    def btn_received_click(self):
        for i in reversed(range(self.verticalLayout_3.count())):
            self.verticalLayout_3.itemAt(i).widget().setParent(None)
        self.verticalLayout_3.addWidget(self.received_table())

    def btn_operators_click(self):
        for i in reversed(range(self.verticalLayout_3.count())):
            self.verticalLayout_3.itemAt(i).widget().setParent(None)

        # self.verticalLayout_3.addWidget(self.operators_table())
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.addOperator = QtWidgets.QPushButton(self.frame_6)
        self.addOperator.setText("Add Operator")
        self.addOperator.setObjectName("addOperator")
        self.horizontalLayout_2.addWidget(self.addOperator)
        spacerItem = QtWidgets.QSpacerItem(652, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_3.addWidget(self.frame_6)

        ## Lower frame
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        # self.tableWidget = QtWidgets.QTableWidget(self.frame_7)
        # self.tableWidget.setRowCount(9)
        # self.tableWidget.setColumnCount(9)
        # self.tableWidget.setObjectName("tableWidget")

        self.verticalLayout_5.addWidget(self.operators_table())
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_3.addWidget(self.frame_7)

    '''
        Ends button events handlers
    '''

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bortec Inventory Analytics System"))
        self.label.setText(_translate("MainWindow", "<h2><i><b><font color=red>BORTEC</font></b></i></h2>"))
        self.pushButton.setText(_translate("MainWindow", "Items"))
        self.pushButton_2.setText(_translate("MainWindow", "Sales"))
        self.pushButton_3.setText(_translate("MainWindow", "Received"))
        self.pushButton_4.setText(_translate("MainWindow", "Inventory"))
        self.pushButton_operators.setText(_translate("MainWindow", "Operators"))
        self.pushButton_5.setText(_translate("MainWindow", "Analytics"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuWindow.setTitle(_translate("MainWindow", "Window"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
