from PyQt5 import uic, QtWidgets


def showFrame1():
    screen.frame_2.close()


def showFrame2():
    screen.frame_2.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    screen = uic.loadUi("frame.ui")

    screen.pushButton_2.clicked.connect(showFrame1)
    screen.pushButton_4.clicked.connect(showFrame2)

    screen.show()
    app.exec()
