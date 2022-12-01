from PyQt5 import uic, QtWidgets

def callSecondWindow():
    second_window.show()
    second_window.label.setText("Hello world!")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    
    first_window = uic.loadUi("firstWindow.ui")
    second_window = uic.loadUi("secondWindow.ui")
    
    first_window.pushButton.clicked.connect(callSecondWindow)

    first_window.show()
    app.exec()
