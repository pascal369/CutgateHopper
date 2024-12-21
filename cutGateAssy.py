# -*- coding: utf-8 -*-
import os
import sys
import Import
from PySide import QtGui
from PySide import QtUiTools
from PySide import QtCore
from FreeCAD import Base
import FreeCADGui as Gui
import DraftVecUtils
import Sketcher
import PartDesign
from math import pi
import Draft
import FreeCAD, FreeCADGui
import FreeCAD as App

hopper_series=['2m3','3m3','4m3','5m3','6m3','7m3','8m3','10m3','12m3',]

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName('Dialog')
        Dialog.resize(300, 70)
        Dialog.move(1000, 0)

        #Series
        self.label_Series = QtGui.QLabel('Series',Dialog)
        self.label_Series.setGeometry(QtCore.QRect(10, 13, 100, 12))
        self.comboBox_Series = QtGui.QComboBox(Dialog)
        self.comboBox_Series.setGeometry(QtCore.QRect(80, 10, 200, 22))
        #Create
        self.pushButton2 = QtGui.QPushButton('Create',Dialog)
        self.pushButton2.setGeometry(QtCore.QRect(80, 35, 100, 22))
        self.comboBox_Series.addItems(hopper_series) 

        QtCore.QObject.connect(self.pushButton2, QtCore.SIGNAL("pressed()"), self.create)

        self.retranslateUi(Dialog)
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", 'cutGateHopper', None))

    def create(self):
 
             mypath=self.comboBox_Series.currentText()
             fname=mypath+'Assy.FCStd'
             
             base=os.path.dirname(os.path.abspath(__file__))
             try:
                 joined_path = os.path.join(base, 'Assy',fname) 
                 print(joined_path)
                 Gui.ActiveDocument.mergeProject(joined_path) 
             except:
                  pass
             Gui.SendMsgToActiveView("ViewFit")
    
class main():
        d = QtGui.QWidget()
        d.ui = Ui_Dialog()
        d.ui.setupUi(d)
        d.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        d.show() 
        