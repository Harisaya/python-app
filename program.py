from PyQt6 import QtWidgets,QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6 import uic
import sys
from database import *
from cart_item_widget import CartItemWidget
from pro_list_widget import ProductListWidget

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
        self.btn_cart = self.findChild(QPushButton, "btn_cart")
        self.btn_avatar = self.findChild(QPushButton, "btn_avatar")
        self.image_button = self.findChild(QLabel, "image_button")
        self.btn_update_info = self.findChild(QPushButton, "update_user")

        self.btn_avatar.clicked.connect(self.update_avatar)
        self.btn_nav_home.clicked.connect(lambda: self.navMainScreen(1))  # home is index 1
        self.btn_cart.clicked.connect(lambda: self.navMainScreen(0))  # cart is index 0
        self.btn_nav_account.clicked.connect(lambda: self.navMainScreen(3))  # account is index 3
        self.btn_update_info.clicked.connect(self.update_info)
        
        # Initialize product list widget
        self.pro_list_widget = self.findChild(QWidget,"pro_list_widget")
        self.product_list = ProductListWidget()
        
        # Create layout for pro_list_widget
        pro_list_layout = QVBoxLayout(self.pro_list_widget)
        pro_list_layout.setContentsMargins(0, 0, 0, 0)
        pro_list_layout.addWidget(self.product_list)
        
        # Connect product list signals
        self.product_list.product_clicked.connect(self.on_product_clicked)
        self.product_list.product_liked.connect(self.on_product_liked)
        self.product_list.product_buy_now.connect(self.on_product_buy_now)

        # Cart widget
        self.cart_widget = self.findChild(QWidget, "cart_widget")
        self.cart_layout = QVBoxLayout(self.cart_widget)
        self.cart_layout.setContentsMargins(8, 8, 8, 8)
        self.cart_layout.setSpacing(8)
        
        # Connect main_widget signal to auto-load cart
        self.main_widget.currentChanged.connect(self.on_main_window_changed)
        
        # Load cart initially
        self.load_cart()

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
    
    
    def on_product_clicked(self, product_id):
        """Handle product card click"""
        product = get_product_by_id(product_id)
        if product:
            self.fill_detail(product)
            self.navMainScreen(2)  # Chuyển đến trang detail (index 2)

    def fill_detail(self, product):
        # Lấy widget detail (index 2)
        detail_widget = self.main_widget.widget(2)
        
        # Lấy các thành phần theo tên mới trong UI
        img_label = detail_widget.findChild(QLabel, "bannerLabel")
        title_label = detail_widget.findChild(QLabel, "product_info")
        info_label = detail_widget.findChild(QLabel, "product_information")
        price_label = detail_widget.findChild(QLabel, "product_price")
        old_price_label = detail_widget.findChild(QLabel, "original_price")
        rating_label = detail_widget.findChild(QLabel, "rate_star")
        desc_label = detail_widget.findChild(QLabel, "product_description")
        category_label = detail_widget.findChild(QLabel, "category_label")
        add_btn = detail_widget.findChild(QPushButton, "addItemto_wantbuy")
        buy_btn = detail_widget.findChild(QPushButton, "buyItemButton")
        
        # Helper chuyển số
        def safe_float(val):
            try:
                return float(str(val).replace(",", "").strip())
            except:
                return 0.0
        
        # Ảnh sản phẩm
        if product['Image']:
            pixmap = QPixmap(product['Image'])
            if not pixmap.isNull():
                img_label.setPixmap(pixmap.scaled(img_label.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
            else:
                img_label.setText("Không có ảnh")
        else:
            img_label.setText("Không có ảnh")
        
        # Tên sản phẩm
        title_label.setText(product['Name'] or product['Title'])
        
        # Thông tin sản phẩm
        info_label.setText(product['Title'])
        
        # Giá hiện tại
        price = safe_float(product['Price'])
        if price > 0:
            price_label.setText(f"₫{int(price):,}")
        else:
            price_label.setText("Liên hệ")
        
        # Giá gốc
        original_price = safe_float(product['Original_Price'])
        if product['Original_Price'] and original_price > price:
            old_price_label.setText(f"₫{int(original_price):,}")
            old_price_label.setVisible(True)
        else:
            old_price_label.setVisible(False)
        
        # Đánh giá
        rating = safe_float(product['Rate'])
        if rating > 0:
            stars = "⭐" * min(5, int(rating))
            rating_label.setText(f"{stars} {rating:.1f}")
        else:
            rating_label.setText("Chưa có đánh giá")
        
        # Mô tả
        desc_label.setText(product['Description'] or "Không có mô tả")
        
        # Danh mục
        category_label.setText(f"Danh mục: {product['Category'] or 'Không phân loại'}")
        
        # Kết nối nút thêm vào giỏ hàng
        add_btn.clicked.disconnect() if add_btn.receivers(add_btn.clicked) > 0 else None
        add_btn.clicked.connect(lambda: self.add_product_to_cart(product))
        
        # Kết nối nút mua ngay
        buy_btn.clicked.disconnect() if buy_btn.receivers(buy_btn.clicked) > 0 else None
        buy_btn.clicked.connect(lambda: self.buy_product_now(product))

    def on_product_liked(self, product_id):
        """Handle product like button click"""
        self.msg = MessageBox()
        self.msg.success_box(f"Đã thêm sản phẩm ID: {product_id} vào danh sách yêu thích")
        # TODO: Add to favorites list
    
    def on_product_buy_now(self, product_id):
        """Handle product buy now button click"""
        product = get_product_by_id(product_id)
        if product:
            add_to_cart(self.user_id, product)
            self.msg = MessageBox()
            self.msg.success_box("Đã thêm vào giỏ hàng!")
        else:
            self.msg = MessageBox()
            self.msg.error_box("Không tìm thấy sản phẩm")

    def add_product_to_cart(self, product):
        add_to_cart(self.user_id, product)
        self.msg = MessageBox()
        self.msg.success_box("Đã thêm vào giỏ hàng!")

    def buy_product_now(self, product):
        """Handle buy now button click"""
        add_to_cart(self.user_id, product)
        self.msg = MessageBox()
        self.msg.success_box("Đã thêm vào giỏ hàng!")
        # Chuyển đến trang giỏ hàng
        self.navMainScreen(0)

    def on_main_window_changed(self, index):
        # Nếu chuyển sang tab cart (index 0), load lại cart
        if index == 0:
            self.load_cart()

    def load_cart(self):
        """Load cart items from database and display them"""
        # Clear existing widgets
        while self.cart_layout.count():
            item = self.cart_layout.takeAt(0)
            w = item.widget()
            if w:
                w.deleteLater()
        
        # Get cart items from database
        cart_items = get_cart_by_user(self.user_id)
        
        if not cart_items:
            # Show empty cart message
            empty_label = QLabel("Giỏ hàng trống")
            empty_label.setStyleSheet("""
                QLabel {
                    font-family: Arial, sans-serif;
                    font-size: 16px;
                    color: #6c757d;
                    padding: 20px;
                    text-align: center;
                }
            """)
            empty_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.cart_layout.addWidget(empty_label)
        else:
            # Create cart item widgets
            for item in cart_items:
                cart_widget = CartItemWidget(item)
                cart_widget.remove_clicked.connect(lambda pid, uid=self.user_id: self.remove_cart_item(uid, pid))
                cart_widget.buy_now_clicked.connect(lambda pid: self.buy_cart_item(pid))
                self.cart_layout.addWidget(cart_widget)
        
        # Add stretch to push items to top
        self.cart_layout.addStretch()

    def remove_cart_item(self, user_id, product_id):
        remove_from_cart(user_id, product_id)
        self.load_cart()
    
    def buy_cart_item(self, product_id):
        """Handle buy now button click from cart item"""
        self.msg = MessageBox()
        self.msg.success_box(f"Đang xử lý mua sản phẩm ID: {product_id}")
        # TODO: Implement checkout process - for now just show message   

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(app.exec())