from PyQt5 import uic, QtWidgets


def list_data():
    read_data = data_list.lineEdit.text()
    data_list.listWidget.addItem(read_data)
    data_list.lineEdit.setText("")

def delete_data():
    data_list.listWidget.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    data_list = uic.loadUi("data_list.ui")
    data_list.pushButton.clicked.connect(list_data)
    data_list.pushButton_2.clicked.connect(delete_data)

    data_list.show()
    app.exec()
