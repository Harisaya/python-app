from PyQt6 import QtWidgets,QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6 import uic
import sys
from database import *

class MessageBox:
    def success_box(self, message):
        box = QMessageBox()
        box.setWindowTitle("Success")
        box.setText(message)
        box.setIcon(QMessageBox.Icon.Information)
        box.exec()

    def error_box(self, message):
        box = QMessageBox()
        box.setWindowTitle("Error")
        box.setText(message)
        box.setIcon(QMessageBox.Icon.Critical)
        box.exec()

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/login.ui", self)

        self.email = self.findChild(QLineEdit, "txt_email")
        self.password = self.findChild(QLineEdit, "txt_password")
        self.btn_login = self.findChild(QPushButton, "btn_login")
        self.btn_register = self.findChild(QPushButton, "btn_register")
        self.btn_eye_p = self.findChild(QPushButton, "btn_eye_p")

        self.btn_login.clicked.connect(self.login)
        self.btn_register.clicked.connect(self.show_register)
        self.btn_eye_p.clicked.connect(lambda: self.hiddenOrShow(self.password, self.btn_eye_p))

    def hiddenOrShow(self, input: QLineEdit, btn: QPushButton):
        if input.echoMode() == QLineEdit.EchoMode.Password:
            input.setEchoMode(QLineEdit.EchoMode.Normal)
            btn.setIcon(QIcon("img/eye-solid.jpg"))
        else:
            input.setEchoMode(QLineEdit.EchoMode.Password)
            btn.setIcon(QIcon("img/eye-slash-solid.jpg"))

    def login(self):
        msg = MessageBox()
        email = self.email.text().strip()
        password = self.password.text().strip()

        if email == "" or password == "":
            msg.error_box("Không thể để trống")
            return

        user = get_user_by_email_and_password(email, password)
        if user:
            msg.success_box("Đăng nhập thành công")
            self.home = Home(user["id"])
            self.home.show()
            self.close()
        else:
            msg.error_box("Đăng nhập thất bại")

    def show_register(self):
        self.register = Register()
        self.register.show()
        self.close()

class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/resign.ui", self)

        self.name = self.findChild(QLineEdit, "txt_name")
        self.email = self.findChild(QLineEdit, "txt_email")
        self.password = self.findChild(QLineEdit, "txt_password")
        self.confirm_password = self.findChild(QLineEdit, "txt_conf_pwd")
        self.btn_register = self.findChild(QPushButton, "btn_register")
        self.btn_login = self.findChild(QPushButton, "btn_login")
        self.btn_eye_p = self.findChild(QPushButton, "btn_eye_p")
        self.btn_eye_cp = self.findChild(QPushButton, "btn_eye_cp")

        self.btn_register.clicked.connect(self.register)
        self.btn_login.clicked.connect(self.show_login)
        self.btn_eye_p.clicked.connect(lambda: self.hiddenOrShow(self.password, self.btn_eye_p))
        self.btn_eye_cp.clicked.connect(lambda: self.hiddenOrShow(self.confirm_password, self.btn_eye_cp))

    def hiddenOrShow(self, input: QLineEdit, btn: QPushButton):
        if input.echoMode() == QLineEdit.EchoMode.Password:
            input.setEchoMode(QLineEdit.EchoMode.Normal)
            btn.setIcon(QIcon("img/eye-solid.jpg"))
        else:
            input.setEchoMode(QLineEdit.EchoMode.Password)
            btn.setIcon(QIcon("img/eye-slash-solid.jpg"))

    def register(self):
        msg = MessageBox()
        name = self.name.text().strip()
        email = self.email.text().strip()
        password = self.password.text().strip()
        confirm_password = self.confirm_password.text().strip()

        if "" in [name, email, password, confirm_password]:
            msg.error_box("Không thể để trống")
            return

        if password != confirm_password:
            msg.error_box("Mật khẩu không trùng khớp")
            return

        if not self.validate_email(email):
            msg.error_box("Email không hợp lệ")
            return

        if get_user_by_email(email):
            msg.error_box("Email đã tồn tại")
            return

        msg.success_box("Đăng ký thành công")
        self.show_login()

    def validate_email(self, s):
        idx = s.find("@")
        return idx != -1 and '.' in s[idx + 1:]

    def show_login(self):
        self.login = Login()
        self.login.show()
        self.close()

class Home(QMainWindow):
    def __init__(self, user_id):
        super().__init__()
        uic.loadUi("ui/mainwindow.ui", self)
        
        self.msg = MessageBox()

        self.user_id = user_id
        self.user = get_user_by_id(user_id)
        self.loadAccountInfo()

        self.txt_name = self.findChild(QLineEdit, "txt_name")
        self.txt_email = self.findChild(QLineEdit, "txt_email")
        self.main_widget = self.findChild(QStackedWidget, "main_widget")

        self.btn_nav_home = self.findChild(QPushButton, "btn_nav_home")
        self.btn_nav_account = self.findChild(QPushButton, "btn_nav_account")
        self.btn_flash_sale = self.findChild(QPushButton, "btn_flash_sale")
        self.btn_avatar = self.findChild(QPushButton, "btn_avatar")
        self.image_button = self.findChild(QLabel, "image_button")
        self.btn_update_info = self.findChild(QPushButton, "update_user")

        self.btn_avatar.clicked.connect(self.update_avatar)
        self.btn_nav_home.clicked.connect(lambda: self.navMainScreen(0))
        self.btn_flash_sale.clicked.connect(lambda: self.navMainScreen(1))
        self.btn_nav_account.clicked.connect(lambda: self.navMainScreen(2))
        self.btn_update_info.clicked.connect(self.update_info)

    def navMainScreen(self, index):
        self.main_widget.setCurrentIndex(index)

    def loadAccountInfo(self):
        self.txt_name = self.findChild(QLineEdit,"txt_name")
        self.txt_email = self.findChild(QLineEdit,"txt_email")
        self.txt_age = self.findChild(QLineEdit,"txt_age")
        self.cb_gender = self.findChild(QComboBox,"cb_gender")
        self.txt_birthday = self.findChild(QDateEdit,"txt_birthday")
        self.txt_birthday.setDisplayFormat("dd/MM/yyyy")
        self.txt_age.setValidator(QIntValidator())

        if self.user["avatar"]:
            self.image_button.setPixmap(QPixmap(self.user["avatar"]))

        self.txt_name.setText(self.user["name"])
        self.txt_email.setText(self.user["email"])
        self.txt_age.setText(self.user["age"])
        self.txt_birthday.setDate(QDate.fromString(self.user["birthday"], "dd/MM/yyyy"))
        
        if not self.user["gender"]:
            self.cb_gender.setCurrentIndex(0)
        elif self.user["gender"] == "Nam":
            self.cb_gender.setCurrentIndex(1)
        elif self.user["gender"] == "Nữ":
            self.cb_gender.setCurrentIndex(2)
        else:
            self.cb_gender.setCurrentIndex(3)

    def update_avatar(self):
            file, _ = QFileDialog.getOpenFileName(self, "Chọn ảnh đại diện", "", "Images (*.png *.jpg *.jpeg)")
            if file:
                self.user["avatar"] = file
                self.image_button.setPixmap(QPixmap(file))
                update_avatar_user(self.user_id, file)
                
    def update_info(self):
        name = self.txt_name.text().strip()
        email = self.txt_email.text().strip()
        gender = self.cb_gender.currentText()
        birthday = self.txt_birthday.text().strip()
        age = self.txt_age.text().strip()
        
        update_user(self.user_id, name, email, gender, birthday, age)
        self.msg.success_box("Cập nhật thông tin thành công")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(app.exec())