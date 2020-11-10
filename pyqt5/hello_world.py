import sys
import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(300, 200)  # 창 크기를 변화시킨다.
        self.lineEdit = QLineEdit(self)  # <input />
        self.pushButton = QPushButton(self)  # <button />
        self.pushButton.move(0, 100)  # 버튼을 100만큼 밑으로 내린다.


if __name__ == "__main__":
    # 기본적인 프로그램 실행 역할
    app = QApplication(sys.argv)

    main_widget = MainWidget()

    # 화면을 띄워준다.
    main_widget.show()

    # 프로그램을 이벤트 루프(무한 루프)로 진입시키는 메서드 -> 계속 창을 띄워준다. & 프로그램에서 벌어지는 이벤트를 받아 처리한다.
    app.exec_()
