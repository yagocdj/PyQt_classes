from PyQt5 import uic, QtWidgets


def main_function():

    if form.radioButton.isChecked():
        selected_option = "Red"
    elif form.radioButton_2.isChecked():
        selected_option = "Green"
    elif form.radioButton_3.isChecked():
        selected_option = "Blue"
    elif form.radioButton_4.isChecked():
        selected_option = "Pink"
    else:
        selected_option = ""

    form.label_2.setText("Selected color: " + selected_option)


app = QtWidgets.QApplication([])
form = uic.loadUi("color_window.ui")
form.pushButton.clicked.connect(main_function)

form.show()
app.exec()
