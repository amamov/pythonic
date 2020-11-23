import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic

UI_PATH = "./UI.ui"


class MainWidget(QWidget):

    """
    Calculator
    """

    def __init__(self):
        super().__init__()
        uic.loadUi(UI_PATH, self)

        # 숫자 버튼 제어
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
            self.num_pushButton_9,
            self.num_pushButton_dot,
        ]
        for button in num_buttons:
            button.clicked.connect(
                lambda state, button=button: self.num_clicked(state, button)
            )  # 이벤트 리스너 연결

        self.delete_pushButton.clicked.connect(self.del_clicked)
        self.reset_pushButton.clicked.connect(self.reset_clicked)

        # 연산자 버튼 제어
        opers_buttons = [
            self.sign_pushButton_plus,
            self.sign_pushButton_minus,
            self.sign_pushButton_mul,
            self.sign_pushButton_div,
        ]
        for button in opers_buttons:
            button.clicked.connect(
                lambda state, button=button: self.opers_clicked(state, button)
            )

        self.result_pushButton.clicked.connect(self.result_clicked)

    def result_clicked(self):
        current_line_text = self.q_lineEdit.text()  # 현재 데이터
        try:
            result = eval(current_line_text)
            self.q_lineEdit.setText(str(result))
        except Exception:
            self.q_lineEdit.setText("")

    def opers_clicked(self, state, button):
        current_line_text = self.q_lineEdit.text()  # 현재 데이터
        updated_line_text = current_line_text + button.text()  # 업데이트된 데이터
        self.q_lineEdit.setText(updated_line_text)

    def reset_clicked(self):
        self.q_lineEdit.setText("")

    def del_clicked(self):
        current_line_text = self.q_lineEdit.text()  # 현재 데이터
        self.q_lineEdit.setText(current_line_text[:-1])

    def num_clicked(self, state, button):
        current_line_text = self.q_lineEdit.text()  # 현재 데이터
        updated_line_text = current_line_text + button.text()  # 업데이트된 데이터
        self.q_lineEdit.setText(updated_line_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_widget = MainWidget()
    main_widget.show()
    app.exec_()
