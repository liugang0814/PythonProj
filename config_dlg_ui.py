# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'config_dlg.ui'
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


class Ui_CfgDlg(object):
    def setupUi(self, CfgDlg):
        if CfgDlg.objectName():
            CfgDlg.setObjectName(u"CfgDlg")
        CfgDlg.resize(220, 93)
        CfgDlg.setMaximumSize(QSize(220, 93))
        self.formLayout = QFormLayout(CfgDlg)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(CfgDlg)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(40, 20))
        self.label.setMaximumSize(QSize(40, 20))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.le_user = QLineEdit(CfgDlg)
        self.le_user.setObjectName(u"le_user")
        self.le_user.setMinimumSize(QSize(100, 20))
        self.le_user.setMaximumSize(QSize(150, 20))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_user)

        self.label_2 = QLabel(CfgDlg)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(40, 20))
        self.label_2.setMaximumSize(QSize(40, 20))

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.le_pwd = QLineEdit(CfgDlg)
        self.le_pwd.setObjectName(u"le_pwd")
        self.le_pwd.setMinimumSize(QSize(100, 20))
        self.le_pwd.setMaximumSize(QSize(150, 20))
        self.le_pwd.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_pwd)

        self.btnbox_config = QDialogButtonBox(CfgDlg)
        self.btnbox_config.setObjectName(u"btnbox_config")
        self.btnbox_config.setOrientation(Qt.Horizontal)
        self.btnbox_config.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.btnbox_config)


        self.retranslateUi(CfgDlg)
        self.btnbox_config.accepted.connect(CfgDlg.accept)
        self.btnbox_config.rejected.connect(CfgDlg.reject)

        QMetaObject.connectSlotsByName(CfgDlg)
    # setupUi

    def retranslateUi(self, CfgDlg):
        CfgDlg.setWindowTitle(QCoreApplication.translate("CfgDlg", u"Config Dialog", None))
        self.label.setText(QCoreApplication.translate("CfgDlg", u"\u8d26\u53f7:", None))
        self.le_user.setPlaceholderText(QCoreApplication.translate("CfgDlg", u"username", None))
        self.label_2.setText(QCoreApplication.translate("CfgDlg", u"\u5bc6\u7801:", None))
        self.le_pwd.setPlaceholderText(QCoreApplication.translate("CfgDlg", u"password", None))
    # retranslateUi

