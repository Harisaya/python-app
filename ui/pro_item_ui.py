# Form implementation generated from reading ui file '/Users/pinxun/Documents/MindX/PTA/PTA08/BaoChau/python-app/ui/pro_item.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ProductCard(object):
    def setupUi(self, ProductCard):
        ProductCard.setObjectName("ProductCard")
        ProductCard.resize(220, 320)
        ProductCard.setMinimumSize(QtCore.QSize(220, 320))
        ProductCard.setMaximumSize(QtCore.QSize(220, 320))
        ProductCard.setStyleSheet("QWidget#ProductCard {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ffffff, stop:1 #f8f9fa);\n"
"    border: 2px solid #e9ecef;\n"
"    border-radius: 16px;\n"
"    margin: 4px;\n"
"}")
        self.mainLayout = QtWidgets.QVBoxLayout(ProductCard)
        self.mainLayout.setContentsMargins(10, 10, 10, 10)
        self.mainLayout.setSpacing(6)
        self.mainLayout.setObjectName("mainLayout")
        self.imageContainer = QtWidgets.QLabel(parent=ProductCard)
        self.imageContainer.setMinimumSize(QtCore.QSize(200, 150))
        self.imageContainer.setMaximumSize(QtCore.QSize(200, 150))
        self.imageContainer.setStyleSheet("QLabel#imageContainer {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #f8f9fa, stop:1 #e9ecef);\n"
"    border: 1px solid #dee2e6;\n"
"    border-radius: 12px;\n"
"    padding: 8px;\n"
"}")
        self.imageContainer.setText("")
        self.imageContainer.setScaledContents(True)
        self.imageContainer.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.imageContainer.setObjectName("imageContainer")
        self.mainLayout.addWidget(self.imageContainer)
        self.productName = QtWidgets.QLabel(parent=ProductCard)
        self.productName.setStyleSheet("QLabel#productName {\n"
"    font-size: 13px;\n"
"    font-weight: 600;\n"
"    color: #1a1a1a;\n"
"    line-height: 1.3;\n"
"    max-height: 40px;\n"
"}")
        self.productName.setWordWrap(True)
        self.productName.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.productName.setObjectName("productName")
        self.mainLayout.addWidget(self.productName)
        self.priceRow = QtWidgets.QHBoxLayout()
        self.priceRow.setSpacing(6)
        self.priceRow.setObjectName("priceRow")
        self.currentPrice = QtWidgets.QLabel(parent=ProductCard)
        self.currentPrice.setStyleSheet("QLabel#currentPrice {\n"
"    font-family: \'Segoe UI\', Arial, sans-serif;\n"
"    font-size: 18px;\n"
"    font-weight: 700;\n"
"    color: #e74c3c;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #fff5f5, stop:1 #ffe6e6);\n"
"    padding: 6px 10px;\n"
"    border-radius: 8px;\n"
"    border: 1px solid #ffcccc;\n"
"}")
        self.currentPrice.setObjectName("currentPrice")
        self.priceRow.addWidget(self.currentPrice)
        self.oldPrice = QtWidgets.QLabel(parent=ProductCard)
        self.oldPrice.setStyleSheet("QLabel#oldPrice {\n"
"    font-family: \'Segoe UI\', Arial, sans-serif;\n"
"    font-size: 12px;\n"
"    color: #95a5a6;\n"
"    text-decoration: line-through;\n"
"    padding: 4px 0px;\n"
"}")
        self.oldPrice.setObjectName("oldPrice")
        self.priceRow.addWidget(self.oldPrice)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.priceRow.addItem(spacerItem)
        self.mainLayout.addLayout(self.priceRow)
        self.infoRow = QtWidgets.QHBoxLayout()
        self.infoRow.setSpacing(8)
        self.infoRow.setObjectName("infoRow")
        self.ratingDisplay = QtWidgets.QLabel(parent=ProductCard)
        self.ratingDisplay.setStyleSheet("QLabel#ratingDisplay {\n"
"    font-family: \'Segoe UI\', Arial, sans-serif;\n"
"    font-size: 11px;\n"
"    color: #f39c12;\n"
"    font-weight: 600;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #fff8e1, stop:1 #ffeaa7);\n"
"    padding: 4px 8px;\n"
"    border-radius: 6px;\n"
"    border: 1px solid #fdcb6e;\n"
"}")
        self.ratingDisplay.setObjectName("ratingDisplay")
        self.infoRow.addWidget(self.ratingDisplay)
        self.salesCount = QtWidgets.QLabel(parent=ProductCard)
        self.salesCount.setStyleSheet("QLabel#salesCount {\n"
"    font-family: \'Segoe UI\', Arial, sans-serif;\n"
"    font-size: 10px;\n"
"    color: #7f8c8d;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #f8f9fa, stop:1 #e9ecef);\n"
"    padding: 4px 8px;\n"
"    border-radius: 6px;\n"
"    border: 1px solid #dee2e6;\n"
"}")
        self.salesCount.setObjectName("salesCount")
        self.infoRow.addWidget(self.salesCount)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.infoRow.addItem(spacerItem1)
        self.mainLayout.addLayout(self.infoRow)
        self.actionRow = QtWidgets.QHBoxLayout()
        self.actionRow.setSpacing(8)
        self.actionRow.setObjectName("actionRow")
        self.buyNowBtn = QtWidgets.QPushButton(parent=ProductCard)
        self.buyNowBtn.setMinimumSize(QtCore.QSize(0, 36))
        self.buyNowBtn.setStyleSheet("QPushButton#buyNowBtn {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #27ae60, stop:1 #2ecc71);\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    font-family: \'Segoe UI\', Arial, sans-serif;\n"
"    font-size: 12px;\n"
"    font-weight: 600;\n"
"    padding: 10px 16px;\n"
"}\n"
"\n"
"QPushButton#buyNowBtn:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #229954, stop:1 #27ae60);\n"
"}\n"
"\n"
"QPushButton#buyNowBtn:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #1e8449, stop:1 #229954);\n"
"}")
        self.buyNowBtn.setObjectName("buyNowBtn")
        self.actionRow.addWidget(self.buyNowBtn)
        self.likeBtn = QtWidgets.QPushButton(parent=ProductCard)
        self.likeBtn.setMinimumSize(QtCore.QSize(36, 36))
        self.likeBtn.setMaximumSize(QtCore.QSize(36, 36))
        self.likeBtn.setStyleSheet("QPushButton#likeBtn {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ecf0f1, stop:1 #bdc3c7);\n"
"    border: 1px solid #bdc3c7;\n"
"    border-radius: 8px;\n"
"    font-size: 16px;\n"
"    color: #7f8c8d;\n"
"}\n"
"\n"
"QPushButton#likeBtn:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #e74c3c, stop:1 #c0392b);\n"
"    color: white;\n"
"    border-color: #c0392b;\n"
"}\n"
"\n"
"QPushButton#likeBtn:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #c0392b, stop:1 #a93226);\n"
"}")
        self.likeBtn.setObjectName("likeBtn")
        self.actionRow.addWidget(self.likeBtn)
        self.mainLayout.addLayout(self.actionRow)

        self.retranslateUi(ProductCard)
        QtCore.QMetaObject.connectSlotsByName(ProductCard)

    def retranslateUi(self, ProductCard):
        _translate = QtCore.QCoreApplication.translate
        ProductCard.setWindowTitle(_translate("ProductCard", "Product Card"))
        self.productName.setText(_translate("ProductCard", "Tên sản phẩm"))
        self.currentPrice.setText(_translate("ProductCard", "₫199K"))
        self.oldPrice.setText(_translate("ProductCard", "₫299K"))
        self.ratingDisplay.setText(_translate("ProductCard", "⭐⭐⭐⭐⭐ 4.8"))
        self.salesCount.setText(_translate("ProductCard", "Đã bán 2.5k"))
        self.buyNowBtn.setText(_translate("ProductCard", "🛒 Mua ngay"))
        self.likeBtn.setText(_translate("ProductCard", "💖"))
