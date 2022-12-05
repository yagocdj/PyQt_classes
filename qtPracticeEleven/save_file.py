from PyQt5 import uic, QtWidgets

def save():
    name = screen.lineEdit.text()
    age = screen.lineEdit_2.text()
    phone = screen.lineEdit_3.text()

    data = f"Name: {name}\nAge: {age}\nPhone: {phone}\n"

    file = QtWidgets.QFileDialog.getSaveFileName()[0]  # it returns the file's path

    with open(f"{file}.txt", 'w') as f:
        f.write(data)


def readFromFile():
    file = QtWidgets.QFileDialog.getOpenFileName()[0]

    with open(file, 'r') as f:
        screen.label_6.setText(f.read())


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    screen = uic.loadUi("save.ui")

    screen.actionSave.triggered.connect(save)
    screen.actionOpen.triggered.connect(readFromFile)

    screen.show()
    app.exec()