# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'man_hinh_quan_ly_hoa_don.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_man_hinh_quan_ly_hoa_don(object):
    def setupUi(self, man_hinh_quan_ly_hoa_don):
        man_hinh_quan_ly_hoa_don.setObjectName("man_hinh_quan_ly_hoa_don")
        man_hinh_quan_ly_hoa_don.resize(1031, 811)
        self.centralwidget = QtWidgets.QWidget(man_hinh_quan_ly_hoa_don)
        self.centralwidget.setObjectName("centralwidget")
        self.thong_ke_gr = QtWidgets.QGroupBox(self.centralwidget)
        self.thong_ke_gr.setGeometry(QtCore.QRect(0, 0, 1031, 811))
        self.thong_ke_gr.setStyleSheet("background-color: rgb(0, 0, 212);")
        self.thong_ke_gr.setTitle("")
        self.thong_ke_gr.setObjectName("thong_ke_gr")
        self.check = QtWidgets.QPushButton(self.thong_ke_gr)
        self.check.setGeometry(QtCore.QRect(30, 360, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.check.setFont(font)
        self.check.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.check.setObjectName("check")
        self.exit = QtWidgets.QPushButton(self.thong_ke_gr)
        self.exit.setGeometry(QtCore.QRect(30, 700, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.exit.setFont(font)
        self.exit.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.exit.setObjectName("exit")
        self.main = QtWidgets.QPushButton(self.thong_ke_gr)
        self.main.setGeometry(QtCore.QRect(30, 120, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.main.setFont(font)
        self.main.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.main.setObjectName("main")
        self.account = QtWidgets.QPushButton(self.thong_ke_gr)
        self.account.setGeometry(QtCore.QRect(30, 580, 171, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.account.setFont(font)
        self.account.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.account.setObjectName("account")
        self.back = QtWidgets.QPushButton(self.thong_ke_gr)
        self.back.setGeometry(QtCore.QRect(900, 747, 93, 41))
        self.back.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.back.setObjectName("back")
        self.quan_ly_hoa_don = QtWidgets.QPushButton(self.thong_ke_gr)
        self.quan_ly_hoa_don.setGeometry(QtCore.QRect(470, 30, 251, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.quan_ly_hoa_don.setFont(font)
        self.quan_ly_hoa_don.setStyleSheet("\n"
"background-color: rgb(0, 255, 255);")
        self.quan_ly_hoa_don.setObjectName("quan_ly_hoa_don")
        self.food = QtWidgets.QPushButton(self.thong_ke_gr)
        self.food.setGeometry(QtCore.QRect(30, 470, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.food.setFont(font)
        self.food.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.food.setObjectName("food")
        self.thong_ke = QtWidgets.QPushButton(self.thong_ke_gr)
        self.thong_ke.setGeometry(QtCore.QRect(220, 30, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.thong_ke.setFont(font)
        self.thong_ke.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.thong_ke.setObjectName("thong_ke")
        self.menu = QtWidgets.QPushButton(self.thong_ke_gr)
        self.menu.setGeometry(QtCore.QRect(30, 230, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menu.setFont(font)
        self.menu.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.menu.setObjectName("menu")
        self.hoa_don = QtWidgets.QPushButton(self.thong_ke_gr)
        self.hoa_don.setGeometry(QtCore.QRect(730, 30, 261, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.hoa_don.setFont(font)
        self.hoa_don.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.hoa_don.setObjectName("hoa_don")
        self.groupBox = QtWidgets.QGroupBox(self.thong_ke_gr)
        self.groupBox.setGeometry(QtCore.QRect(280, 370, 691, 161))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.groupBox.setObjectName("groupBox")
        self.ma_hoa_don_qlhd1 = QtWidgets.QLineEdit(self.groupBox)
        self.ma_hoa_don_qlhd1.setGeometry(QtCore.QRect(0, 80, 113, 22))
        self.ma_hoa_don_qlhd1.setObjectName("ma_hoa_don_qlhd1")
        self.ten_sp_qlhd1 = QtWidgets.QLineEdit(self.groupBox)
        self.ten_sp_qlhd1.setGeometry(QtCore.QRect(110, 80, 113, 22))
        self.ten_sp_qlhd1.setObjectName("ten_sp_qlhd1")
        self.ten_ban_qlhd1 = QtWidgets.QLineEdit(self.groupBox)
        self.ten_ban_qlhd1.setGeometry(QtCore.QRect(220, 80, 121, 22))
        self.ten_ban_qlhd1.setObjectName("ten_ban_qlhd1")
        self.so_luong_qlhd1 = QtWidgets.QLineEdit(self.groupBox)
        self.so_luong_qlhd1.setGeometry(QtCore.QRect(340, 80, 121, 22))
        self.so_luong_qlhd1.setObjectName("so_luong_qlhd1")
        self.don_gia_qlhd1 = QtWidgets.QLineEdit(self.groupBox)
        self.don_gia_qlhd1.setGeometry(QtCore.QRect(460, 80, 121, 22))
        self.don_gia_qlhd1.setObjectName("don_gia_qlhd1")
        self.tong_qlhd1 = QtWidgets.QLineEdit(self.groupBox)
        self.tong_qlhd1.setGeometry(QtCore.QRect(580, 80, 111, 22))
        self.tong_qlhd1.setObjectName("tong_qlhd1")
        self.don_gia_qlhd2 = QtWidgets.QLineEdit(self.groupBox)
        self.don_gia_qlhd2.setGeometry(QtCore.QRect(460, 100, 121, 22))
        self.don_gia_qlhd2.setObjectName("don_gia_qlhd2")
        self.ten_sp_qlhd2 = QtWidgets.QLineEdit(self.groupBox)
        self.ten_sp_qlhd2.setGeometry(QtCore.QRect(110, 100, 113, 22))
        self.ten_sp_qlhd2.setObjectName("ten_sp_qlhd2")
        self.ma_hoa_don_qlhd2 = QtWidgets.QLineEdit(self.groupBox)
        self.ma_hoa_don_qlhd2.setGeometry(QtCore.QRect(0, 100, 113, 22))
        self.ma_hoa_don_qlhd2.setObjectName("ma_hoa_don_qlhd2")
        self.so_luong_qlhd2 = QtWidgets.QLineEdit(self.groupBox)
        self.so_luong_qlhd2.setGeometry(QtCore.QRect(340, 100, 121, 22))
        self.so_luong_qlhd2.setObjectName("so_luong_qlhd2")
        self.ten_ban_qlhd2 = QtWidgets.QLineEdit(self.groupBox)
        self.ten_ban_qlhd2.setGeometry(QtCore.QRect(220, 100, 121, 22))
        self.ten_ban_qlhd2.setObjectName("ten_ban_qlhd2")
        self.tong_qlhd2 = QtWidgets.QLineEdit(self.groupBox)
        self.tong_qlhd2.setGeometry(QtCore.QRect(580, 100, 111, 22))
        self.tong_qlhd2.setObjectName("tong_qlhd2")
        self.ma_hoa_don_qlhd4 = QtWidgets.QLineEdit(self.groupBox)
        self.ma_hoa_don_qlhd4.setGeometry(QtCore.QRect(0, 140, 113, 22))
        self.ma_hoa_don_qlhd4.setObjectName("ma_hoa_don_qlhd4")
        self.don_gia_qlhd3 = QtWidgets.QLineEdit(self.groupBox)
        self.don_gia_qlhd3.setGeometry(QtCore.QRect(460, 120, 121, 22))
        self.don_gia_qlhd3.setObjectName("don_gia_qlhd3")
        self.ten_sp_qlhd4 = QtWidgets.QLineEdit(self.groupBox)
        self.ten_sp_qlhd4.setGeometry(QtCore.QRect(110, 140, 113, 22))
        self.ten_sp_qlhd4.setObjectName("ten_sp_qlhd4")
        self.ten_sp_qlhd3 = QtWidgets.QLineEdit(self.groupBox)
        self.ten_sp_qlhd3.setGeometry(QtCore.QRect(110, 120, 113, 22))
        self.ten_sp_qlhd3.setObjectName("ten_sp_qlhd3")
        self.ma_hoa_don_qlhd3 = QtWidgets.QLineEdit(self.groupBox)
        self.ma_hoa_don_qlhd3.setGeometry(QtCore.QRect(0, 120, 113, 22))
        self.ma_hoa_don_qlhd3.setObjectName("ma_hoa_don_qlhd3")
        self.ten_ban_qlhd4 = QtWidgets.QLineEdit(self.groupBox)
        self.ten_ban_qlhd4.setGeometry(QtCore.QRect(220, 140, 121, 22))
        self.ten_ban_qlhd4.setObjectName("ten_ban_qlhd4")
        self.so_luong_qlhd3 = QtWidgets.QLineEdit(self.groupBox)
        self.so_luong_qlhd3.setGeometry(QtCore.QRect(340, 120, 121, 22))
        self.so_luong_qlhd3.setObjectName("so_luong_qlhd3")
        self.don_gia_qlhd4 = QtWidgets.QLineEdit(self.groupBox)
        self.don_gia_qlhd4.setGeometry(QtCore.QRect(460, 140, 121, 22))
        self.don_gia_qlhd4.setObjectName("don_gia_qlhd4")
        self.so_luong_qlhd4 = QtWidgets.QLineEdit(self.groupBox)
        self.so_luong_qlhd4.setGeometry(QtCore.QRect(340, 140, 121, 22))
        self.so_luong_qlhd4.setObjectName("so_luong_qlhd4")
        self.tong_qlhd4 = QtWidgets.QLineEdit(self.groupBox)
        self.tong_qlhd4.setGeometry(QtCore.QRect(580, 140, 111, 22))
        self.tong_qlhd4.setObjectName("tong_qlhd4")
        self.ten_ban_qlhd3 = QtWidgets.QLineEdit(self.groupBox)
        self.ten_ban_qlhd3.setGeometry(QtCore.QRect(220, 120, 121, 22))
        self.ten_ban_qlhd3.setObjectName("ten_ban_qlhd3")
        self.tong_qlhd3 = QtWidgets.QLineEdit(self.groupBox)
        self.tong_qlhd3.setGeometry(QtCore.QRect(580, 120, 111, 22))
        self.tong_qlhd3.setObjectName("tong_qlhd3")
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setGeometry(QtCore.QRect(10, 60, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        self.label_18.setGeometry(QtCore.QRect(110, 60, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.groupBox)
        self.label_19.setGeometry(QtCore.QRect(250, 60, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.groupBox)
        self.label_20.setGeometry(QtCore.QRect(370, 60, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.groupBox)
        self.label_21.setGeometry(QtCore.QRect(490, 60, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.groupBox)
        self.label_22.setGeometry(QtCore.QRect(620, 60, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.ten_sp_qlhd1.raise_()
        self.ten_ban_qlhd1.raise_()
        self.so_luong_qlhd1.raise_()
        self.don_gia_qlhd1.raise_()
        self.tong_qlhd1.raise_()
        self.don_gia_qlhd2.raise_()
        self.ten_sp_qlhd2.raise_()
        self.so_luong_qlhd2.raise_()
        self.ten_ban_qlhd2.raise_()
        self.tong_qlhd2.raise_()
        self.ma_hoa_don_qlhd2.raise_()
        self.ma_hoa_don_qlhd1.raise_()
        self.don_gia_qlhd3.raise_()
        self.ten_sp_qlhd4.raise_()
        self.ten_sp_qlhd3.raise_()
        self.ma_hoa_don_qlhd3.raise_()
        self.ten_ban_qlhd4.raise_()
        self.so_luong_qlhd3.raise_()
        self.don_gia_qlhd4.raise_()
        self.so_luong_qlhd4.raise_()
        self.tong_qlhd4.raise_()
        self.ten_ban_qlhd3.raise_()
        self.tong_qlhd3.raise_()
        self.ma_hoa_don_qlhd4.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.tim_kiem_hoa_don = QtWidgets.QLineEdit(self.thong_ke_gr)
        self.tim_kiem_hoa_don.setGeometry(QtCore.QRect(342, 141, 231, 51))
        self.tim_kiem_hoa_don.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tim_kiem_hoa_don.setObjectName("tim_kiem_hoa_don")
        self.label = QtWidgets.QLabel(self.thong_ke_gr)
        self.label.setGeometry(QtCore.QRect(290, 140, 51, 51))
        self.label.setStyleSheet("border-image: url(:/picture/398288296_664763935842542_91204699368765392_n.png);\n"
"border-color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.thong_ke_gr)
        self.pushButton.setGeometry(QtCore.QRect(572, 137, 61, 61))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(189, 189, 189);")
        self.pushButton.setObjectName("pushButton")
        man_hinh_quan_ly_hoa_don.setCentralWidget(self.centralwidget)

        self.retranslateUi(man_hinh_quan_ly_hoa_don)
        QtCore.QMetaObject.connectSlotsByName(man_hinh_quan_ly_hoa_don)

    def retranslateUi(self, man_hinh_quan_ly_hoa_don):
        _translate = QtCore.QCoreApplication.translate
        man_hinh_quan_ly_hoa_don.setWindowTitle(_translate("man_hinh_quan_ly_hoa_don", "Quản Lý Hóa Đơn"))
        self.check.setText(_translate("man_hinh_quan_ly_hoa_don", "Hóa Đơn"))
        self.exit.setText(_translate("man_hinh_quan_ly_hoa_don", "Đăng Xuất"))
        self.main.setText(_translate("man_hinh_quan_ly_hoa_don", "Trang chủ"))
        self.account.setText(_translate("man_hinh_quan_ly_hoa_don", "Tài Khoản"))
        self.back.setText(_translate("man_hinh_quan_ly_hoa_don", "Trở về"))
        self.quan_ly_hoa_don.setText(_translate("man_hinh_quan_ly_hoa_don", "Quản Lý Hóa Đơn"))
        self.food.setText(_translate("man_hinh_quan_ly_hoa_don", "Gọi Món"))
        self.thong_ke.setText(_translate("man_hinh_quan_ly_hoa_don", "Thống Kê"))
        self.menu.setText(_translate("man_hinh_quan_ly_hoa_don", "MENU"))
        self.hoa_don.setText(_translate("man_hinh_quan_ly_hoa_don", "Hóa Đơn"))
        self.groupBox.setTitle(_translate("man_hinh_quan_ly_hoa_don", "Thông Tin Hóa Đơn"))
        self.label_17.setText(_translate("man_hinh_quan_ly_hoa_don", "Mã Hóa Đơn"))
        self.label_18.setText(_translate("man_hinh_quan_ly_hoa_don", "Tên Sản Phẩm"))
        self.label_19.setText(_translate("man_hinh_quan_ly_hoa_don", "Tên Bàn"))
        self.label_20.setText(_translate("man_hinh_quan_ly_hoa_don", "Số Lượng"))
        self.label_21.setText(_translate("man_hinh_quan_ly_hoa_don", "Đơn giá"))
        self.label_22.setText(_translate("man_hinh_quan_ly_hoa_don", "Tổng"))
        self.pushButton.setText(_translate("man_hinh_quan_ly_hoa_don", "Tìm kiếm"))
import add_image_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    man_hinh_quan_ly_hoa_don = QtWidgets.QMainWindow()
    ui = Ui_man_hinh_quan_ly_hoa_don()
    ui.setupUi(man_hinh_quan_ly_hoa_don)
    man_hinh_quan_ly_hoa_don.show()
    sys.exit(app.exec_())