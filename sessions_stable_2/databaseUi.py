# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'database.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(901, 257)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(270, 10, 401, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 271, 41))
        self.label_2.setObjectName("label_2")
        self.comboBox_disciplineNameSV = QtWidgets.QComboBox(Form)
        self.comboBox_disciplineNameSV.setGeometry(QtCore.QRect(30, 110, 851, 22))
        self.comboBox_disciplineNameSV.setObjectName("comboBox_disciplineNameSV")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 481, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 170, 571, 31))
        self.label_4.setObjectName("label_4")
        self.label_someDisciplineName = QtWidgets.QLabel(Form)
        self.label_someDisciplineName.setGeometry(QtCore.QRect(300, 50, 400, 41))
        self.label_someDisciplineName.setObjectName("label_someDisciplineName")
        self.pb_continue = QtWidgets.QPushButton(Form)
        self.pb_continue.setGeometry(QtCore.QRect(380, 210, 151, 31))
        self.pb_continue.setObjectName("pb_continue")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">Помогите программе определить учебную дисциплину</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p>В файле сессии обнаружена дисциплина</p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p>Выберите название этой дисциплины из списка дисциплин сводной ведомости:</p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p>Перед продолжением убедитесь, что все документы из выбранных ранее папок <span style=\" font-weight:600;\">закрыты</span></p></body></html>"))
        self.label_someDisciplineName.setText(_translate("Form", "<html><head/><body><p><span style=\" font-style:italic;\">some_discipline_name</span></p></body></html>"))
        self.pb_continue.setText(_translate("Form", "Продолжить"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
