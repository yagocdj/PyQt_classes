from PyQt5 import uic, QtWidgets


def sum():

    my_sum = 0
    
    if first_screen.checkBox_1.isChecked():
        my_sum += 15.0
        first_screen.checkBox_1.setChecked(False)

    if first_screen.checkBox_2.isChecked():
        my_sum += 20.0
        first_screen.checkBox_2.setChecked(False)

    if first_screen.checkBox_3.isChecked():
        my_sum += 10.0
        first_screen.checkBox_3.setChecked(False)

    if first_screen.checkBox_4.isChecked():
        my_sum += 32.0
        first_screen.checkBox_4.setChecked(False)

    if first_screen.checkBox_5.isChecked():
        my_sum += 5.50
        first_screen.checkBox_5.setChecked(False)
        
    first_screen.label.setText(f"Total value: {my_sum:.2f}")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    first_screen = uic.loadUi("checkboxSum.ui")
    first_screen.pushButton.clicked.connect(sum)

    first_screen.show()
    app.exec()
