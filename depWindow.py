from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QComboBox, QLineEdit, QTableWidget, QTableWidgetItem, \
    QMessageBox
from PyQt5.QtGui import *


class depWindow(QWidget):
    def __init__(self, con):
        super().__init__()
        self.con = con
        self.setGeometry(1500, 400, 900, 500)
        self.setFixedSize(self.size())
        self.setWindowTitle('Отделы')

        self.add_btn = QPushButton('Добавить', self)
        self.add_btn.move(20, 460)
        self.add_btn.resize(150, 30)
        self.add_btn.clicked.connect(self.add_clicked)

        self.delete_btn = QPushButton('Удалить', self)
        self.delete_btn.move(360, 460)
        self.delete_btn.resize(150, 30)
        self.delete_btn.clicked.connect(self.delete_clicked)

        self.title_label = QLabel('', self)
        self.title_label.move(630, 30)
        self.title_label.setFont(QFont('Helvetica', 18))


        self.dep_label = QLabel('Отдел', self)
        self.dep_label.move(570, 100)

        self.emp_label = QLabel('Cотрудник', self)
        self.emp_label.move(570, 150)

        self.dep_id_label = QLabel('Отдел', self)
        self.dep_id_label.move(570, 300)

        self.dep_name_label = QLabel('Название', self)
        self.dep_name_label.move(570, 350)


        self.dep_id_combobox = QComboBox(self)
        self.dep_id_combobox.move(675, 100)
        self.dep_id_combobox.resize(163, 20)
        self.dep_id_combobox.currentIndexChanged.connect(self.id_changed)

        self.emp_id_combobox = QComboBox(self)
        self.emp_id_combobox.move(675, 150)
        self.emp_id_combobox.resize(163, 20)
        self.emp_id_combobox.currentIndexChanged.connect(self.id_changed)


        self.dep_id_edit = QLineEdit(self)
        self.dep_id_edit.move(680, 300)
        self.dep_id_edit.resize(150, 20)

        self.dep_name_edit = QLineEdit(self)
        self.dep_name_edit.move(680, 350)
        self.dep_name_edit.resize(150, 20)


        self.apply_btn1 = QPushButton('', self)
        self.apply_btn1.move(670, 200)
        self.apply_btn1.resize(165, 30)
        self.apply_btn1.clicked.connect(self.apply1_clicked)

        self.apply_btn2 = QPushButton('', self)
        self.apply_btn2.move(670, 400)
        self.apply_btn2.resize(165, 30)
        self.apply_btn2.clicked.connect(self.apply2_clicked)

        self.commit_btn = QPushButton('Сохранить', self)
        self.commit_btn.move(570, 460)
        self.commit_btn.resize(150, 30)
        self.commit_btn.clicked.connect(self.commit_clicked)

        self.rollback_btn = QPushButton('Отменить', self)
        self.rollback_btn.move(740, 460)
        self.rollback_btn.resize(150, 30)
        self.rollback_btn.clicked.connect(self.rollback_clicked)

        self.table = QTableWidget(self)
        self.table.setColumnCount(5)
        self.table.resize(520, 450)
        self.table.setColumnWidth(0, 50)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 70)
        self.table.setColumnWidth(3, 110)
        self.table.setColumnWidth(4, 115)
        self.update_table()
        self.update_dep_combobox()
        self.update_emp_combobox()
        self.hide_all()

    def add_emp(self):
        try:
            cur = self.con.cursor()
            query =r"INSERT INTO Departments_employees (department_id, employee_id) " \
                   r"VALUES ({}, {})".format(self.dep_id_combobox.currentText().split()[0],
                                              self.emp_id_combobox.currentText().split()[0])

            cur.execute(query)
            self.update_table()
            self.clear_all()
        except:
            error_d = QMessageBox()
            error_d.setIcon(QMessageBox.Critical)
            error_d.setWindowTitle("Ошибка!")
            error_d.setWindowTitle("Похоже сотрудник уже состоит в отделе!")
            error_d.exec_()

    def add_dep(self):
        try:
            curs = self.con.cursor()
            query =r"INSERT INTO Departments(name) " \
                   r"VALUES ('{}')".format(self.dep_name_edit.text())
            curs.execute(query)
            self.update_table()
            self.clear_all()

        except:
            # print(query)
            error_d = QMessageBox()
            error_d.setIcon(QMessageBox.Critical)
            error_d.setWindowTitle("Ошибка!")
            error_d.setText("Невозможно выполнить операцию!")
            error_d.exec_()

    def delete_emp(self):
        try:
            cur = self.con.cursor()
            query = r"DELETE from Departments_employees " \
                    r"where department_id = {} and employee_id = {} ".format(self.dep_id_combobox.currentText().split()[0],
                                                                             self.emp_id_combobox.currentText().split()[0])
            cur.execute(query)
            self.update_table()
            self.update_dep_combobox()
            self.update_emp_combobox()
            self.update_table()

        except:
            error_d = QMessageBox()
            error_d.setIcon(QMessageBox.Critical)
            error_d.setWindowTitle("Ошибка удаления данных")
            error_d.setWindowTitle("Неизвестная ошибка!")

    def delete_dep(self):

        try:
            cur = self.con.cursor()
            query = r"DELETE from Departments " \
                    r"where id = {}".format(self.dep_id_combobox.currentText().split()[0])
            cur.execute(query)
            # print(query)
            self.update_table()
            self.update_dep_combobox()
            self.update_emp_combobox()
            self.update_table()
        except:
            # print(query)

            error_d = QMessageBox()
            error_d.setIcon(QMessageBox.Critical)
            error_d.setWindowTitle("Ошибка удаления данных")
            error_d.setWindowTitle("Неизвестная ошибка!")

    def update_dep_combobox(self):
        cur = self.con.cursor()
        self.dep_id_combobox.clear()
        cur.execute("select id, name from departments order by id")
        l = cur.fetchall()
        for id in l:
            self.dep_id_combobox.addItem('{} - {}'.format(id[0], id[1]))

        # self.dep_id_combobox.setCurrentIndex(0)
        # self.dep_id_edit.setText(self.dep_id_combobox.currentText())

    def update_emp_combobox(self):
        cur = self.con.cursor()
        self.emp_id_combobox.clear()
        cur.execute("select id, Last_name from Employees order by id")
        l = cur.fetchall()
        for id in l:
            self.emp_id_combobox.addItem('{} - {}'.format(id[0], id[1]))

        self.emp_id_combobox.setCurrentIndex(0)

    def update_table(self):
        cur = self.con.cursor()
        query = r"select " \
                r"DEPARTMENTS_EMPLOYEES.DEPARTMENT_ID," \
                r"DEPARTMENTS.NAME," \
                r"EMPLOYEES.ID,EMPLOYEES.LAST_NAME," \
                r"EMPLOYEES.FIRST_NAME" \
                r" from EMPLOYEES, DEPARTMENTS, DEPARTMENTS_EMPLOYEES " \
                r"WHERE EMPLOYEES.ID = DEPARTMENTS_EMPLOYEES.EMPLOYEE_ID AND DEPARTMENTS.ID = DEPARTMENTS_EMPLOYEES.DEPARTMENT_ID " \
                r"ORDER BY DEPARTMENTS.ID, employees.id"
        cur.execute('select count(*) from ({})'.format(query))
        self.N_ROWS = cur.fetchone()[0]
        self.table.setRowCount(self.N_ROWS)
        self.table.setHorizontalHeaderLabels(['Отдел', 'Название', 'Сотрудник', 'Фамилия', 'Имя'])
        cur.execute(query)

        l = cur.fetchall()
        ll = []
        for el in l:
            ll.append(list(el))
        for i in range(0, self.N_ROWS):
            for j in range(0, 5):
                self.table.setItem(i, j, QTableWidgetItem(str(ll[i][j])))

    def update_edits(self):
        if self.apply_btn2.text() == 'Изменить':

            self.dep_id_edit.setText(self.dep_id_combobox.currentText().split()[0])
            self.dep_name_edit.setText(self.dep_id_combobox.currentText().split()[2])

    def id_changed(self):
        self.update_edits()

    def add_clicked(self):
        self.hide_all()

        self.title_label.setText('Введите новые данные')
        self.title_label.show()

        # self.label1.setText('Добавление сотрудника в отдел')
        # self.label2.setText('Добавление отдела')

        self.dep_label.show()
        self.dep_label.show()
        self.emp_label.show()
        self.dep_name_label.show()

        self.dep_id_combobox.show()
        self.emp_id_combobox.show()

        self.apply_btn2.move(670, 400)
        self.apply_btn1.move(670, 200)
        self.dep_name_edit.show()

        self.apply_btn1.setText('Добавить сотрудника')
        self.apply_btn2.setText('Добавить отдел')
        self.rollback_btn.setText('Отменить')
        self.apply_btn1.show()
        self.apply_btn2.show()
        self.rollback_btn.show()
        self.commit_btn.show()

    def delete_clicked(self):
        self.hide_all()

        self.title_label.setText('Удалите данные')

        self.title_label.show()

        self.dep_label.show()
        self.emp_label.show()
        # self.dep_name_label.show()
        # self.dep_id_label.show()

        self.dep_id_combobox.show()
        self.emp_id_combobox.show()
        # self.dep_name_edit.show()
        # self.dep_id_edit.show()


        self.apply_btn1.setText('Удалить сотрудника')
        self.apply_btn2.setText('Удалить отдел')
        self.apply_btn2.move(670, 200)

        self.apply_btn1.move(670, 250)

        self.rollback_btn.setText('Отменить')

        self.apply_btn1.show()
        self.apply_btn2.show()

        self.rollback_btn.show()
        self.commit_btn.show()

    def apply1_clicked(self):
        if self.apply_btn1.text() == 'Добавить сотрудника':
            self.add_emp()
        elif self.apply_btn1.text() == 'Удалить сотрудника':
            self.delete_emp()
        self.update_emp_combobox()
        self.update_dep_combobox()
        self.update_table()

    def apply2_clicked(self):
        if self.apply_btn2.text() == 'Добавить отдел':
            self.add_dep()
        elif self.apply_btn2.text() == 'Удалить отдел':
            self.delete_dep()
        self.update_emp_combobox()
        self.update_dep_combobox()
        self.update_table()


    def commit_clicked(self):
        self.con.commit()
        self.update_emp_combobox()
        self.update_dep_combobox()
        self.update_table()

    def rollback_clicked(self):
        self.con.rollback()
        self.update_table()
        self.update_dep_combobox()
        self.update_emp_combobox()

    def hide_all(self):
        self.title_label.setVisible(False)

        self.dep_label.setVisible(False)
        self.emp_label.setVisible(False)
        self.dep_name_label.hide()
        self.dep_id_label.hide()

        self.dep_id_combobox.hide()
        self.emp_id_combobox.hide()
        # self.surname_edit.hide()
        # self.name_edit.hide()
        self.dep_name_edit.hide()
        self.dep_id_edit.hide()

        self.apply_btn1.hide()
        self.apply_btn2.hide()
        self.rollback_btn.hide()
        self.commit_btn.hide()

    def clear_all(self):
        self.dep_name_edit.setText('')
        self.dep_id_edit.setText('')