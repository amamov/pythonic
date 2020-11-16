import sys
import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

UI_PATH = "./ui/calculator.ui"


class MainDialog(QDialog):

    """ main Dialog """

    def __init__(self):
        super().__init__()
        uic.loadUi(UI_PATH, self)
        num_buttons = [
            self.num_pushButton_0,
            self.num_pushButton_1,
            self.num_pushButton_2,
            self.num_pushButton_3,
            self.num_pushButton_4,
            self.num_pushButton_5,
            self.num_pushButton_6,
            self.num_pushButton_7,
            self.num_pushButton_8,
            self.num_pushButton_8,
            self.num_pushButton_9,
        ]
        for button in num_buttons:
            button.clicked.connect(
                lambda state, button=button: self.num_clicked(state, button)
            )

    def num_clicked(self, state, button):
        current_line_text = self.q_lineEdit.text()
        updated_line_text = current_line_text + button.text()
        self.q_lineEdit.setText(updated_line_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_dialog = MainDialog()
    main_dialog.show()
    app.exec_()