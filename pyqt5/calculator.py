import sys
import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

UI_PATH = "./ui/calculator.ui"


class MainDialog(QDialog):

    """ calculator dialog """

    def __init__(self):
        super().__init__()
        uic.loadUi(UI_PATH, self)

        # 숫자 버튼 제어
        num_buttons = [
            self.num_pushButton_1,
            self.num_pushButton_2,
            self.num_pushButton_3,
            self.num_pushButton_4,
            self.num_pushButton_5,
            self.num_pushButton_6,
            self.num_pushButton_7,
            self.num_pushButton_8,
            self.num_pushButton_9,
            self.num_pushButton_dot,
            self.sign_pushButton_plus,
            self.sign_pushButton_minus,
            self.sign_pushButton_mul,
            self.sign_pushButton_div,
        ]
        for button in num_buttons:
            button.clicked.connect(
                lambda state, button=button: self.num_clicked(state, button)
            )  # 이벤트 리스너 연결

    def num_clicked(self, state, button):
        # 버튼에 따라 계산하기 알고리즘 짜기
        current_line_text = self.q_lineEdit.text()  # 현재 데이터
        updated_line_text = current_line_text + button.text()  # 업데이트된 데이터
        self.q_lineEdit.setText(updated_line_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_dialog = MainDialog()
    main_dialog.show()
    app.exec_()
