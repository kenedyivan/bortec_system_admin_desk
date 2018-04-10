import sys
from PyQt5 import QtGui
from PyQt5 import QtWidgets


def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    # button
    b = QtWidgets.QPushButton(w)
    b.setText('Push Me')
    b.move(100, 50)
    # --end of button

    # labels
    l1 = QtWidgets.QLabel(w)
    l1.setText('Look at me')
    # --end of labels

    h_box = QtWidgets.QHBoxLayout()
    h_box.addStretch()
    h_box.addWidget(l1)
    h_box.addStretch()

    # layout manager
    v_box = QtWidgets.QVBoxLayout()
    v_box.addWidget(b)
    v_box.addWidget(l1)
    v_box.addLayout(h_box)
    w.setLayout(v_box)
    # --end layout manager

    w.setWindowTitle('Bortec Smart System')
    l1.move(130, 20)
    w.show()
    sys.exit(app.exec_())


window()
