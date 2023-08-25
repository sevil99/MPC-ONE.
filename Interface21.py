import sys
import random
import threading
from time import sleep
from multiprocessing import Process
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication, QBasicTimer, QDateTime, Qt, QSize, QTimer, QThread
import Interface
from DialWind import Ui_Dialog


class RegulWindow(QDialog, Ui_Dialog):
    def __init__(self, root):
        QDialog.__init__(self, root)
        self.setupUi(self)
        self.MainWindow = root
        self.pushButton_13.clicked.connect(self.acept_data)
        self.pushButton_14.clicked.connect(self.reject_data)

        self.pushButton_1.clicked.connect(lambda: self.add_text("1"))
        self.pushButton_2.clicked.connect(lambda: self.add_text("2"))
        self.pushButton_3.clicked.connect(lambda: self.add_text("3"))
        self.pushButton_4.clicked.connect(lambda: self.add_text("4"))
        self.pushButton_5.clicked.connect(lambda: self.add_text("5"))
        self.pushButton_6.clicked.connect(lambda: self.add_text("6"))
        self.pushButton_7.clicked.connect(lambda: self.add_text("7"))
        self.pushButton_8.clicked.connect(lambda: self.add_text("8"))
        self.pushButton_9.clicked.connect(lambda: self.add_text("9"))
        self.pushButton_10.clicked.connect(lambda: self.add_text("0"))
        self.pushButton_11.clicked.connect(lambda: self.add_text("."))
        self.pushButton_12.clicked.connect(self.clear_text)

    def add_text(self, text):
        current_text = self.label_value_flow_Ar.text()
        self.label_value_flow_Ar.setText(current_text + text)

    def clear_text(self):
        self.label_value_flow_Ar.setText("")

    def acept_data(self):
        self.MainWindow.fakeLineEditO.setText(self.label_value_flow_Ar.text())
        self.close()

    def reject_data(self):
        print('команда сработала')
        self.close()


class RegulWindow2(QDialog, Ui_Dialog):
    def __init__(self, root):
        QDialog.__init__(self, root)
        self.setupUi(self)
        self.MainWindow = root
        self.pushButton_13.clicked.connect(self.acept_data)
        self.pushButton_14.clicked.connect(self.reject_data)

        self.pushButton_1.clicked.connect(lambda: self.add_text("1"))
        self.pushButton_2.clicked.connect(lambda: self.add_text("2"))
        self.pushButton_3.clicked.connect(lambda: self.add_text("3"))
        self.pushButton_4.clicked.connect(lambda: self.add_text("4"))
        self.pushButton_5.clicked.connect(lambda: self.add_text("5"))
        self.pushButton_6.clicked.connect(lambda: self.add_text("6"))
        self.pushButton_7.clicked.connect(lambda: self.add_text("7"))
        self.pushButton_8.clicked.connect(lambda: self.add_text("8"))
        self.pushButton_9.clicked.connect(lambda: self.add_text("9"))
        self.pushButton_10.clicked.connect(lambda: self.add_text("0"))
        self.pushButton_11.clicked.connect(lambda: self.add_text("."))
        self.pushButton_12.clicked.connect(self.clear_text)

    def add_text(self, text):
        current_text = self.label_value_flow_Ar.text()
        self.label_value_flow_Ar.setText(current_text + text)

    def clear_text(self):
        self.label_value_flow_Ar.setText("")

    def acept_data(self):
        self.MainWindow.fakeLineEditO_2.setText(self.label_value_flow_Ar.text())
        self.close()

    def reject_data(self):
        self.close()


def click_openAr():
    global current_command
    current_command = "020F000200020101"
    print("def click_openAr выполнено")


class MainWindow(QMainWindow, Interface.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.flow_value = ' '

        self.btn_openO.clicked.connect(self.thread_openO)  # функции нажатия на кнопки
        self.btn_openAr.clicked.connect(click_openAr)
        self.btn_closeO.clicked.connect(self.click_closeO)
        self.btn_closeAr.clicked.connect(self.click_closeAr)
        self.btn_regulateO.clicked.connect(self.click_regulateO)
        self.btn_regulateAr.clicked.connect(self.click_regulateAr)
        self.btn_installO.clicked.connect(self.click_installO)
        self.btn_installAr.clicked.connect(self.click_installAr)
        self.fakeButtonO.clicked.connect(self.show_keyboard_dialogO)
        self.fakeButtonO_2.clicked.connect(self.show_keyboard_dialogAr)
        self.pushButton.clicked.connect(self.Exit_)  # клик на кнопку ВЫХОД

        # GPIO.setmode(GPIO.BCM)                                  # Инициализация пина RPi - Master (используется при MAX485)
        # GPIO.setup(DU_Pin_Rpi_Master, GPIO.OUT)
        # GPIO.output(DU_Pin_Rpi_Master, True)
        # self.setGeometry(0, 70, 1024, 600)                        # расположение главновго окна
        self.setWindowFlags(Qt.FramelessWindowHint)  # убирает шапку приложения
        # icon_switch_off = QtGui.QIcon()                         # картинка на кнопке ВЫХОД
        # icon_switch_off.addPixmap(QtGui.QPixmap("/home/pi/Desktop/Modbus/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.Exit.setIcon(icon_switch_off)                      # добавляет иконку

    def Exit_(self):  # при выходе из программы
        global current_command
        current_command = 'Exit'

    def show_keyboard_dialogO(self):
        dialog = RegulWindow(self)
        dialog.show()
        dialog.exec()

    def show_keyboard_dialogAr(self):
        dialog = RegulWindow2(self)
        dialog.show()
        dialog.exec()

    def showEvent(self, event):  # запускает программу при при её открытии
        global current_command
        print('Продукт Vasiliev&Vasiliev Embedded Software Technology. Все права защищены')
        current_command = '010300040002'
        self.check_o()

    def check_o(self):
        global current_command
        if current_command == 'Exit':
            sleep(2)
            self.close()
            return None
        cmd_show_oxygen = '010300040002'
        if current_command != cmd_show_oxygen and current_command != 'Exit':
            print('модуль получил глобальную команду')
            thread = threading.Thread(target=self.fn_sendcmd, args=(current_command,))
            thread.start()
            thread.join()
            current_command = cmd_show_oxygen
        else:
            print('modul 1 made/ ')
            thread = threading.Thread(target=self.fn_sendcmd, args=(cmd_show_oxygen,))
            thread.start()
            thread.join()
            self.updatelabeltextO(self.flow_value)

        timer = threading.Timer(0.5, self.check_ar, args=(str,))
        timer.start()

    def check_ar(self):
        a = '020300040002'
        print('modul 2 made /')
        thread = threading.Thread(target=self.fn_sendcmd, args=(a,))
        thread.start()
        thread.join()
        self.updatelabeltextAr(self.flow_value)
        self.check_o()

    def updatelabeltextAr(self, str_num):
        str_num = str(round(str_num / 1.45, 2))
        self.label_realflowAr.setText(str_num)

    def updatelabeltextO(self, str_num):
        str_num = str(round(str_num, 2))
        self.label_realflowO.setText(str_num)

    def fn_sendcmd(self, number):  # извлекаем содержимое ячеек
        print("def fn_sendcmd получило значение - ", number)  # данные
        ed_id = number[0:2]  # адрес устройства ID
        ed_cmd = number[2:4]  # номер команды
        ed_adr = number[4:8]  # адрес регистра
        ed_count = number[8:17]  # данные
        self.flow_value = random.randint(0, 100)
        sleep(1)

    def click_openO(self):
        global current_command
        current_command = "010F000200020101"
        print("def click_openO выполнено")
        for i in range(1_000_000):
            print(i)

    def thread_openO(self):
        t1 = threading.Thread(target=self.click_openO)
        t1.start()

    @staticmethod
    def click_closeO():
        global current_command
        current_command = "010F000200020102"
        print("def click_closeO выполнено")

    def click_closeAr(self):
        global current_command
        current_command = "020F000200020102"
        print("def click_closeAr выполнено")

    def click_regulateO(self):
        global current_command
        current_command = "010F000200020100"
        print("def click_regulateO выполнено")

    def click_regulateAr(self):
        global current_command
        current_command = "020F000200020100"
        print("def click_regulateAr выполнено")

    def click_installO(self):
        value_flow_1 = self.fakeLineEditO.text()  # значение из TextEdit в строку
        try:  # TODO: Слишком много строк, где можно завалиться. Надо уменьшить try, а лучше от него избавиться
            value_flow_1 = float(value_flow_1)
            procent = int((value_flow_1 / 90) * 10000 * 1.45)
            procent1 = hex(procent)
            if value_flow_1 > 90:
                self.show_error("Значение должно быть не больше 90 л/с")
            else:
                procent1 = str(procent1)
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
        except:
            self.show_error('Введено некорректное значение потока')

    def click_installAr(self):
        value_flow_1 = self.fakeLineEditO_2.text()  # значение из TextEdit в строку
        try:
            value_flow_1 = float(value_flow_1)
            procent = int((value_flow_1 / 90) * 10000 * 1.45)
            procent1 = hex(procent)
            if value_flow_1 > 90:
                self.show_error("Значение должно быть не больше 90 л/с")
                procent1 = str(procent1)
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
        except:
            self.show_error('Введено некорректное значение потока')

    def show_error(self, str):  # вывод ошибки
        error = QMessageBox()
        error.setWindowTitle("Ошибка")
        error.setText(str)
        error.setIcon(QMessageBox.Warning)
        error.setStandardButtons(QMessageBox.Ok)
        error.exec()


def main():  # открытие главного окна
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())


if __name__ == "__main__": main()
