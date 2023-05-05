# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interface2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import threading
import time
import random 
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox, QApplication, QPushButton, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets, uic 
from time import time, sleep
from PyQt5.QtCore import QBasicTimer, QDateTime, QThread
from PyQt5.QtCore import pyqtSignal, QObject

from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import QCoreApplication, QBasicTimer, QDateTime, Qt, QSize, QTimer
import Interface

class MainWindow(QMainWindow, Interface.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.btn_openO.clicked.connect(self.click_openO) #функции нажатия на кнопки
        self.btn_openAr.clicked.connect(self.click_openAr)
        self.btn_closeO.clicked.connect(self.click_closeO)
        self.btn_closeAr.clicked.connect(self.click_closeAr)
        self.btn_regulateO.clicked.connect(self.click_regulateO)
        self.btn_regulateAr.clicked.connect(self.click_regulateAr)
        self.btn_installO.clicked.connect(self.click_installO)
        self.btn_installAr.clicked.connect(self.click_installAr)
    
    def showEvent(self, event): #запускает программу при при её открытии 
        global current_command 
        current_command = '010F000200020101'
        self.start_readout()

    def start_readout(self):
        global current_command 
        a = '010F000200020101'
        if current_command != a:
            print('модуль получил глобальную команду')
            thread1 = threading.Thread(target = self.fn_sendcmd, args=(current_command,) )
            thread1.start()
            thread1.join()
            current_command = '010F000200020101'
        else:
            print('modul 1 made/ ')
            thread1 = threading.Thread(target = self.fn_sendcmd, args=(a,) )
            thread1.start()
            thread1.join()
            global flow_value
            self.updatelabeltextO(flow_value)
        timer = threading.Timer(2.0, self.second_part, args=(str,))
        timer.start()
 
    def second_part(self, str):
        a = '020F000200020101'
        print('modul 2 made /')
        thread1 = threading.Thread(target = self.fn_sendcmd, args=(a,) )
        thread1.start()
        thread1.join()
        global flow_value
        self.updatelabeltextAr(flow_value)
        self.start_readout()
        
    def updatelabeltextAr(self, str):
        self.label_realflowAr.setText(str)

    def updatelabeltextO(self, str):
        self.label_realflowO.setText(str)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MPC ONE"))
        self.label_7.setText(_translate("MainWindow", "2"))
        self.btn_closeO.setText(_translate("MainWindow", "Закрыть O"))
        self.label.setText(_translate("MainWindow", "2"))
        self.label_3.setText(_translate("MainWindow", "2"))
        self.label_2.setText(_translate("MainWindow", "Поток O "))
        self.label_realflowO.setText(_translate("MainWindow", "0.00"))
        self.btn_openO.setText(_translate("MainWindow", "Открыть O"))
        self.btn_regulateO.setText(_translate("MainWindow", "Регулировать O"))
        self.label_6.setText(_translate("MainWindow", "Поток O"))
        self.btn_installO.setText(_translate("MainWindow", "Установить О"))
        self.label_5.setText(_translate("MainWindow", "2"))
        self.label_4.setText(_translate("MainWindow", "2"))
        self.label_9.setText(_translate("MainWindow", "2"))
        self.label_10.setText(_translate("MainWindow", "Реальный"))
        self.label_11.setText(_translate("MainWindow", "Заданный"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "O2"))
        self.btn_installAr.setText(_translate("MainWindow", "Установить Ar"))
        self.btn_closeAr.setText(_translate("MainWindow", "Закрыть Ar"))
        self.btn_regulateAr.setText(_translate("MainWindow", "Регулировать Ar"))
        self.label_realflowAr.setText(_translate("MainWindow", "0.00"))
        self.label_1.setText(_translate("MainWindow", "Поток Ar"))
        self.label_8.setText(_translate("MainWindow", "Поток Ar"))
        self.btn_openAr.setText(_translate("MainWindow", "Открыть Ar"))
        self.label_12.setText(_translate("MainWindow", "Реальный"))
        self.label_13.setText(_translate("MainWindow", "Заданный"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Ar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Блок питания"))

    def fn_sendcmd(self, number):                                       # извлекаем содержимое ячеек
        print("def fn_sendcmd получило значение - ", number)                         # данные
        self.ed_id= number[0:2]                           # адрес устройства ID
        self.ed_cmd=number[2:4]                           # номер команды
        self.ed_adr=number[4:8]                           # адрес регистра
        self.ed_count=number[8:17]                          # данные
        global flow_value
        flow_value = str(random.randint(0,100))
        sleep(1)

    def click_openO(self):
        global current_command  
        current_command = "010F000200020101"
        type_command = "010F000200020101"
        print("def click_openO выполнено")
        self.fn_sendcmd(type_command) 

    def click_openAr(self):
        global current_command  
        current_command = "020F000200020101"
        type_command = "020F000200020101"
        print("def click_openAr выполнено")
        self.fn_sendcmd(type_command) 
        
    def click_closeO(self):
        global current_command  
        current_command = "010F000200020102"
        type_command = "010F000200020102"
        print("def click_closeO выполнено")
        self.fn_sendcmd(type_command)

    def click_closeAr(self):
        global current_command  
        current_command = "020F000200020102"
        type_command = "020F000200020102"
        print("def click_closeAr выполнено")
        self.fn_sendcmd(type_command)
        
    def click_regulateO(self):
        global current_command  
        current_command = "010F000200020100"
        type_command = "010F000200020100"
        print("def click_regulateO выполнено")
        self.fn_sendcmd(type_command)
        
    def click_regulateAr(self):
        global current_command  
        current_command = "020F000200020100"
        type_command = "020F000200020100"
        print("def click_regulateAr выполнено")
        self.fn_sendcmd(type_command)
        
    def click_installO(self):
        value_flow = self.lineEdit.text() #значение из TextEdit в строку
        try:
            value_flow = float(value_flow)
            procent = int((value_flow/90)*10000)
            procent1 = hex(procent)
            procent1=str(procent1)
            print("отчивка", procent1)
            if len(procent1) < 6:
                procent2 = "0" + procent1[2:6]
                print(procent2)
            else:
                procent2 = procent1[2:6]
            print("def click_installO выполнено", procent2)
            type_command = "01060004" + procent2
            print(type_command)
            global current_command  
            current_command = type_command
            self.fn_sendcmd(type_command)
        except: 
            self.show_error(value_flow)

    def click_installAr(self):
        value_flow = self.text_givenAr.text() #значение из TextEdit в строку
        try:
            value_flow = float(value_flow)
            procent = int((value_flow/90)*10000*1.45)
            procent1 = hex(procent)
            procent1=str(procent1)
            print("отчивка", procent1)
            if len(procent1) < 6:
                procent2 = "0" + procent1[2:6]
                print(procent2)
            else:
                procent2 = procent1[2:6]
            print("def click_installO выполнено", procent2)
            type_command = "02060004" + procent2
            print(type_command)
            global current_command  
            current_command = type_command
            self.fn_sendcmd(type_command)
        except: 
            self.show_error(value_flow)

    def show_error(self, number): #вывод ошибки 
        error = QMessageBox()
        error.setWindowTitle("Ошибка")
        error.setText('Введено некорректное значение потока ')
        error.setIcon(QMessageBox.Warning)
        error.setStandardButtons(QMessageBox.Ok)
        error.exec()
    
def main():                                                     # открытие главного окна
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())

if __name__ == "__main__": main()
