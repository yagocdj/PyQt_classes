import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QToolTip,
    QLabel,
    QLineEdit
)
from PyQt5 import QtGui

class Window(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        self.top = 100
        self.left = 100
        self.window_width = 800
        self.window_height = 600
        self.title = "First Window"

        # Text Field
        self.text_field = QLineEdit(self)
        self.text_field.move(300, 100)  # x, y
        self.text_field.resize(200, 25)  # w, h

        # Button One
        button_one = QPushButton("Button One", self)
        button_one.move(150, 275)
        button_one.resize(150, 80)
        button_one.setStyleSheet("""
            QPushButton {
                background-color: #ae168a;
                font: bold;
                font-size: 20px
            }""")
        button_one.clicked.connect(self.buttonOneClick)

        # Button Two
        button_two = QPushButton("Button Two", self)
        button_two.move(315, 275)
        button_two.resize(150, 80)
        button_two.setStyleSheet("""
            QPushButton {
                background-color: #98f448;
                font: bold;
                font-size: 20px
            }""")
        button_two.clicked.connect(self.buttonTwoClick)

        # Show Typed Text Button
        show_text_button = QPushButton("Show Text", self)
        show_text_button.move(480, 275)
        show_text_button.resize(150, 80)
        show_text_button.setStyleSheet("""
            QPushButton {
                background-color: #4683e8;
                font: bold;
                font-size: 20px
            }""")
        show_text_button.clicked.connect(self.showTypedText)

        # Label One
        # We need to put the self keyword to make the label_one an attribute defined in our __init__ method
        self.label_one = QLabel(self)
        self.label_one.setText("Press a button")
        self.label_one.move(300, 50)
        self.label_one.setStyleSheet("""
            QLabel {
                font: bold;
                font-size: 25px;
                color: "blue"
            }""")
        self.label_one.resize(400, 25)

        # Show Typed Text Label
        self.show_text_label = QLabel(self)
        self.show_text_label.setText("Text: ")
        self.show_text_label.move(150, 175)
        self.show_text_label.setStyleSheet("""
            QLabel {
                font: bold;
                font-size: 25px;
                color: "blue"
            }""")
        self.show_text_label.resize(400, 35)

        # Cat Label
        self.cat = QLabel(self)
        self.cat.move(75, 400)
        self.cat.setPixmap(QtGui.QPixmap('imgs/kittyOne.jpg'))
        self.cat.resize(800, 300)

        self.loadWindow()

    def loadWindow(self):
        self.setGeometry(self.left, self.top, self.window_width, self.window_height)
        self.setWindowTitle(self.title)
        self.show()

    def buttonOneClick(self):
        
        self.label_one.setText("Kitty!")
        self.label_one.setStyleSheet("""
            QLabel {
                font: bold;
                font-size: 25px;
                color: "green"
            }""")
        self.cat.setPixmap(QtGui.QPixmap('imgs/kittyOne.jpg'))

    def buttonTwoClick(self):
        
        self.label_one.setText("Puppy!")
        self.label_one.setStyleSheet("""
            QLabel {
                font: bold;
                font-size: 25px;
                color: "red"
            }""")
        self.cat.setPixmap(QtGui.QPixmap('imgs/puppyTwo.jpg'))

    def showTypedText(self):
        
        user_input = self.text_field.text()
        self.show_text_label.setText("Text: " + user_input)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
