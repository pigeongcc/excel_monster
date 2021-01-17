# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'input.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(901, 257)
        self.pb_chooseSVFolder = QtWidgets.QPushButton(Form)
        self.pb_chooseSVFolder.setGeometry(QtCore.QRect(20, 40, 341, 61))
        self.pb_chooseSVFolder.setObjectName("pb_chooseSVFolder")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(570, 10, 141, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(390, 50, 481, 51))
        self.label_2.setObjectName("label_2")
        self.pb_chooseSessionFolder = QtWidgets.QPushButton(Form)
        self.pb_chooseSessionFolder.setGeometry(QtCore.QRect(20, 120, 341, 71))
        self.pb_chooseSessionFolder.setObjectName("pb_chooseSessionFolder")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(390, 120, 511, 71))
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(20, 100, 861, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pb_continue = QtWidgets.QPushButton(Form)
        self.pb_continue.setGeometry(QtCore.QRect(560, 210, 151, 31))
        self.pb_continue.setObjectName("pb_continue")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pb_chooseSVFolder.setText(_translate("Form", "Выбрать папку, содержащую сводные ведомости"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">Важная инфрмация</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p>- Проверьте, чтобы папка содержала <span style=\" text-decoration: underline;\">только сводные ведомости</span></p><p>- Должен соблюдаться формат названия сводной ведомости: <span style=\" font-weight:600; font-style:italic;\">сводная-26.xlsx</span></p></body></html>"))
        self.pb_chooseSessionFolder.setText(_translate("Form", "Выбрать папку, содержащую файлы сессий"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p>- Проверьте, чтобы папка содержала <span style=\" text-decoration: underline;\">только файлы сессий</span></p><p>- Должен соблюдаться формат названия файла сессии: <span style=\" font-weight:600; font-style:italic;\">сессия-лето-19-20.xlsx</span></p><p>- В каждом файле сессии средние баллы должны находиться в столбце <span style=\" font-weight:600; font-style:italic;\">\'AD\'</span></p></body></html>"))
        self.pb_continue.setText(_translate("Form", "Продолжить"))




if __name__ == "__main__":
    main()

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
