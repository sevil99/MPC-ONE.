import random
import sys
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import settings
from typing import List, Optional


def show_error():
    """
    Вывод ошибок
    """
    error = QMessageBox()
    error.setWindowTitle("Ошибка")
    error.setText('Введено некорректное значение потока ')
    error.setIcon(QMessageBox.Warning)
    error.setStandardButtons(QMessageBox.Ok)
    error.exec()


class UICustom:
    widget = None

    def __init__(self, widget: QtWidgets.QWidget):
        UICustom.set_widget(widget)

    @staticmethod
    def set_widget(widget: QtWidgets.QWidget):
        UICustom.widget = widget

    class UITabWidget:
        """
        Класс табов
        """

        @staticmethod
        def create(size: List[int],
                   name: str):
            tab = QtWidgets.QTabWidget(UICustom.widget)
            if len(size) != 4:
                raise Exception("Передан список размера окна не с 4 параметрами")
            tab.setGeometry(QtCore.QRect(*size))
            tab.setMinimumSize(QtCore.QSize(200, 200))
            tab.setMaximumSize(QtCore.QSize(1920, 400))
            tab.setFont(QtGui.QFont(settings.default_font, pointSize=20))
            tab.setObjectName(name)
            return tab

    class UILabel:
        """
        Класс текстового поля со статическими методами для настройки
        """

        @staticmethod
        def create(text: Optional[str],
                   size: List[int],
                   name: Optional[str] = None,
                   color: List[int] = None,
                   font_size: int = 13):
            if color is None:
                color = [111, 111, 111]
            label = QtWidgets.QLabel(UICustom.widget)
            label.setGeometry(QtCore.QRect(*size))
            label.setFont(QtGui.QFont(settings.default_font, pointSize=font_size))
            label.setStyleSheet(f"background-color: rgb({color[0]}, {color[1]}, {color[2]});")
            label.setObjectName(name)
            label.setText(text)
            return label

    class UIButton:
        """
        Класс кнопки
        """
        @staticmethod
        def create(text: Optional[str],
                   size: List[int],
                   name: Optional[str] = None):
            pass


class UIMainWindow:
    """
    Класс главного окна с тремя виджитами - Кислород, Ar и монитор
    """

    def __init__(self):
        self.default_font = settings.default_font
        self.main_window = QtWidgets.QMainWindow()
        self.main_window.setObjectName("MainWindow")
        self.main_window.setFixedSize(640, 250)
        self.main_window.setStyleSheet("background-color: rgb(255, 255, 255);")
        ui = UICustom(self.main_window)
        self.tab_base = ui.UITabWidget.create([0, 0, 640, 250], "tabWidget")
        self.tab_oxygen = ui.UITabWidget.create([0, 0, 0, 305], "tab_oxygen")

        ui.set_widget(self.tab_oxygen)

        self.label_2 = ui.UILabel.create("Поток 0", [0, 0, 300, 100], "label_2", [111] * 3, 20)
        self.label_realflowO = ui.UILabel.create("0.00", [140, 10, 151, 71], "label_realflowO", [111] * 3, 20)
        self.label_6 = ui.UILabel.create("Поток 0", [310, 0, 320, 100], font_size=20)
        self.label_10 = ui.UILabel.create("Реальный", [10, 65, 91, 21])
        self.label_11 = ui.UILabel.create("Заданный", [325, 65, 91, 21])
        # Степени
        self.label_7 = ui.UILabel.create("2", [425, 50, 16, 20])
        self.label = ui.UILabel.create("2", [100, 150, 16, 20])
        self.label_3 = ui.UILabel.create("2", [270, 150, 16, 20])
        self.label_5 = ui.UILabel.create("2", [95, 50, 16, 20])
        self.label_4 = ui.UILabel.create("2", [450, 150, 16, 20])
        self.label_9 = ui.UILabel.create("2", [620, 155, 10, 20])

        self.btn_closeO = QtWidgets.QPushButton(self.tab_oxygen)
        self.btn_closeO.setGeometry(QtCore.QRect(150, 100, 150, 100))
        self.btn_closeO.setFont(QtGui.QFont(self.default_font, pointSize=13))
        self.btn_closeO.setStyleSheet("background-color: rgb(111, 111, 111);")
        self.btn_closeO.setObjectName("btn_closeO")

        self.btn_openO = QtWidgets.QPushButton(self.tab_oxygen)
        self.btn_openO.setGeometry(QtCore.QRect(0, 100, 150, 100))
        self.btn_openO.setStyleSheet("background-color: rgb(111, 111, 111);")
        self.btn_openO.setObjectName("btn_openO")

        self.btn_regulateO = QtWidgets.QPushButton(self.tab_oxygen)
        self.btn_regulateO.setGeometry(QtCore.QRect(470, 100, 160, 100))
        self.btn_regulateO.setFont(QtGui.QFont(self.default_font, pointSize=15))
        self.btn_regulateO.setStyleSheet("background-color: rgb(111, 111, 111);")
        self.btn_regulateO.setObjectName("btn_regulateO")

        self.btn_installO = QtWidgets.QPushButton(self.tab_oxygen)
        self.btn_installO.setGeometry(QtCore.QRect(310, 100, 160, 100))
        self.btn_installO.setFont(QtGui.QFont(self.default_font, pointSize=15))
        self.btn_installO.setStyleSheet("background-color: rgb(111, 111, 111);")
        self.btn_installO.setObjectName("btn_installO")

        self.lineEdit = QtWidgets.QLineEdit(self.tab_oxygen)
        self.lineEdit.setGeometry(QtCore.QRect(440, 10, 151, 71))
        self.lineEdit.setFont(QtGui.QFont(self.default_font, pointSize=20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")

        self.tab_base.addTab(self.tab_oxygen, "")

        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")

        self.btn_installAr = QtWidgets.QPushButton(self.tab_4)
        self.btn_installAr.setGeometry(QtCore.QRect(310, 100, 161, 100))
        self.btn_installAr.setFont(QtGui.QFont(self.default_font, pointSize=15))
        self.btn_installAr.setStyleSheet("background-color: rgb(111, 111, 111);")
        self.btn_installAr.setObjectName("btn_installAr")

        self.btn_closeAr = QtWidgets.QPushButton(self.tab_4)
        self.btn_closeAr.setGeometry(QtCore.QRect(150, 100, 150, 100))
        self.btn_closeAr.setFont(QtGui.QFont(self.default_font, pointSize=15))
        self.btn_closeAr.setStyleSheet("background-color: rgb(111, 111, 111);")
        self.btn_closeAr.setObjectName("btn_closeAr")

        self.btn_regulateAr = QtWidgets.QPushButton(self.tab_4)
        self.btn_regulateAr.setGeometry(QtCore.QRect(470, 100, 161, 100))
        self.btn_regulateAr.setFont(QtGui.QFont(self.default_font, pointSize=15))
        self.btn_regulateAr.setStyleSheet("background-color: rgb(111, 111, 111);")
        self.btn_regulateAr.setObjectName("btn_regulateAr")

        self.label_realflowAr = QtWidgets.QLabel(self.tab_4)
        self.label_realflowAr.setGeometry(QtCore.QRect(140, 10, 151, 71))
        self.label_realflowAr.setFont(QtGui.QFont(self.default_font, pointSize=20))
        self.label_realflowAr.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_realflowAr.setObjectName("label_realflowAr")

        self.label_1 = QtWidgets.QLabel(self.tab_4)
        self.label_1.setGeometry(QtCore.QRect(0, 0, 300, 100))
        self.label_1.setFont(QtGui.QFont(self.default_font, pointSize=20))
        self.label_1.setStyleSheet("background-color: rgb(111, 111, 111);")
        self.label_1.setObjectName("label_1")

        self.label_8 = QtWidgets.QLabel(self.tab_4)
        self.label_8.setGeometry(QtCore.QRect(310, 0, 321, 100))
        self.label_8.setFont(QtGui.QFont(self.default_font, pointSize=20))
        self.label_8.setStyleSheet("background-color: rgb(111, 111, 111);")
        self.label_8.setObjectName("label_8")

        self.btn_openAr = QtWidgets.QPushButton(self.tab_4)
        self.btn_openAr.setGeometry(QtCore.QRect(0, 100, 150, 100))
        self.btn_openAr.setFont(QtGui.QFont(self.default_font, pointSize=15))
        self.btn_openAr.setStyleSheet("background-color: rgb(111, 111, 111);")
        self.btn_openAr.setObjectName("btn_openAr")

        self.text_givenAr = QtWidgets.QLineEdit(self.tab_4)
        self.text_givenAr.setGeometry(QtCore.QRect(440, 10, 151, 71))
        self.text_givenAr.setFont(QtGui.QFont(self.default_font, pointSize=20))
        self.text_givenAr.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.text_givenAr.setObjectName("text_givenAr")

        self.label_12 = QtWidgets.QLabel(self.tab_4)
        self.label_12.setGeometry(QtCore.QRect(10, 65, 91, 21))
        self.label_12.setStyleSheet("background-color: rgb(111, 111,111);")
        self.label_12.setObjectName("label_12")

        self.label_13 = QtWidgets.QLabel(self.tab_4)
        self.label_13.setGeometry(QtCore.QRect(325, 65, 91, 21))
        self.label_13.setStyleSheet("background-color: rgb(111, 111,111);")
        self.label_13.setObjectName("label_13")

        self.btn_installO.raise_()
        self.btn_regulateO.raise_()
        self.btn_openO.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.btn_closeO.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        self.label_realflowO.raise_()
        self.label_5.raise_()
        self.label_4.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.lineEdit.raise_()
        self.label_11.raise_()
        self.label_1.raise_()
        self.btn_installAr.raise_()
        self.btn_closeAr.raise_()
        self.btn_regulateAr.raise_()
        self.label_realflowAr.raise_()
        self.label_8.raise_()
        self.btn_openAr.raise_()
        self.text_givenAr.raise_()
        self.label_12.raise_()
        self.label_13.raise_()

        self.tab_base.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tab_base.addTab(self.tab_5, "")
        self.main_window.setCentralWidget(self.tab_base)

        self.retranslate_data()

        self.tab_base.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self.main_window)
        event_button = {
            self.btn_openO: self.click_open0,
            self.btn_closeO: self.click_closeO,
            self.btn_openAr: self.click_openAr,
            self.btn_closeAr: self.click_closeAr,
            self.btn_regulateO: self.click_regulateO,
            self.btn_regulateAr: self.click_regulateAr,
            self.btn_installO: self.click_installO,
            self.btn_installAr: self.click_installAr,

        }
        for btn, func in event_button.items():
            btn.clicked.connect(func)

    def retranslate_data(self):
        _translate = QtCore.QCoreApplication.translate
        self.main_window.setWindowTitle(_translate("MainWindow", "MPC ONE"))
        self.btn_closeO.setText(_translate("MainWindow", "Закрыть O"))
        self.btn_openO.setText(_translate("MainWindow", "Открыть O"))
        self.btn_regulateO.setText(_translate("MainWindow", "Регулировать O"))
        self.btn_installO.setText(_translate("MainWindow", "Установить О"))
        self.tab_base.setTabText(self.tab_base.indexOf(self.tab_oxygen), _translate("MainWindow", "O2"))
        self.btn_installAr.setText(_translate("MainWindow", "Установить Ar"))
        self.btn_closeAr.setText(_translate("MainWindow", "Закрыть Ar"))
        self.btn_regulateAr.setText(_translate("MainWindow", "Регулировать Ar"))
        self.label_realflowAr.setText(_translate("MainWindow", "0.00"))
        self.label_1.setText(_translate("MainWindow", "Поток Ar"))
        self.label_8.setText(_translate("MainWindow", "Поток Ar"))
        self.btn_openAr.setText(_translate("MainWindow", "Открыть Ar"))
        self.label_12.setText(_translate("MainWindow", "Реальный"))
        self.label_13.setText(_translate("MainWindow", "Заданный"))
        self.tab_base.setTabText(self.tab_base.indexOf(self.tab_4), _translate("MainWindow", "Ar"))
        self.tab_base.setTabText(self.tab_base.indexOf(self.tab_5), _translate("MainWindow", "Блок питания"))

    def fn_sendcmd(self, number):  # извлекаем содержимое ячеек
        print("def fn_sendcmd получило значение - ", number)  # данные
        self.ed_id = number[0:2]  # адрес устройства ID
        print(self.ed_id)
        self.ed_cmd = number[2:4]  # номер команды
        print(self.ed_cmd)
        self.ed_adr = number[4:8]  # адрес регистра
        print(self.ed_adr)
        self.ed_count = number[8:17]  # данные
        print(self.ed_count)
        # self.ed_count=str(hex(4000))[2:len(str(hex(4000)))]

    def click_open0(self):
        type_command = "010F000200020101"
        print("def click_openO выполнено")
        self.fn_sendcmd(type_command)

    def click_openAr(self):
        type_command = "020F000200020101"
        print("def click_openAr выполнено")
        self.fn_sendcmd(type_command)

    def click_closeO(self):
        type_command = "010F000200020102"
        print("def click_closeO выполнено")
        self.fn_sendcmd(type_command)

    def click_closeAr(self):
        type_command = "020F000200020102"
        print("def click_closeAr выполнено")
        self.fn_sendcmd(type_command)

    def click_regulateO(self):
        type_command = "010F000200020100"
        print("def click_regulateO выполнено")
        self.fn_sendcmd(type_command)

    def click_regulateAr(self):
        type_command = "020F000200020100"
        print("def click_regulateAr выполнено")
        self.output()  # !!!!!!!!!!!! # это неправильная функция, с помощью нее я пытался понять, почему не записываются нормально значения в Lable

    def click_installO(self):
        value_flow = self.lineEdit.text()  # значение из TextEdit в строку
        if value_flow.isnumeric():
            value_flow = int(value_flow)
            procent = int((value_flow / 90) * 10000)
            procent1 = hex(procent)
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
            self.fn_sendcmd(type_command)
        else:
            show_error(value_flow)

    def click_installAr(self):
        value_flow = self.text_givenAr.text()  # значение из TextEdit в строку
        if value_flow.isnumeric():
            value_flow = int(value_flow)
            procent = int((value_flow / 90) * 10000 * 1.45)
            procent1 = hex(procent)
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
            self.fn_sendcmd(type_command)
        else:
            show_error(value_flow)

    def output(self):
        """
        Отладочная функция переодической записи в Lable
        """
        for i in range(10):
            a = random.randint(0, 10)
            self.label_realflowAr.setText(str(a))
            print(a)


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UIMainWindow()
    ui.main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
