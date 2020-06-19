from PyQt5 import QtCore
from PyQt5.QtWidgets import QTableWidget, QApplication, QGridLayout, QWidget, QPushButton, QToolTip, QLabel, QComboBox, QLineEdit, QErrorMessage, QMessageBox, QRadioButton, QGroupBox, QVBoxLayout, QTableWidgetItem
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
import startWindow
from datetime import date

class resultWindow(QWidget):
    def __init__(self, con):
        super().__init__()
        self.con = con
        self.setGeometry(1500, 400, 900, 500)
        self.setFixedSize(self.size())
        self.setWindowTitle('Результат')
        self.text1 = ''
        self.text2 = ''
        self.text3 = ''

        self.third1_btn = QPushButton('Записать в файл', self)
        self.third1_btn.resize(500, 40)
        self.third1_btn.move(200, 450)
        self.third1_btn.setFont(QFont('Helvetica', 15))

        self.third2_btn = QPushButton('Записать в файл', self)
        self.third2_btn.resize(500, 40)
        self.third2_btn.move(200, 450)
        self.third2_btn.setFont(QFont('Helvetica', 15))

        self.third3_btn = QPushButton('Записать в файл', self)
        self.third3_btn.resize(500, 40)
        self.third3_btn.move(200, 450)
        self.third3_btn.setFont(QFont('Helvetica', 15))

        self.third4_btn = QPushButton('Записать в файл', self)
        self.third4_btn.resize(500, 40)
        self.third4_btn.move(200, 450)
        self.third4_btn.setFont(QFont('Helvetica', 15))



    def update_table1(self):
        self.table = QTableWidget(self)
        self.table.setColumnCount(2)
        self.table.resize(520, 450)
        self.table.move(185, 0)
        self.third2_btn.hide()
        self.third3_btn.hide()
        self.third4_btn.hide()
        cur = self.con.cursor()
        try:
            cur.execute('select count(*) from output_d')
            self.N_ROWS = cur.fetchone()[0]
            self.table.setRowCount(self.N_ROWS)
            self.table.setColumnWidth(0, 250)
            self.table.setColumnWidth(1,250)
            self.table.setHorizontalHeaderLabels(['Название отдела', 'Среднее время работы (в месяцах)'])
            cur.execute("select * from output_d")

            self.l = cur.fetchall()
            ll = []
            for el in self.l:
                ll.append(list(el))
            for i in range(0, self.N_ROWS):
                for j in range(0, 2):
                    if j == 1 & (str(ll[i][j]) != 'None'):
                        self.table.setItem(i, j, QTableWidgetItem(str(round(float(ll[i][j]), 1))))
                    else:
                        self.table.setItem(i, j, QTableWidgetItem(str(ll[i][j])))

            self.table.show()
            self.third1_btn.show()
            self.third1_btn.clicked.connect(self.click1)

        except:
            print("Неизвестная ошибка!")
            error_d = QMessageBox()
            error_d.setIcon(QMessageBox.Critical)
            error_d.setWindowTitle("Ошибка!")
            error_d.setText("Ошибка Загрузки данных!\nПовторите попытку позднее")
            error_d.exec_()
            return

    def update_table2(self):
        self.table = QTableWidget(self)
        self.table.setColumnCount(1)
        self.table.resize(520, 450)
        self.table.move(185, 0)
        self.third1_btn.hide()
        self.third3_btn.hide()
        self.third4_btn.hide()
        cur = self.con.cursor()
        try:
            cur.execute('select count(*) from table_pr5')
            self.N_ROWS = cur.fetchone()[0]
            self.table.setRowCount(self.N_ROWS)
            self.table.setColumnWidth(0, 500)
            print(self.text1)
            self.table.setHorizontalHeaderLabels(["Прибыль с '{}'".format(self.text1+'/'+(self.text2)+'/'+self.text3)])
            cur.execute("select * from table_pr5")

            self.l = cur.fetchall()
            ll = []
            for el in self.l:
                ll.append(list(el))
            for i in range(0, self.N_ROWS):
                for j in range(0, 1):
                    self.table.setItem(i, j, QTableWidgetItem(str(round(float(ll[i][j]), 1))))

            self.table.show()
            self.third2_btn.show()
            self.third2_btn.clicked.connect(self.click2)
        except:
            print("Неизвестная ошибка!")
            error_d = QMessageBox()
            error_d.setIcon(QMessageBox.Critical)
            error_d.setWindowTitle("Ошибка!")
            error_d.setText("Ошибка Загрузки данных!\nПовторите попытку позднее")
            error_d.exec_()
            return

    def update_table3(self):

        self.table = QTableWidget(self)
        self.table.setColumnCount(2)
        self.table.resize(520, 450)
        self.table.move(185, 0)
        self.third2_btn.hide()
        self.third1_btn.hide()
        self.third4_btn.hide()
        cur = self.con.cursor()
        try:
            cur.execute('select count(*) from table_pr3')

            self.N_ROWS = cur.fetchone()[0]
            self.table.setRowCount(self.N_ROWS)
            self.table.setHorizontalHeaderLabels(["Самый продолжительный проект отдела №'{}'".format(self.text1), 'Время (в месяцах)'])
            cur.execute("select * from table_pr3")
            self.table.setColumnWidth(0, 320)
            self.table.setColumnWidth(1, 190)

            self.l = cur.fetchall()
            ll = []
            for el in self.l:
                ll.append(list(el))
            for i in range(0, self.N_ROWS):
                for j in range(0, 2):
                    if j == 1 & (str(ll[i][j]) != 'None'):
                        self.table.setItem(i, j, QTableWidgetItem(str(round(float(ll[i][j]), 1))))
                    else:
                        self.table.setItem(i, j, QTableWidgetItem(str(ll[i][j])))

            self.table.show()
            self.third3_btn.show()
            self.third3_btn.clicked.connect(self.click3)

        except:
            print("Неизвестная ошибка!")
            error_d = QMessageBox()
            error_d.setIcon(QMessageBox.Critical)
            error_d.setWindowTitle("Ошибка!")
            error_d.setText("Ошибка Загрузки данных!\nПовторите попытку позднее")
            error_d.exec_()
            return

    def update_table4(self):
        self.table = QTableWidget(self)
        self.table.setColumnCount(1)
        self.table.resize(520, 450)
        self.table.move(185, 0)
        self.third2_btn.hide()
        self.third3_btn.hide()
        self.third1_btn.hide()
        cur = self.con.cursor()
        try:
            cur.execute('select count(*) from outp')

            self.N_ROWS = cur.fetchone()[0]
            self.table.setRowCount(self.N_ROWS)
            self.table.setHorizontalHeaderLabels(["Совместные проекты служащих №'{}' и №'{}'".format(self.text1, self.text2)])
            cur.execute("select * from outp")
            self.table.setColumnWidth(0, 500)

            self.l = cur.fetchall()
            ll = []
            for el in self.l:
                ll.append(list(el))
            for i in range(0, self.N_ROWS):
                for j in range(0, 1):
                    self.table.setItem(i, j, QTableWidgetItem(str(ll[i][j])))

            self.table.show()
            self.third4_btn.show()
            self.third4_btn.clicked.connect(self.click4)
        except:
            print("Неизвестная ошибка!")
            error_d = QMessageBox()
            error_d.setIcon(QMessageBox.Critical)
            error_d.setWindowTitle("Ошибка!")
            error_d.setText("Ошибка Загрузки данных!\nПовторите попытку позднее")
            error_d.exec_()
            return

    def click1(self):
        f = open('1.txt', 'w')
        for id in self.l:
            f.writelines(str(id))
            f.write('\n')
        f.close()

    def click2(self):
        f = open('2.txt', 'w')
        f.write("Прибыль с '{}'".format(self.text1+'/'+(self.text2)+'/'+self.text3))
        f.write('\n')
        for id in self.l:
            f.writelines(str(id))
            f.write('\n')
        f.close()

    def click3(self):
        f = open('3.txt', 'w')
        f.write("Самый продолжительный проект отдела №'{}'".format(self.text1))
        f.write('\n')
        for id in self.l:
            f.writelines(str(id))
            f.write('\n')
        f.close()

    def click4(self):
        f = open('4.txt', 'w')
        f.write("Совместные проекты служащих №'{}' и №'{}'".format(self.text1, self.text2))
        f.write('\n')
        for id in self.l:
            f.writelines(str(id))
            f.write('\n')
        f.close()
