# Form implementation generated from reading ui file '/Users/pinxun/Documents/MindX/PTA/PTA08/BaoChau/python-app/ui/resign.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(840, 612)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.btn_register = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_register.setGeometry(QtCore.QRect(70, 390, 271, 41))
        self.btn_register.setStyleSheet(" background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 89, 102, 255), stop:1 rgba(255, 255, 255, 255)); /* Màu nền tím */\n"
"    color: white;             /* Màu chữ */\n"
"    font-size: 16px;          /* Kích thước chữ */\n"
"    font-weight: bold;        /* Chữ in đậm */\n"
"    border: none;             /* Xóa đường viền mặc định */\n"
"    border-radius: 20px;      /* Bo góc */\n"
"    padding: 10px 20px;       /* Khoảng cách bên trong */\n"
"color: rgb(0, 0, 0)\n"
" ")
        self.btn_register.setObjectName("btn_register")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-10, 470, 421, 101))
        self.label_2.setStyleSheet("background-color: rgb(0, 0, 0)")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 411, 471))
        self.label_3.setStyleSheet("background-color: rgb(244, 244, 244)")
        self.label_3.setText("")
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 480, 81, 21))
        self.pushButton_2.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border-radius: 9px")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA08/BaoChau/python-app/ui/../img/Google__G__logo.svg.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 480, 81, 21))
        self.pushButton_3.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border-radius: 9px")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA08/BaoChau/python-app/ui/../img/images.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(160, 450, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("")
        self.label_7.setObjectName("label_7")
        self.btn_login = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_login.setGeometry(QtCore.QRect(270, 520, 91, 21))
        self.btn_login.setStyleSheet("color: white;             /* Màu chữ */\n"
"font-size: 16px;          /* Kích thước chữ */\n"
"font-weight: bold;        /* Chữ in đậm */\n"
"border: none;             /* Xóa đường viền mặc định */\n"
"border-radius: 20px;\n"
"background-color: rgb(0, 0, 255)")
        self.btn_login.setObjectName("btn_login")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(170, 0, 61, 41))
        self.label_6.setStyleSheet("font-size: 20px;          /* Kích thước chữ */\n"
"    font-weight: Arial;\n"
"color:rgb(0, 0, 0)")
        self.label_6.setObjectName("label_6")
        self.label_15 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(40, 40, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(False)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("font-size: 25px;          /* Kích thước chữ */\n"
"color:rgb(0, 0, 0)")
        self.label_15.setObjectName("label_15")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(50, 80, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(17)
        font.setBold(False)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(75, 75, 75)")
        self.label_8.setObjectName("label_8")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(410, 0, 431, 571))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA08/BaoChau/python-app/ui/../img/265b15abe358d372e8fe6cd38d982614b29e3911.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 520, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255)")
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 110, 341, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=self.verticalLayoutWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.txt_name = QtWidgets.QLineEdit(parent=self.frame)
        self.txt_name.setGeometry(QtCore.QRect(60, 20, 251, 41))
        self.txt_name.setStyleSheet("background-color: #f8f9fa; /* Màu nền */\n"
"    border: 2px solid #ced4da; /* Viền */\n"
"    border-radius: 5px;       /* Bo góc */\n"
"    padding: 5px;             /* Khoảng cách bên trong */\n"
"    font-size: 14px;          /* Cỡ chữ */\n"
"    color: #495057;           /* Màu chữ */\n"
"border: 2px solid #007bff; /* Viền khi đang focus (nhấp chuột vào ô) */\n"
"    outline: none;             /* Xóa viền mặc định */")
        self.txt_name.setObjectName("txt_name")
        self.label_11 = QtWidgets.QLabel(parent=self.frame)
        self.label_11.setGeometry(QtCore.QRect(10, 20, 40, 41))
        self.label_11.setMaximumSize(QtCore.QSize(40, 1000))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA08/BaoChau/python-app/ui/../img/address-card-solid.svg"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(parent=self.verticalLayoutWidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_5 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 41, 41))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA08/BaoChau/python-app/ui/../img/at-solid.svg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.txt_email = QtWidgets.QLineEdit(parent=self.frame_2)
        self.txt_email.setGeometry(QtCore.QRect(60, 20, 251, 41))
        self.txt_email.setStyleSheet("background-color: #f8f9fa; /* Màu nền */\n"
"    border: 2px solid #ced4da; /* Viền */\n"
"    border-radius: 5px;       /* Bo góc */\n"
"    padding: 5px;             /* Khoảng cách bên trong */\n"
"    font-size: 14px;          /* Cỡ chữ */\n"
"    color: #495057;           /* Màu chữ */\n"
"border: 2px solid #007bff; /* Viền khi đang focus (nhấp chuột vào ô) */\n"
"    outline: none;             /* Xóa viền mặc định */")
        self.txt_email.setObjectName("txt_email")
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(parent=self.verticalLayoutWidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_9 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_9.setGeometry(QtCore.QRect(10, 20, 40, 40))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA08/BaoChau/python-app/ui/../img/key-solid.svg"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.txt_password = QtWidgets.QLineEdit(parent=self.frame_3)
        self.txt_password.setGeometry(QtCore.QRect(60, 20, 251, 41))
        self.txt_password.setStyleSheet("background-color: #f8f9fa; /* Màu nền */\n"
"    border: 2px solid #ced4da; /* Viền */\n"
"    border-radius: 5px;       /* Bo góc */\n"
"    padding: 5px;             /* Khoảng cách bên trong */\n"
"    font-size: 14px;          /* Cỡ chữ */\n"
"    color: #495057;           /* Màu chữ */\n"
"border: 2px solid #007bff; /* Viền khi đang focus (nhấp chuột vào ô) */\n"
"    outline: none;             /* Xóa viền mặc định */")
        self.txt_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.txt_password.setObjectName("txt_password")
        self.btn_eye_p = QtWidgets.QPushButton(parent=self.frame_3)
        self.btn_eye_p.setGeometry(QtCore.QRect(260, 20, 51, 41))
        self.btn_eye_p.setStyleSheet("border: none;\n"
"background: none;")
        self.btn_eye_p.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA08/BaoChau/python-app/ui/../img/eye-slash-solid.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_eye_p.setIcon(icon2)
        self.btn_eye_p.setIconSize(QtCore.QSize(32, 32))
        self.btn_eye_p.setObjectName("btn_eye_p")
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(parent=self.verticalLayoutWidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_10 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_10.setGeometry(QtCore.QRect(10, 20, 41, 41))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA08/BaoChau/python-app/ui/../img/check-solid.svg"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.txt_conf_pwd = QtWidgets.QLineEdit(parent=self.frame_4)
        self.txt_conf_pwd.setGeometry(QtCore.QRect(60, 20, 251, 41))
        self.txt_conf_pwd.setStyleSheet("background-color: #f8f9fa; /* Màu nền */\n"
"    border: 2px solid #ced4da; /* Viền */\n"
"    border-radius: 5px;       /* Bo góc */\n"
"    padding: 5px;             /* Khoảng cách bên trong */\n"
"    font-size: 14px;          /* Cỡ chữ */\n"
"    color: #495057;           /* Màu chữ */\n"
"border: 2px solid #007bff; /* Viền khi đang focus (nhấp chuột vào ô) */\n"
"    outline: none;             /* Xóa viền mặc định */")
        self.txt_conf_pwd.setText("")
        self.txt_conf_pwd.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.txt_conf_pwd.setObjectName("txt_conf_pwd")
        self.btn_eye_cp = QtWidgets.QPushButton(parent=self.frame_4)
        self.btn_eye_cp.setGeometry(QtCore.QRect(260, 20, 51, 41))
        self.btn_eye_cp.setStyleSheet("border: none;\n"
"background: none;")
        self.btn_eye_cp.setText("")
        self.btn_eye_cp.setIcon(icon2)
        self.btn_eye_cp.setIconSize(QtCore.QSize(32, 32))
        self.btn_eye_cp.setObjectName("btn_eye_cp")
        self.verticalLayout.addWidget(self.frame_4)
        self.label_2.raise_()
        self.label_3.raise_()
        self.btn_register.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.label_7.raise_()
        self.btn_login.raise_()
        self.label_6.raise_()
        self.label_15.raise_()
        self.label_8.raise_()
        self.label_4.raise_()
        self.label.raise_()
        self.verticalLayoutWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 840, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_register.setText(_translate("MainWindow", " Click Here To Create Account"))
        self.pushButton_2.setText(_translate("MainWindow", "Google"))
        self.pushButton_3.setText(_translate("MainWindow", "Facebook"))
        self.label_7.setText(_translate("MainWindow", "Or Create By:"))
        self.btn_login.setText(_translate("MainWindow", "Click Here!"))
        self.label_6.setText(_translate("MainWindow", "Rishop"))
        self.label_15.setText(_translate("MainWindow", "-Welcome, Have a nice day !-"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Create An Account</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "You Already Have An Account?"))
        self.txt_name.setPlaceholderText(_translate("MainWindow", "Username"))
        self.txt_email.setPlaceholderText(_translate("MainWindow", "Email"))
        self.txt_password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.txt_conf_pwd.setPlaceholderText(_translate("MainWindow", "Confirm Password"))
