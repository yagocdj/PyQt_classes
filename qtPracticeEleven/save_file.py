from PyQt5 import uic, QtWidgets

def save():
    name = screen.lineEdit.text()
    age = screen.lineEdit_2.text()
    phone = screen.lineEdit_3.text()

    data = f"Name: {name}\nAge: {age}\nPhone: {phone}\n"

    file = QtWidgets.QFileDialog.getSaveFileName()[0]  # it returns the file's path

    with open(f"{file}.txt", 'w') as f:
        f.write(data)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    screen = uic.loadUi("save.ui")

    screen.actionSave.triggered.connect(save)

    screen.show()
    app.exec()