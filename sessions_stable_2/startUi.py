# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(901, 257)
        self.pb_SVZMDO = QtWidgets.QPushButton(Form)
        self.pb_SVZMDO.setGeometry(QtCore.QRect(460, 20, 421, 211))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pb_SVZMDO.setFont(font)
        self.pb_SVZMDO.setObjectName("pb_SVZMDO")
        self.pb_UP = QtWidgets.QPushButton(Form)
        self.pb_UP.setGeometry(QtCore.QRect(20, 20, 421, 211))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pb_UP.setFont(font)
        self.pb_UP.setObjectName("pb_UP")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pb_SVZMDO.setText(_translate("Form", "Заполнение сводных ведомостей\n"
"Генерация данных на ЗМ, ДО"))
        self.pb_UP.setText(_translate("Form", "Генерация сводной ведомости"))


'''
if __name__ == "__main__":
    main()
'''

def main(next_step):
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    ui.pb_SVZMDO.clicked.connect(next_step)
    Form.show()
    sys.exit(app.exec_())