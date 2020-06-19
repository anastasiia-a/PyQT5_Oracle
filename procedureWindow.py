from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget, QPushButton, QToolTip, QLabel, QComboBox, QLineEdit, QErrorMessage, QMessageBox, QRadioButton, QGroupBox, QVBoxLayout
from PyQt5.QtGui import *
import startWindow
import resultWindow

class procWindow(QWidget):
    def __init__(self, con):
        super().__init__()
        self.con = con
        self.resWindow = resultWindow.resultWindow(self.con)
        self.setGeometry(1500, 400, 900, 500)
        self.setFixedSize(self.size())
        self.setWindowTitle('Выберите процедуру')

        first_btn = QPushButton('Отделы и среднее время их работы над проектами', self)
        first_btn.resize(500, 40)
        first_btn.move(200, 10)
        first_btn.setFont(QFont('Helvetica', 15))
        first_btn.clicked.connect(self.proc1)

        second_btn = QPushButton('Расчет суммы прибыли от завершенных проектов', self)
        second_btn.resize(500, 40)
        second_btn.move(200, 70)
        second_btn.setFont(QFont('Helvetica', 15))
        second_btn.clicked.connect(self.proc2)

        self.l4 = QLabel('Введите начальную дату периода', self)
        self.l4.resize(310, 100)
        self.l4.move(330, 200)
        self.l4.setFont(QFont('Helvetica', 15))
        self.l5 = QLabel('(Формат DD/MM/YYYY)', self)

        self.dd = QLabel('Число', self)
        self.dd.resize(310, 100)
        self.dd.move(300, 230)
        self.dd.setFont(QFont('Helvetica', 14))
        self.dd.hide()

        self.combdd = QComboBox(self)
        self.combdd.resize(100, 80)
        self.combdd.move(275, 280)
        self.combdd.hide()

        self.mm = QLabel('Месяц', self)
        self.mm.resize(310, 100)
        self.mm.move(430, 230)
        self.mm.setFont(QFont('Helvetica', 14))
        self.mm.hide()

        self.combmm = QComboBox(self)
        self.combmm.resize(100, 80)
        self.combmm.move(405, 280)
        self.combmm.hide()


        self.yy = QLabel('Год', self)
        self.yy.resize(310, 100)
        self.yy.move(565, 230)
        self.yy.setFont(QFont('Helvetica', 14))
        self.yy.hide()

        self.combyy = QComboBox(self)
        self.combyy.resize(100, 80)
        self.combyy.move(530, 280)
        self.combyy.hide()

        self.l5.resize(310, 100)
        self.l5.move(380, 240)
        self.l5.setFont(QFont('Helvetica', 13))
        self.l4.hide()
        self.l5.hide()

        self.text = QLineEdit(self)
        self.text.resize(110, 50)
        self.text.move(390, 310)
        self.text.hide()


        third_btn = QPushButton('Самый продолжительный проект выбранного отдела', self)
        third_btn.resize(500, 40)
        third_btn.move(200, 130)
        third_btn.setFont(QFont('Helvetica', 15))

        self.l3 = QLabel('Отдел', self)
        self.l3.resize(300, 50)
        self.l3.move(430, 230)
        self.l3.hide()

        self.box3 = QComboBox(self)
        self.box3.resize(200, 160)
        self.box3.move(350, 200)
        self.box3.hide()
        third_btn.clicked.connect(self.proc3)

        last_btn = QPushButton('Проекты двух выбранных служащих', self)
        last_btn.resize(500, 40)
        last_btn.move(200, 190)
        last_btn.setFont(QFont('Helvetica', 15))
        last_btn.clicked.connect(self.proc4)
        self.l1 = QLabel('Первый', self)
        self.l1.resize(200, 160)
        self.l1.move(330, 180)
        self.l1.hide()

        self.l2 = QLabel('Второй', self)
        self.l2.resize(200, 160)
        self.l2.move(520, 180)
        self.l2.hide()

        self.box1 = QComboBox(self)
        self.box1.resize(200, 160)
        self.box1.move(250, 200)
        self.box1.hide()

        self.box2 = QComboBox(self)
        self.box2.resize(200, 160)
        self.box2.move(450, 200)
        self.box2.hide()

        self.btn_show2 = QPushButton('Посмотреть результат', self)
        self.btn_show2.resize(300, 50)
        self.btn_show2.move(300, 375)
        self.btn_show2.setFont(QFont('Helvetica', 15))

        self.btn_show3 = QPushButton('Посмотреть результат', self)
        self.btn_show3.resize(300, 50)
        self.btn_show3.move(300, 330)
        self.btn_show3.setFont(QFont('Helvetica', 15))

        self.btn_show3.hide()
        self.btn_show2.hide()

        self.btn_show4 = QPushButton('Посмотреть результат', self)
        self.btn_show4.resize(300, 50)
        self.btn_show4.move(300, 330)
        self.btn_show4.setFont(QFont('Helvetica', 15))

        self.btn_show4.hide()

        back_btn = QPushButton('Вернуться на главную страницу', self)
        back_btn.resize(300, 50)
        back_btn.move(300, 440)
        back_btn.setFont(QFont('Helvetica', 15))
        back_btn.clicked.connect(self.backToStart)

    def backToStart(self):
        self.procWindow = startWindow.StartWindow(self.con)
        self.close()

    def proc1(self):
        self.dd.hide()
        self.mm.hide()
        self.yy.hide()
        self.combdd.hide()
        self.combmm.hide()
        self.combyy.hide()
        self.l4.hide()
        self.l5.hide()
        self.text.hide()
        self.btn_show2.hide()
        self.btn_show3.hide()
        self.box3.hide()
        self.l3.hide()
        self.box1.hide()
        self.box2.hide()
        self.l1.hide()
        self.l2.hide()
        self.btn_show4.hide()
        self.showRes1()


    def proc2(self):
        self.btn_show3.hide()
        self.box3.hide()
        self.l3.hide()
        self.box1.hide()
        self.box2.hide()
        self.l1.hide()
        self.l2.hide()
        self.btn_show4.hide()
        self.l4.show()
        self.dd.show()
        self.mm.show()
        self.yy.show()
        self.combdd.show()
        self.combmm.show()
        self.combyy.show()
        self.init_dd()
        self.init_mm()
        self.init_yy()
        self.btn_show2.show()
        self.btn_show2.clicked.connect(self.showRes2)

    def proc3(self):
        self.dd.hide()
        self.mm.hide()
        self.yy.hide()
        self.combdd.hide()
        self.combmm.hide()
        self.combyy.hide()
        self.l4.hide()
        self.l5.hide()
        self.text.hide()
        self.btn_show2.hide()
        self.btn_show4.hide()
        self.box1.hide()
        self.box2.hide()
        self.l1.hide()
        self.l2.hide()
        self.box3.show()
        self.l3.show()
        self.btn_show3.show()
        self.init_box3()
        self.btn_show3.clicked.connect(self.showRes3)

    def proc4(self):
        self.dd.hide()
        self.mm.hide()
        self.yy.hide()
        self.combdd.hide()
        self.combmm.hide()
        self.combyy.hide()
        self.l4.hide()
        self.l5.hide()
        self.text.hide()
        self.btn_show2.hide()
        self.btn_show3.hide()
        self.box3.hide()
        self.l3.hide()
        self.box1.show()
        self.box2.show()
        self.l1.show()
        self.l2.show()
        self.btn_show4.show()
        self.init_box1()
        self.init_box2()
        self.btn_show4.clicked.connect(self.showRes4)

    def init_box1(self):
        cur = self.con.cursor()
        self.box1.clear()
        cur.execute("select id from employees")
        l = cur.fetchall()
        for id in l:
            self.box1.addItem(str(id[0]))

        self.box1.setCurrentIndex(0)

    def init_box2(self):
        cur = self.con.cursor()
        self.box2.clear()
        cur.execute("select id from employees")
        l = cur.fetchall()
        for id in l:
            self.box2.addItem(str(id[0]))

        self.box2.setCurrentIndex(0)

    def init_box3(self):
        cur = self.con.cursor()
        self.box3.clear()
        cur.execute("select id from departments")
        l = cur.fetchall()
        for id in l:
            self.box3.addItem(str(id[0]))

        self.box3.setCurrentIndex(0)

    def init_dd(self):
        self.combdd.clear()
        self.combdd.addItems(['01', '02', '03','04', '05', '06', '07', '08', '09',
                              '10', '11', '12', '13', '14', '15', '16', '17', '18',
                              '19', '20', '21', '22', '23', '24', '25', '26', '27',
                              '28', '29', '30', '31'])

        self.combdd.setCurrentIndex(0)

    def init_mm(self):
        self.combmm.clear()
        self.combmm.addItems(['01', '02', '03', '04', '05', '06', '07', '08', '09',
                              '10', '11', '12'])

        self.combmm.setCurrentIndex(0)

    def init_yy(self):
        self.combyy.clear()
        self.combyy.addItems(['1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007',
                              '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016',
                              '2017', '2018', '2019', '2020'])

        self.combyy.setCurrentIndex(0)

    def showRes1(self):
        self.resWindow.show()
        cur = self.con.cursor()
        try:
            cur.callproc('output_dep')
            self.resWindow.update_table1()
        except:
            print("Неизвестная ошибка!")
            error_d = QMessageBox()
            error_d.setIcon(QMessageBox.Critical)
            error_d.setWindowTitle("Ошибка!")
            error_d.setText("Ошибка вызова процедуры!\nПовторите попытку позднее")
            error_d.exec_()
            return

    def showRes2(self):
        self.resWindow.show()

        cur = self.con.cursor()
        try:
            cur.execute(
                "ALTER SESSION SET NLS_DATE_FORMAT = 'DD-MM-YYYY'"
                " NLS_TIMESTAMP_FORMAT = 'DD-MM-YYYY'")
            str = self.combdd.currentText()+self.combmm.currentText()+self.combyy.currentText()
            self.resWindow.text1 = self.combdd.currentText()
            self.resWindow.text2 = self.combmm.currentText()
            self.resWindow.text3 = self.combyy.currentText()
            cur.callproc('pr_5', [str])
            self.resWindow.update_table2()
        except:
            print("Неизвестная ошибка!")
            error_d = QMessageBox()
            error_d.setIcon(QMessageBox.Critical)
            error_d.setWindowTitle("Ошибка!")
            error_d.setText("Ошибка вызова процедуры!\nПовторите попытку позднее")
            error_d.exec_()
            return

    def showRes3(self):
        self.resWindow.show()
        cur = self.con.cursor()
        try:
            cur.callproc('pr_3', [int(self.box3.currentText())])

            self.resWindow.text1 = (self.box3.currentText())
            self.resWindow.update_table3()
        except:
            print("Неизвестная ошибка!")
            error_d = QMessageBox()
            error_d.setIcon(QMessageBox.Critical)
            error_d.setWindowTitle("Ошибка!")
            error_d.setText("Ошибка вызова процедуры!\nПовторите попытку позднее")
            error_d.exec_()
            return

    def showRes4(self):
        self.resWindow.show()
        cur = self.con.cursor()
        try:
            cur.callproc('proj2', [int(self.box1.currentText()), int(self.box2.currentText())])

            self.resWindow.text1 = (self.box1.currentText())
            self.resWindow.text2 = (self.box2.currentText())

            self.resWindow.update_table4()
        except:
            print("Неизвестная ошибка!")
            error_d = QMessageBox()
            error_d.setIcon(QMessageBox.Critical)
            error_d.setWindowTitle("Ошибка!")
            error_d.setText("Ошибка вызова процедуры!\nПовторите попытку позднее")
            error_d.exec_()
            return