import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel


class BYshka(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.k = 2
        self.setGeometry(621, 621, 621, 621)
        self.setFixedSize(621, 621)
        self.setWindowTitle('Cyrcle')

        self.button.move(230, 20)
        self.pablo = QPixmap("krug.png")
        self.p = QLabel(self)
        self.p.setPixmap(self.pablo)
        self.p.resize(500, 500)
        self.p.move(10000, 10000)

        self.button.clicked.connect(self.cyrcle)

    def cyrcle(self):
        if self.k % 2 == 0:
            self.p.move(100, 100)
            self.k += 1
        else:
            self.p.move(1000, 1000)
            self.k += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BYshka()
    ex.show()
    sys.exit(app.exec_())
