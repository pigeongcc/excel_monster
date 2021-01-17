# -*- coding: utf-8 -*-

import design
import sys
from PyQt5 import QtWidgets
from threading import Event

class MainClass(QtWidgets.QMainWindow):
    
    def __init__(self):
        self.data = {
            'foldername_SESSION': None,
            'foldername_SV': None,
            'firstCourse': None,
            'firstSession': None
        }

        self.startDesign = design.Start(self.step_start)
        self.input1Design = design.Input1(self.step_input1, self.setData, self.getData)
        self.input2Design = design.Input2(self.step_input2, self.setData, self.getData)
        self.progressDesign = design.Progress(self.step_progress, self.getData)
        #self.finishDesign = design.Start(self.step1)
        print('\nBEST DEBUG EVER\n')

        self.startDesign.show()
        
    def setData(self, data):
        print(self.data)
        self.data = data
        print('is set to')
        print(self.data)
        print()

    def getData(self):
        print(self.data)
        print('is returned')
        print()
        return self.data

    def step_start(self, flag):
        self.startDesign.hide()
        if flag:
            self.input1Design.show()
        else:
            pass

    def step_input1(self):
        self.input1Design.hide()
        self.input2Design.show()

    def step_input2(self):
        self.input2Design.hide()
        self.progressDesign.show()
        self.progressDesign.svzmdo_handler_start()
        print('Hey there')
    
    def step_progress(self):
        self.progressDesign.hide()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainClass()
    sys.exit(app.exec_())
