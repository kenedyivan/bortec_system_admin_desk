from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import mysql.connector
import bcrypt


class GUIForm(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.mylayout()

    def mylayout(self):
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setObjectName("LoginDialog")
        self.resize(400, 300)
        self.setWindowTitle("Admin Login")
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(61, 51, 251, 131))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(60, 200, 251, 20))
        self.label_3.setStyleSheet("color:rgb(255, 0, 0)")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.frame)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi()
        self.buttonBox.accepted.connect(self.btn_login_clk)
        self.buttonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)

    def btn_login_clk(self):
        self.username = str(self.lineEdit.text()).strip()
        self.password = str(self.lineEdit_2.text()).strip()

        if self.authenticate_user(self.username, self.password):
            self.hide()
        else:
            self.label_3.setText("Wrong credentials!")

    def authenticate_user(self, username, password):
        conn = mysql.connector.connect(user='root', password='root', host='localhost', database='bortec_inv_system_db')
        cursor = conn.cursor()
        cursor.execute('select username, password from admins')
        data_list = cursor.fetchall()
        db_username = ''
        db_password = ''
        for row_number, d in enumerate(data_list):
            db_username = d[0]
            db_password = d[1]

        if username == db_username:
            if password == db_password:
                is_auth = True
            else:
                is_auth = False
        else:
            is_auth = False
        conn.close()
        return is_auth

    def reject(self):
        self.close()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Admin login"))
        self.label.setText(_translate("Dialog", "Username:"))
        self.label_2.setText(_translate("Dialog", "Password:"))

    def closeEvent(self, event):
        exit(0)
        event.accept()


# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     myapp = GUIForm()
#     myapp.show()
#     ret = app.exec_()
#     sys.exit(ret)
