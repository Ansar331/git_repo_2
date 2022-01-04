from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QColor
import random
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('lolo.ui', self)
        self.should_paint_circle = False
        self.lolo = QtWidgets.QPushButton('НАЖАТЬ', self)
        self.lolo.setGeometry(10, 10, 200, 100)
        self.colors = ['RED', 'BLUE', 'GREEN', 'YELLOW']
        self.lolo.clicked.connect(self.paintcircle)
        self.lolo.clicked.connect(self.paintEvent)
        self.should_paint_circle = False

    def paintEvent(self, event):
        if self.should_paint_circle:
            painter = QtGui.QPainter(self)
            painter.setBrush(QColor(self.colors[random.randint(0, 3)]))
            pen = QtGui.QPen()
            pen.setWidth(5)
            painter.setPen(pen)
            a = random.randint(1, 300)
            b = random.randint(1, 300)
            c = random.randint(1, 300)
            painter.drawEllipse(400, 400, a, a)
            painter.drawEllipse(200, 250, b, b)
            painter.drawEllipse(150, 100, c, c)

    def paintcircle(self):
        self.should_paint_circle = True
        self.update()


def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    application()
