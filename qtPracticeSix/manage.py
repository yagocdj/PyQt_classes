from PyQt5 import uic, QtWidgets

value = 0

def increase_progress():
    global value
    value += 10
    window.progressBar.setValue(value)


def reset_progress():
    global value
    value = 0
    window.progressBar.setValue(value)


if __name__ == "__main__":

    app = QtWidgets.QApplication([])

    window = uic.loadUi("progressBar.ui")

    window.pushButton.clicked.connect(increase_progress)
    window.pushButton_2.clicked.connect(reset_progress)

    window.show()
    app.exec()
