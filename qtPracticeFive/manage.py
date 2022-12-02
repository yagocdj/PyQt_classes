from PyQt5 import uic, QtWidgets

def callSecondWindow():

    second_window.show()

    # In case you want to hide the first window when the first is opened,
    # do the following:
    # first_window.hide()

    second_window.label.setText("Hello world!")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    
    first_window = uic.loadUi("firstWindow.ui")
    second_window = uic.loadUi("secondWindow.ui")
    
    first_window.pushButton.clicked.connect(callSecondWindow)

    first_window.show()
    app.exec()
