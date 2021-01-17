# -*- coding: utf-8 -*-

import sys, os
import startUi, input1Ui, input2Ui, progressUi, databaseUi, finishUi
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
import svzmdo_handler
import threading

class Start(QtWidgets.QWidget, startUi.Ui_Form):

    def __init__(self, nextStepFunc):
        super(Start, self).__init__()
        self.setupUi(self) # design was initialized

        self.nextStepFunc = nextStepFunc

        self.pb_UP.id = False
        self.pb_SVZMDO.id = True
        self.pb_UP.clicked.connect(self.step)
        self.pb_SVZMDO.clicked.connect(self.step)

        
    def step(self):
        btn = self.sender() #clicked button
        if btn.id:
            self.nextStepFunc(True)
        else:
            self.nextStepFunc(False)

class Input1(QtWidgets.QWidget, input1Ui.Ui_Form):
    def __init__(self, nextStepFunc, setData, getData):
        super(Input1, self).__init__()
        self.setupUi(self) # design was initialized
        self.current_directory = os.path.abspath(os.curdir)

        self.nextStepFunc = nextStepFunc
        self.setData = setData
        self.getData = getData

        self.pb_continue.clicked.connect(self.step)

        self.foldername_SESSION = None
        self.pb_chooseSessionFolder.id = 'session'
        self.pb_chooseSessionFolder.clicked.connect(self.chooseFolder)
        self.foldername_SV = None
        self.pb_chooseSVFolder.id = 'sv'
        self.pb_chooseSVFolder.clicked.connect(self.chooseFolder)


    def chooseFolder(self):
        btn = self.sender() #clicked button
        if btn.id == 'session':
            advice = 'Выберите папку со сводными ведомостями:'
        else:
            advice = 'Выберите папку с файлами сессий:'

        foldername = QFileDialog.getExistingDirectory(None, advice, self.current_directory, QtWidgets.QFileDialog.ShowDirsOnly)
        
        if btn.id == 'session':
            self.foldername_SESSION = foldername
        else:
            self.foldername_SV = foldername

        
    def step(self):
        data = self.getData()
        print('getData is done')
        data['foldername_SESSION'] = self.foldername_SESSION
        data['foldername_SV'] = self.foldername_SV
        self.setData(data)
        
        self.nextStepFunc()

class Input2(QtWidgets.QWidget, input2Ui.Ui_Form):
    def __init__(self, nextStepFunc, setData, getData):
        super(Input2, self).__init__()
        self.setupUi(self) # design was initialized

        self.nextStepFunc = nextStepFunc
        self.setData = setData
        self.getData = getData

        self.pb_continue.clicked.connect(self.step)

        self.firstCourse = None
        self.firstSession = None        

        
    def step(self):
        self.firstCourse = int(self.comboBox_firstCourse.currentText())
        self.firstSession = self.lineEdit_firstSession.text()

        data = self.getData()
        data['firstCourse'] = self.firstCourse
        data['firstSession'] = self.firstSession
        self.setData(data)
        
        self.nextStepFunc()

class Progress(QtWidgets.QWidget, progressUi.Ui_Form):
    run_trigger = pyqtSignal()

    def __init__(self, nextStepFunc, getData):
        super(Progress, self).__init__()
        self.setupUi(self) # design was initialized
        self.databaseDesign = Database(self.step_database)

        self.nextStepFunc = nextStepFunc
        self.getData = getData

        self.thread = QThread()
        self.thread.start()
        self.is_ready = threading.Event()

        self.handler = svzmdo_handler.Handler(self, self.show_database, self.is_ready)
        self.run_trigger.connect(self.handler.run)
        self.handler.moveToThread(self.thread)

    @pyqtSlot(list)
    def show_database(self, list_with_disciplines):
        # list_with_disciplines: unknown disc and list of known disciplines from SESSION
        self.databaseDesign.fill(list_with_disciplines)
        self.databaseDesign.show()

    def step_database(self, answer_string):
        self.databaseDesign.hide()
        self.handler.set_answer_string(answer_string)
        self.is_ready.set()

    def svzmdo_handler_start(self):
        data = self.getData()
        self.handler.data = data
        self.run_trigger.emit()
        
    def step(self):
        self.nextStepFunc()

class Database(QtWidgets.QWidget, databaseUi.Ui_Form):
    def __init__(self, nextStepFunc):
        super(Database, self).__init__()
        self.setupUi(self) # design was initialized

        self.nextStepFunc = nextStepFunc

        self.pb_continue.clicked.connect(self.step)

    def fill(self, list_with_disciplines):
        _translate = QtCore.QCoreApplication.translate
        # Filling of label
        self.label_someDisciplineName.setText(list_with_disciplines[0])

        # Filling of comboBox
        disciplines_from_SESSION = list_with_disciplines[1]
        for i in range(len(disciplines_from_SESSION)):
            self.comboBox_disciplineNameSV.addItem("")
            self.comboBox_disciplineNameSV.setItemText(i, _translate("Form", disciplines_from_SESSION[i]))

    def get_answer_string(self, label_string, comboBox_string):
        answer_string = "\n" + label_string + ";" + comboBox_string
        return answer_string

    def step(self):
        label_string = self.label_someDisciplineName.text()
        comboBox_string = self.comboBox_disciplineNameSV.currentText()
        answer_string = self.get_answer_string(label_string, comboBox_string)
        self.nextStepFunc(answer_string)