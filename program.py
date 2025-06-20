from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6 import uic
import sys
from database import *

class MessageBox():
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

        if email == "":
            msg.error_box("không thể để trống")
            self.email.setFocus()
            return

        if password == "":
            msg.error_box("không thể để trống")
            self.password.setFocus()
            return

        user = get_user_by_email_and_password(email, password)
        if user is not None:
            msg.success_box("Đăng nhập thành công")
            self.show_home(user["id"])
            return

        msg.error_box("Đăng nhập thất bại")

    def show_home(self, user_id):
        self.home = Home(user_id)
        self.home.show()
        self.close()

    def show_register(self):
        self.register = Register()
        self.register.show()
        self.close()

class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/resgin.ui", self)

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

        if name == "":
            msg.error_box("Không thể để trống")
            self.name.setFocus()
            return

        if email == "":
            msg.error_box("Không thể để trống")
            self.email.setFocus()
            return

        if password == "":
            msg.error_box("Không thể để trống")
            self.password.setFocus()
            return

        if confirm_password == "":
            msg.error_box("Không thể để trống")
            self.confirm_password.setFocus()
            return

        if password != confirm_password:
            msg.error_box("Mật khẩu không trùng khớp")
            self.password.setFocus()
            return

        if not self.validate_email(email):
            msg.error_box("Email không hợp lệ")
            self.email.setFocus()
            return

        if get_user_by_email(email) is not None:
            msg.error_box("Email đã tồn tại")
            return

    def validate_email(self, s):
        idx_at = s.find("@")
        if idx_at == -1:
            return False
        return '.' in s[idx_at + 1:]

    def show_login(self):
        self.login = Login()
        self.login.show()
        self.close()

class Home(QMainWindow):
    def __init__(self, user_id):
        super().__init__()
        uic.loadUi("ui/mainwindow.ui", self)

        self.txt_name = self.findChild(QLineEdit, "txt_name")
        self.txt_email = self.findChild(QLineEdit, "txt_email")
        
        self.user_id = user_id
        self.user = get_user_by_id(user_id)

        self.main_widget = self.findChild(QStackedWidget, "main_widget")
        self.btn_nav_account = self.findChild(QPushButton, "btn_nav_account")
        self.btn_nav_home = self.findChild(QPushButton, "btn_nav_home")
        self.btn_flash_sale = self.findChild(QPushButton, "btn_flash_sale")

        self.btn_avatar = self.findChild(QPushButton, "btn_avatar")
        self.btn_avatar.clicked.connect(self.update_avatar)

        self.btn_nav_home.clicked.connect(lambda: self.navMainScreen(0))
        self.btn_flash_sale.clicked.connect(lambda: self.navMainScreen(1))
        self.btn_nav_account.clicked.connect(lambda: self.navMainScreen(2))

    def navMainScreen(self, index):
        self.main_widget.setCurrentIndex(index)

    def update_avatar(self):
        file = QFileDialog.getOpenFileName(self, "Chọn ảnh đại diện", "", "Images (*.png *.jpg *.jpeg)")[0]
        if file:
            self.user_id["avatar"] = file
            self.btn_avatar.setIcon(QIcon(file))
            update_avatar_user(self.user_id, file)
            MessageBox().success_box("Cập nhật ảnh đại diện thành công")

    def update_info(self):
        name = self.txt_name.text().strip()
        email = self.txt_email.text().strip()
        age = self.txt_age.text().strip()
        if self.user is None:
            MessageBox().error_box("Không tìm thấy người dùng")
            return

        if name == "":
            MessageBox().error_box("Không thể để trống tên")
            self.txt_name.setFocus()
            return

        if email == "":
            MessageBox().error_box("Không thể để trống email")
            self.txt_email.setFocus()
            return

        if not self.validate_email(email):
            MessageBox().error_box("Email không hợp lệ")
            self.txt_email.setFocus()
            return

        if get_user_by_email(email) is not None and get_user_by_email(email)["id"] != self.user_id:
            MessageBox().error_box("Email đã tồn tại")
            return

        update_user_info(self.user_id, name, email)
        MessageBox().success_box("Cập nhật thông tin thành công")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(app.exec())