from PyQt5 import uic, QtWidgets


def red_menu_action():
    screen.label_2.setText("Red")
    screen.label_2.setStyleSheet("color: red;")


def green_menu_action():
    screen.label_2.setText("Green")
    screen.label_2.setStyleSheet("color: green;")


def blue_menu_action():
    screen.label_2.setText("Blue")
    screen.label_2.setStyleSheet("color: blue;")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    screen = uic.loadUi("menu.ui")

    screen.actionRed.triggered.connect(red_menu_action)
    screen.actionGreen.triggered.connect(green_menu_action)
    screen.actionBlue.triggered.connect(blue_menu_action)

    screen.show()
    app.exec()
