import sys
from PyQt5 import QtGui
from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.le = QtWidgets.QLineEdit()
        self.b = QtWidgets.QPushButton('Clear')
        self.b2 = QtWidgets.QPushButton('Print')

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.le)
        v_box.addWidget(self.b)
        v_box.addWidget(self.b2)

        self.setLayout(v_box)

        self.setWindowTitle('PyQt5 lesson 5')

        self.b.clicked.connect(self.btn_clk)
        self.b2.clicked.connect(self.btn_clk)

        self.show()

    def btn_clk(self):
        sender = self.sender()
        if sender.text() == 'Print':
            print(self.le.text())
        else:
            self.le.clear()


app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
