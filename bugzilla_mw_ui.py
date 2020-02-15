# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bugzilla_mw.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Bugzilla_MW(object):
    def setupUi(self, Bugzilla_MW):
        if Bugzilla_MW.objectName():
            Bugzilla_MW.setObjectName(u"Bugzilla_MW")
        Bugzilla_MW.resize(557, 474)
        self.action_login = QAction(Bugzilla_MW)
        self.action_login.setObjectName(u"action_login")
        self.action_config = QAction(Bugzilla_MW)
        self.action_config.setObjectName(u"action_config")
        self.action_config.setCheckable(True)
        self.centralwidget = QWidget(Bugzilla_MW)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 0, 270, 380))
        self.groupBox.setMaximumSize(QSize(280, 380))
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.cb_product = QComboBox(self.groupBox)
        self.cb_product.setObjectName(u"cb_product")
        self.cb_product.setMinimumSize(QSize(250, 22))
        self.cb_product.setMaximumSize(QSize(250, 22))
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(8)
        font1.setBold(True)
        font1.setWeight(75)
        self.cb_product.setFont(font1)
        self.cb_product.setEditable(True)
        self.cb_product.setFrame(True)
        self.cb_product.setModelColumn(0)

        self.verticalLayout.addWidget(self.cb_product)

        self.lw_products = QListWidget(self.groupBox)
        self.lw_products.setObjectName(u"lw_products")
        self.lw_products.setMinimumSize(QSize(250, 250))
        self.lw_products.setMaximumSize(QSize(250, 250))
        self.lw_products.setFont(font1)

        self.verticalLayout.addWidget(self.lw_products)

        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_clear_product = QPushButton(self.widget)
        self.btn_clear_product.setObjectName(u"btn_clear_product")
        self.btn_clear_product.setMaximumSize(QSize(100, 30))

        self.gridLayout.addWidget(self.btn_clear_product, 0, 0, 1, 1)

        self.le_product_count = QLineEdit(self.widget)
        self.le_product_count.setObjectName(u"le_product_count")
        self.le_product_count.setEnabled(False)

        self.gridLayout.addWidget(self.le_product_count, 0, 2, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(8)
        self.label.setFont(font2)

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.widget)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(260, 0, 270, 380))
        self.groupBox_2.setMaximumSize(QSize(280, 380))
        self.groupBox_2.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.cb_status = QComboBox(self.groupBox_2)
        self.cb_status.setObjectName(u"cb_status")
        self.cb_status.setMinimumSize(QSize(250, 22))
        self.cb_status.setMaximumSize(QSize(250, 22))
        self.cb_status.setFont(font1)
        self.cb_status.setEditable(True)
        self.cb_status.setFrame(True)
        self.cb_status.setModelColumn(0)

        self.verticalLayout_3.addWidget(self.cb_status)

        self.lw_status = QListWidget(self.groupBox_2)
        self.lw_status.setObjectName(u"lw_status")
        self.lw_status.setMinimumSize(QSize(250, 250))
        self.lw_status.setMaximumSize(QSize(250, 250))
        self.lw_status.setFont(font1)

        self.verticalLayout_3.addWidget(self.lw_status)

        self.widget_3 = QWidget(self.groupBox_2)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_3 = QGridLayout(self.widget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.btn_clear_status = QPushButton(self.widget_3)
        self.btn_clear_status.setObjectName(u"btn_clear_status")
        self.btn_clear_status.setMaximumSize(QSize(100, 30))

        self.gridLayout_3.addWidget(self.btn_clear_status, 0, 0, 1, 1)

        self.le_status_count = QLineEdit(self.widget_3)
        self.le_status_count.setObjectName(u"le_status_count")
        self.le_status_count.setEnabled(False)

        self.gridLayout_3.addWidget(self.le_status_count, 0, 2, 1, 1)

        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.gridLayout_3.addWidget(self.label_3, 0, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.centralwidget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(10, 380, 521, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_generate = QPushButton(self.widget_4)
        self.btn_generate.setObjectName(u"btn_generate")

        self.horizontalLayout_2.addWidget(self.btn_generate)

        self.le_result_fp = QLineEdit(self.widget_4)
        self.le_result_fp.setObjectName(u"le_result_fp")
        self.le_result_fp.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.le_result_fp)

        self.btn_open_file = QPushButton(self.widget_4)
        self.btn_open_file.setObjectName(u"btn_open_file")

        self.horizontalLayout_2.addWidget(self.btn_open_file)

        Bugzilla_MW.setCentralWidget(self.centralwidget)
        self.toolBar = QToolBar(Bugzilla_MW)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setToolButtonStyle(Qt.ToolButtonIconOnly)
        Bugzilla_MW.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.action_config)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_login)

        self.retranslateUi(Bugzilla_MW)

        self.cb_product.setCurrentIndex(-1)
        self.cb_status.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Bugzilla_MW)
    # setupUi

    def retranslateUi(self, Bugzilla_MW):
        Bugzilla_MW.setWindowTitle(QCoreApplication.translate("Bugzilla_MW", u"Bugzilla Client", None))
        self.action_login.setText(QCoreApplication.translate("Bugzilla_MW", u"\u767b\u5f55", None))
#if QT_CONFIG(tooltip)
        self.action_login.setToolTip(QCoreApplication.translate("Bugzilla_MW", u"\u767b\u5f55bugzilla", None))
#endif // QT_CONFIG(tooltip)
        self.action_config.setText(QCoreApplication.translate("Bugzilla_MW", u"\u914d\u7f6e", None))
#if QT_CONFIG(tooltip)
        self.action_config.setToolTip(QCoreApplication.translate("Bugzilla_MW", u"\u914d\u7f6e\u8d26\u53f7\u4fe1\u606f", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox.setTitle(QCoreApplication.translate("Bugzilla_MW", u"Product Selection", None))
        self.btn_clear_product.setText(QCoreApplication.translate("Bugzilla_MW", u"Clear All", None))
        self.label.setText(QCoreApplication.translate("Bugzilla_MW", u"Count:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Bugzilla_MW", u"Status Selection", None))
        self.btn_clear_status.setText(QCoreApplication.translate("Bugzilla_MW", u"Clear All", None))
        self.label_3.setText(QCoreApplication.translate("Bugzilla_MW", u"Count:", None))
        self.btn_generate.setText(QCoreApplication.translate("Bugzilla_MW", u"\u751f\u6210\u7ed3\u679c", None))
        self.btn_open_file.setText(QCoreApplication.translate("Bugzilla_MW", u"\u6253\u5f00\u6587\u4ef6", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("Bugzilla_MW", u"toolBar", None))
    # retranslateUi

