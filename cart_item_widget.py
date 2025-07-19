import sys
from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QPixmap
from ui.cart_item_ui import Ui_CartItem
import database


class CartItemWidget(QWidget):
    """
    Cart item widget for displaying products in shopping cart
    """
    
    # Signals for user interactions
    remove_clicked = pyqtSignal(int)    # product_id
    buy_now_clicked = pyqtSignal(int)   # product_id
    
    def __init__(self, cart_item_data=None, parent=None):
        super().__init__(parent)
        
        # Setup UI
        self.ui = Ui_CartItem()
        self.ui.setupUi(self)
        
        # Initialize cart item data
        self.cart_item_data = cart_item_data or {}
        self.product_id = self.cart_item_data.get('product_id', 0)
        
        # Connect signals
        self.ui.removeBtn.clicked.connect(self._on_remove_clicked)
        self.ui.buyNowBtn.clicked.connect(self._on_buy_now_clicked)
        
        # Update display if cart item data is provided
        if cart_item_data:
            self.update_cart_item_data(cart_item_data)
    
    def update_cart_item_data(self, cart_item_data):
        """Update the widget with new cart item data"""
        self.cart_item_data = cart_item_data
        self.product_id = cart_item_data.get('product_id', 0)
        
        # Update product title
        title = cart_item_data.get('title', 'Tên sản phẩm')
        # Allow longer titles for cart items since we have more space
        if len(title) > 120:
            title = title[:117] + "..."
        self.ui.productTitle.setText(title)
        
        # Helper chuyển số
        def safe_float(val):
            try:
                return float(str(val).replace(',', '').strip())
            except Exception:
                return 0.0

        # Update price - handle price format from database
        price_data = cart_item_data.get('price', 0)
        if price_data:
            # Handle price that might be string with "đ" or numeric
            if isinstance(price_data, str):
                # Remove "đ" and convert to float
                price_str = price_data.replace('đ', '').replace(',', '').strip()
                try:
                    price = float(price_str)
                    price_text = self._format_price(price)
                    self.ui.productPrice.setText(f"₫{price_text}")
                except ValueError:
                    self.ui.productPrice.setText(price_data)  # Show original if can't parse
            else:
                # Numeric price
                price = safe_float(price_data)
                if price > 0:
                    price_text = self._format_price(price)
                    self.ui.productPrice.setText(f"₫{price_text}")
                else:
                    self.ui.productPrice.setText("Liên hệ")
        else:
            self.ui.productPrice.setText("Liên hệ")
        
        # Update quantity
        quantity = cart_item_data.get('quantity', 1)
        self.ui.quantityLabel.setText(f"Số lượng: {quantity}")
        
        # Update image
        image_path = cart_item_data.get('img', '')
        self._load_product_image(image_path)
    
    def _format_price(self, price):
        """Format price with K/M suffix"""
        # Convert price to float if it's a string
        try:
            price = float(price)
        except (ValueError, TypeError):
            price = 0.0
            
        if price >= 1000000:
            return f"{price/1000000:.1f}M"
        elif price >= 1000:
            return f"{price/1000:.0f}K"
        else:
            return str(int(price))
    
    def _load_product_image(self, image_path):
        """Load and display product image"""
        if image_path:
            try:
                pixmap = QPixmap(image_path)
                if not pixmap.isNull():
                    # Scale pixmap to fit the container while maintaining aspect ratio
                    scaled_pixmap = pixmap.scaled(
                        self.ui.productImage.size(),
                        Qt.AspectRatioMode.KeepAspectRatio,
                        Qt.TransformationMode.SmoothTransformation
                    )
                    self.ui.productImage.setPixmap(scaled_pixmap)
                else:
                    self._set_default_image()
            except Exception as e:
                print(f"Error loading image {image_path}: {e}")
                self._set_default_image()
        else:
            self._set_default_image()
    
    def _set_default_image(self):
        """Set default placeholder image"""
        self.ui.productImage.setText("🖼️\nKhông có ảnh")
        self.ui.productImage.setStyleSheet("""
            QLabel#productImage {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #f8f9fa, stop:1 #e9ecef);
                border: 1px solid #dee2e6;
                border-radius: 8px;
                padding: 4px;
                font-size: 14px;
                color: #6c757d;
                font-weight: 500;
                text-align: center;
            }
        """)
    
    def _on_remove_clicked(self):
        """Handle remove button click"""
        self.remove_clicked.emit(self.product_id)
    
    def _on_buy_now_clicked(self):
        """Handle buy now button click"""
        self.buy_now_clicked.emit(self.product_id)


# Example usage and testing
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Create a sample cart item
    sample_cart_item = {
        'product_id': 1,
        'title': 'Ví nam Playboy kẻ, Combo Ví da nam nhỏ gọn & Bọc Căn Cước Công Dân DODANA dáng ngang da PU',
        'price': 1900,
        'quantity': 2,
        'img': 'img_pro/vi.webp'
    }
    
    # Create and show the widget
    widget = CartItemWidget(sample_cart_item)
    widget.show()
    
    # Connect signals for testing
    widget.remove_clicked.connect(lambda product_id: print(f"Remove: Product {product_id}"))
    widget.buy_now_clicked.connect(lambda product_id: print(f"Buy now: Product {product_id}"))
    
    sys.exit(app.exec()) 