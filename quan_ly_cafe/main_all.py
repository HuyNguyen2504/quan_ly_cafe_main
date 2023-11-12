from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

import sys
import Hoa_don,Man_hinh_thong_ke_ui ,man_hinh_quan_ly_hoa_don , quan_ly_ban_khach, quan_ly_san_pham 
import Goi_mon_cafe,trang_chu

ui=''
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()


def mainpage():
    global ui
    ui= trang_chu.Ui_trang_chu()
    ui.setupUi(MainWindow)
    ui.menu.clicked.connect(qlb)
    ui.food.clicked.connect(cf)
    ui.check.clicked.connect(mhtkUi)
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
    MainWindow.show()
def mhtkUi():
    global ui
    ui = Man_hinh_thong_ke_ui.Ui_Man_hinh_thong_ke()
    ui.setupUi(MainWindow)
    ui.hoa_don.clicked.connect(hdUi)
    ui.menu.clicked.connect(qlb)
    ui.food.clicked.connect(cf)
    ui.quan_ly_hoa_don.clicked.connect(qlhdUi)
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
    MainWindow.show()
def qlb():
    global ui
    ui = quan_ly_ban_khach.Ui_quan_ly_ban_khach()
    ui.setupUi(MainWindow)
    ui.check.clicked.connect(mhtkUi)
    ui.quan_ly_san_pham.clicked.connect(qlsp)
    ui.food.clicked.connect(cf)
    ui.main.clicked.connect(mainpage)
    MainWindow.show()
def qlsp():
    global ui
    ui = quan_ly_san_pham.Ui_search()
    ui.setupUi(MainWindow)
    ui.check.clicked.connect(mhtkUi)
    ui.food.clicked.connect(cf)
    ui.quan_ly_ban.clicked.connect(qlb)
    ui.main.clicked.connect(mainpage)
    MainWindow.show()
def cf():
    global ui
    ui = Goi_mon_cafe.Ui_goi_mon_cafe()
    ui.setupUi(MainWindow)
    ui.check.clicked.connect(mhtkUi)
    ui.menu.clicked.connect(qlb)
    ui.main.clicked.connect(mainpage)
    MainWindow.show()
mainpage()
sys.exit(app.exec_())