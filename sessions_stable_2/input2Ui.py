# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'input2.ui'
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
        self.label.setGeometry(QtCore.QRect(360, 10, 141, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(330, 70, 161, 41))
        self.label_2.setObjectName("label_2")
        self.comboBox_firstCourse = QtWidgets.QComboBox(Form)
        self.comboBox_firstCourse.setGeometry(QtCore.QRect(490, 80, 191, 22))
        self.comboBox_firstCourse.setModelColumn(0)
        self.comboBox_firstCourse.setObjectName("comboBox_firstCourse")
        self.comboBox_firstCourse.addItem("")
        self.comboBox_firstCourse.addItem("")
        self.comboBox_firstCourse.addItem("")
        self.comboBox_firstCourse.addItem("")
        self.comboBox_firstCourse.addItem("")
        self.comboBox_firstCourse.addItem("")
        self.comboBox_firstCourse.addItem("")
        self.comboBox_firstCourse.addItem("")
        self.comboBox_firstCourse.addItem("")
        self.comboBox_firstCourse.addItem("")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(160, 100, 321, 31))
        self.label_3.setObjectName("label_3")
        self.lineEdit_firstSession = QtWidgets.QLineEdit(Form)
        self.lineEdit_firstSession.setGeometry(QtCore.QRect(490, 110, 191, 22))
        self.lineEdit_firstSession.setObjectName("lineEdit_firstSession")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(240, 130, 361, 31))
        self.label_4.setObjectName("label_4")
        self.pb_continue = QtWidgets.QPushButton(Form)
        self.pb_continue.setGeometry(QtCore.QRect(360, 190, 151, 31))
        self.pb_continue.setObjectName("pb_continue")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">Заполнение данных</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p>Выберите первый курс:</p></body></html>"))
        self.comboBox_firstCourse.setItemText(0, _translate("Form", "20"))
        self.comboBox_firstCourse.setItemText(1, _translate("Form", "21"))
        self.comboBox_firstCourse.setItemText(2, _translate("Form", "22"))
        self.comboBox_firstCourse.setItemText(3, _translate("Form", "23"))
        self.comboBox_firstCourse.setItemText(4, _translate("Form", "24"))
        self.comboBox_firstCourse.setItemText(5, _translate("Form", "25"))
        self.comboBox_firstCourse.setItemText(6, _translate("Form", "26"))
        self.comboBox_firstCourse.setItemText(7, _translate("Form", "27"))
        self.comboBox_firstCourse.setItemText(8, _translate("Form", "28"))
        self.comboBox_firstCourse.setItemText(9, _translate("Form", "29"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p>Введите <span style=\" text-decoration: underline;\">первую сессию</span> для этого курса по образцу:</p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-style:italic;\">Например, для 28 курса: </span><span style=\" font-weight:600; font-style:italic;\">зима-18-19</span></p></body></html>"))
        self.pb_continue.setText(_translate("Form", "Продолжить"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
