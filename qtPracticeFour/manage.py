from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox


def showMessage():
    read_data = window.lineEdit.text()
    print(read_data)
    window.lineEdit.setText("")
    
    if read_data == "":
        QMessageBox.about(window, "Warning", "No name typed in")
    else:
        QMessageBox.about(window, "Warning", "Hello, {}!".format(read_data))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = uic.loadUi("messageBox.ui")
    window.pushButton.clicked.connect(showMessage)

    window.show()
    app.exec()
