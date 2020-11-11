from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_photoForm(object):
    def setupUi(self, photoForm):
        photoForm.setObjectName("photoForm")
        photoForm.resize(384, 246)
        photoForm.setStyleSheet("background-color: #94c4fd;")
        self.lineEdit = QtWidgets.QLineEdit(photoForm)
        self.lineEdit.setGeometry(QtCore.QRect(60, 120, 261, 31))
        self.lineEdit.setStyleSheet(
            "background-color: rgb(248, 248, 250);\n"
            "border-radius:15px;\n"
            "padding: 5px;\n"
            "color: gray;\n"
            "font-size: 14px;\n"
            ""
        )
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayoutWidget = QtWidgets.QWidget(photoForm)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 160, 291, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setStyleSheet(
            "background-color: #5e98c4;\n"
            "color: #94c4fd;\n"
            "border-radius: 21px;\n"
            "font-size: 15px;"
        )
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setStyleSheet(
            "background-color: #5e98c4;\n"
            "color: #94c4fd;\n"
            "border-radius: 50%;\n"
            "font-size: 15px;"
        )
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayoutWidget = QtWidgets.QWidget(photoForm)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 32, 293, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titlr = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.titlr.setStyleSheet(
            "color: #5e98c4;\n" "font-size: 25px;\n" "font-weight: 700;\n" ""
        )
        self.titlr.setAlignment(QtCore.Qt.AlignCenter)
        self.titlr.setObjectName("titlr")
        self.verticalLayout.addWidget(self.titlr)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setStyleSheet("font-size: 12px;\n" "color: #5e98c4;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(photoForm)
        QtCore.QMetaObject.connectSlotsByName(photoForm)

    def retranslateUi(self, photoForm):
        _translate = QtCore.QCoreApplication.translate
        photoForm.setWindowTitle(_translate("photoForm", "Form"))
        self.lineEdit.setText(_translate("photoForm", "ex) apple"))
        self.pushButton_2.setText(_translate("photoForm", "Open folder"))
        self.pushButton.setText(_translate("photoForm", "Download"))
        self.titlr.setText(_translate("photoForm", "Photo Scraper"))
        self.label.setText(_translate("photoForm", "어떤 사진을 다운 받고 싶나요? 키워드를 입력해주세요"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    photoForm = QtWidgets.QWidget()
    ui = Ui_photoForm()
    ui.setupUi(photoForm)
    photoForm.show()
    sys.exit(app.exec_())
