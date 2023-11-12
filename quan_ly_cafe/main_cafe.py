import typing
from PyQt5 import QtCore, QtWidgets,uic
from PyQt5.QtWidgets import *

from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
import sys
import MySQLdb as mdb
import Hoa_don,Man_hinh_thong_ke_ui ,man_hinh_quan_ly_hoa_don , quan_ly_ban_khach, quan_ly_san_pham 
import Goi_mon_cafe,trang_chu, dang_ki,dang_nhap, dang_nhap_sai,quen_mk,doi_mat_khau,dang_xuat

ui=''
unn=''
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
widget = QtWidgets.QStackedWidget()
#cua so login
class Login_w(QMainWindow):
    def __init__(self):
        super(Login_w,self).__init__()
        uic.loadUi('dang_nhap.ui',self)
        self.dang_nhap.clicked.connect(self.login)
        self.dang_ki.clicked.connect(self.reg_form)
        self.doi_mk.clicked.connect(self.change_form)
        self.forgoted_mk.clicked.connect(self.forgot_form)
    def forgot_form(self):
        widget.setCurrentIndex(4)
    def reg_form(self):
        widget.setCurrentIndex(2)
    def change_form(self):
        widget.setCurrentIndex(3)
    def login(self):
        un=self.tai_khoan.text()
        psw=self.mat_khau.text()
        global unn
        unn = "'" + un + 'database' + "'"
        db = mdb.connect(host='localhost', port=3307, user='huynguyen', passwd='nguyenvanhuy03', db='accounts')
        query = db.cursor()
        query.execute("select * from accounts_list where user= '"+un+"' and pass= '"+psw+"' ")
        kt = query.fetchone()
        if kt:
            #QMessageBox.information(self,"Login ouput","Login success")
            global ui
            ui = trang_chu.Ui_trang_chu()
            ui.setupUi(MainWindow)
            ui.menu.clicked.connect(qlb)
            ui.food.clicked.connect(cf)
            ui.check.clicked.connect(mhtkUi)
            ui.exit.clicked.connect(exit_out)
            MainWindow.show()
            config = {
                'user': 'username',
                'password': 'password',
                'port' : 3307,
                'host': 'localhost',
                'database': unn  # Sử dụng biến tên cơ sở dữ liệu ở đây
            }
            db = mdb.connect(**config)
            widget.destroy()           
        else:
            #QMessageBox.information(self,"Login ouput","Login fail")
            widget.setCurrentIndex(1)
class Login_f_w(QMainWindow):
    def __init__(self):
        super(Login_f_w,self).__init__()
        uic.loadUi('dang_nhap_sai.ui',self)
        self.dang_nhap_tk.clicked.connect(self.login)
        self.dang_ki.clicked.connect(self.reg_form)
        self.doi_mk.clicked.connect(self.change_form)
        self.forgoted_mk.clicked.connect(self.forgot_form)
    def forgot_form(self):
        widget.setCurrentIndex(4)
    def reg_form(self):
        widget.setCurrentIndex(2)
    def change_form(self):
        widget.setCurrentIndex(3)
    def login(self):
        un=self.tai_khoan.text()
        psw=self.mat_khau.text()
        global unn
        unn = "'" + un + 'database' + "'"
        db = mdb.connect(host='localhost', port=3307, user='huynguyen', passwd='nguyenvanhuy03', db='accounts')
        query = db.cursor()
        query.execute("select * from accounts_list where user= '"+un+"' and pass= '"+psw+"' ")
        kt = query.fetchone()
        if kt:
            #QMessageBox.information(self,"Login ouput","Login success")
            global ui
            ui = trang_chu.Ui_trang_chu()
            ui.setupUi(MainWindow)
            ui.menu.clicked.connect(qlb)
            ui.food.clicked.connect(cf)
            ui.check.clicked.connect(mhtkUi)
            MainWindow.show()
            config = {
                'user': 'username',
                'password': 'password',
                'port' : 3307,
                'host': 'localhost',
                'database': unn  # Sử dụng biến tên cơ sở dữ liệu ở đây
            }
            db = mdb.connect(**config)
            widget.destroy()
        else:
            #QMessageBox.information(self,"Login ouput","Login fail")
            widget.setCurrentIndex(1)       
#cua so register

class Reg_w(QMainWindow):
    def __init__(self):
        super(Reg_w,self).__init__()
        uic.loadUi('dang_ki.ui',self)   
        self.dang_ki_2.clicked.connect(self.reg)
        self.back_dn.clicked.connect(self.back_in)
    def back_in(self):
        widget.setCurrentIndex(0)
    def reg(self):
        un=self.tai_khoan_dang_ki.text()
        psw=self.mat_khau_dang_ki.text()
        pswa=self.mat_khau_dang_ki_2.text()
        if psw==pswa:
            db = mdb.connect(host='localhost', port=3307, user='huynguyen', passwd='nguyenvanhuy03', db='accounts')
            query = db.cursor()
            query.execute("select * from accounts_list where user= '"+un+"' and pass= '"+psw+"' ")
            kt = query.fetchone()
            if kt:
                QMessageBox.information(self,"Reg ouput","tai khoan da ton tai")
            else:              
                query.execute("insert into accounts_list values ('"+un+"', '"+psw+"') ")
                db.commit()
                global unn
                unn = un +'database'
                db = mdb.connect(host='localhost', port=3307, user='huynguyen', passwd='nguyenvanhuy03',db='')
                query = db.cursor()
                query.execute("create database `'"+unn+"'` ")
                db.commit()
                QMessageBox.information(self,"Reg ouput","dang ki thanh cong")                    
        else:
            QMessageBox.information(self,"Reg output","MẬT KHẨU SAI \nHOẶC KHÔNG TRÙNG KHỚP")

    
#cua so doi mat khau
class Change_w(QMainWindow):
    def __init__(self):
        super(Change_w,self).__init__()
        uic.loadUi('doi_mat_khau.ui',self)
        self.back_dn.clicked.connect(self.back_in)
        self.xac_nhan.clicked.connect(self.change_pass)
    def back_in(self):
        widget.setCurrentIndex(0)
    def change_pass(self):
        un=self.tai_khoan_dang_ki.text()
        psw=self.mat_khau_cu.text()
        pswn=self.mat_khau_dang_ki.text()
        pswna=self.mat_khau_dang_ki_2.text()
        if pswna == pswn:
            db = mdb.connect(host='localhost', port=3307, user='huynguyen', passwd='nguyenvanhuy03', db='accounts')
            query = db.cursor()
            query.execute("select * from accounts_list where user= '"+un+"' and pass= '"+psw+"' ")
            kt = query.fetchone()
            if kt:                
                QMessageBox.information(self,"Change_pass_output","Success")
                query.execute("update accounts_list set pass= '"+pswn+"' where user= '"+un+"' ")
                db.commit()
            else:
                QMessageBox.information(self,"Change_pass_output","TÀI KHOẢN KHÔNG TỒN TẠI \nHOẶC MẬT KHẨU KHÔNG ĐÚNG")
        else :
            QMessageBox.information(self,"Change_pass_output","MẬT KHẨU KHÔNG TRÙNG KHỚP")
#cua so quen mk
class forgot_w(QMainWindow):
    def __init__(self):
        super(forgot_w,self).__init__()
        uic.loadUi('quen_mk.ui',self)
        self.back_dn.clicked.connect(self.back_in)
        self.xac_nhan.clicked.connect(self.change_pass)
    def back_in(self):
        widget.setCurrentIndex(0)
    def change_pass(self):
        un=self.tai_khoan_dang_ki.text()
        pswn=self.mat_khau_dang_ki.text()
        pswna=self.mat_khau_dang_ki_2.text()
        db = mdb.connect(host='localhost', port=3307, user='huynguyen', passwd='nguyenvanhuy03', db='accounts')
        query = db.cursor()
        query.execute("select * from accounts_list where user= '"+un+"' ")
        kt = query.fetchone()
        if kt:
            if pswna == pswn:
                QMessageBox.information(self,"Change_pass_output","Success")
                query.execute("update accounts_list set pass= '"+pswn+"' where user= '"+un+"' ")
                db.commit()
            else:
                QMessageBox.information(self,"Change_pass_output","MẬT KHẨU KHÔNG TRÙNG KHỚP")
        else :
            QMessageBox.information(self,"Change_pass_output","TÀI KHOẢN KHÔNG TỒN TẠI \nHOẶC MẬT KHẨU KHÔNG ĐÚNG")

def exit_out():
    global ui
    ui= dang_xuat.Ui_dang_xuat()
    ui.setupUi(MainWindow)
    ui.dang_xuat_han.clicked.connect(out_w)
    ui.tro_ve.clicked.connect(mainpage)
    MainWindow.show()

def out_w():
    widget.setCurrentIndex(0)
    MainWindow.destroy()
def mainpage():
    global ui
    ui= trang_chu.Ui_trang_chu()
    ui.setupUi(MainWindow)
    ui.menu.clicked.connect(qlb)
    ui.food.clicked.connect(cf)
    ui.check.clicked.connect(mhtkUi)
    ui.exit.clicked.connect(exit_out)
    MainWindow.show()
def hdUi():
    global ui
    ui = Hoa_don.Ui_Hoa_Don()
    ui.setupUi(MainWindow)
    ui.thong_ke.clicked.connect(mhtkUi)
    ui.menu.clicked.connect(qlb)
    ui.food.clicked.connect(cf)
    ui.main.clicked.connect(mainpage)
    ui.quan_ly_hoa_don.clicked.connect(qlhdUi)
    ui.exit.clicked.connect(exit_out)
    MainWindow.show()
def mhtkUi():
    global ui
    ui = Man_hinh_thong_ke_ui.Ui_Man_hinh_thong_ke()
    ui.setupUi(MainWindow)
    ui.hoa_don.clicked.connect(hdUi)
    ui.menu.clicked.connect(qlb)
    ui.food.clicked.connect(cf)
    ui.quan_ly_hoa_don.clicked.connect(qlhdUi)
    ui.exit.clicked.connect(exit_out)
    ui.main.clicked.connect(mainpage)
    MainWindow.show() 
def qlhdUi():
    global ui
    ui = man_hinh_quan_ly_hoa_don.Ui_man_hinh_quan_ly_hoa_don()
    ui.setupUi(MainWindow)
    ui.thong_ke.clicked.connect(mhtkUi)
    ui.hoa_don.clicked.connect(hdUi)
    ui.food.clicked.connect(cf)
    ui.menu.clicked.connect(qlb)
    ui.main.clicked.connect(mainpage)
    ui.exit.clicked.connect(exit_out)
    MainWindow.show()
def qlb():
    global ui
    ui = quan_ly_ban_khach.Ui_quan_ly_ban_khach()
    ui.setupUi(MainWindow)
    ui.check.clicked.connect(mhtkUi)
    ui.quan_ly_san_pham.clicked.connect(qlsp)
    ui.food.clicked.connect(cf)
    ui.main.clicked.connect(mainpage)
    ui.exit.clicked.connect(exit_out)
    MainWindow.show()
def qlsp():
    global ui
    ui = quan_ly_san_pham.Ui_search()
    ui.setupUi(MainWindow)
    ui.check.clicked.connect(mhtkUi)
    ui.food.clicked.connect(cf)
    ui.quan_ly_ban.clicked.connect(qlb)
    ui.exit.clicked.connect(exit_out)
    ui.main.clicked.connect(mainpage)
    MainWindow.show()
def cf():
    global ui
    ui = Goi_mon_cafe.Ui_goi_mon_cafe()
    ui.setupUi(MainWindow)
    ui.check.clicked.connect(mhtkUi)
    ui.menu.clicked.connect(qlb)
    ui.main.clicked.connect(mainpage)
    ui.exit.clicked.connect(exit_out)
    MainWindow.show()


    
Login_f=Login_w()
Reg_f=Reg_w()
Change_f=Change_w()
Login_f_f=Login_f_w()
Forgot_f=forgot_w()
widget.addWidget(Login_f)
widget.addWidget(Login_f_f)
widget.addWidget(Reg_f)
widget.addWidget(Change_f)
widget.addWidget(Forgot_f)
widget.setCurrentIndex(0)
widget.setFixedHeight(400)
widget.setFixedWidth(800)
widget.show()
sys.exit(app.exec())