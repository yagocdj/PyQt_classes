from PyQt5 import uic, QtWidgets

def selected_option():
    city = screen.comboBox.currentText()
    screen.label_2.setText("City: " + city)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    screen = uic.loadUi("combobox.ui")

    screen.comboBox.addItems(["João Pessoa", "Guarabira", "Campina Grande", "Recife", "Caruaru", "Macaparana", "Sapé", "Areia", "Mari", "Cajazeiras", "Bayeux", "Cabedelo", "Santa Rita", "Itambé"])
    screen.pushButton.clicked.connect(selected_option)

    screen.show()
    app.exec()
