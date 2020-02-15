# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 20:39
# @Author  : Liu Gang
# @Site    : 
# @File    : main_opr.py
# @Software: PyCharm
import sys
import json
import os

from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2.QtCore import Slot

from bugzilla_mw_ui import Ui_Bugzilla_MW
from config_dlg_ui import Ui_CfgDlg
from bugzilla import Bugzilla


def get_json_config(json_file):
    with open(json_file, "r") as config_fp:
        config_dict = json.load(config_fp)

    return config_dict


def set_json_config(config_dict, json_file):
    with open(json_file, "w") as config_fp:
        json.dump(config_dict, config_fp, indent=4)

    return True


class ConfigDlg(QtWidgets.QDialog):
    def __init__(self):
        super(ConfigDlg, self).__init__()
        self.ui = Ui_CfgDlg()
        self.ui.setupUi(self)
        self.ui.btnbox_config.accepted.connect(self.save)
        self.ui.btnbox_config.rejected.connect(self.cancel)
        self.config_dict = dict()
        # init dlg
        self.load_config()

    def load_config(self):
        self.config_dict = get_json_config("config/account.json")
        self.ui.le_user.setText(self.config_dict["user"])
        self.ui.le_pwd.setText(self.config_dict["pwd"])

    def save(self):
        self.config_dict["user"] = self.ui.le_user.text()
        self.config_dict["pwd"] = self.ui.le_pwd.text()
        set_json_config(self.config_dict, "config/account.json")
        self.close()

    def cancel(self):
        self.close()


class BugzillaWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(BugzillaWindow, self).__init__()
        self.ui = Ui_Bugzilla_MW()
        self.ui.setupUi(self)
        # Set Window ICON
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icon/bugzilla.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon)

        self.cfg_dlg = ConfigDlg()
        self.bug = Bugzilla(self.cfg_dlg.config_dict["user"], self.cfg_dlg.config_dict["pwd"])
        self.product_list = list()
        self.status_list = list()

    @staticmethod
    def msg_box(info_str, title_str="提示", btn_type=True):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle(title_str)
        msg.setText(info_str)
        if btn_type is True:
            msg.addButton(QtWidgets.QMessageBox.Ok).setText(u"是")
            msg.addButton(QtWidgets.QMessageBox.No).setText(u"否")
            ret = msg.exec_()
            if ret == QtWidgets.QMessageBox.Ok:
                return True
            elif ret == QtWidgets.QMessageBox.No:
                return False
        else:
            msg.exec_()

    def init_devices(self):
        product_dict = get_json_config("config/product.json")
        self.product_list = product_dict["product_list"].split(",")
        self.ui.cb_product.addItems(self.product_list)
        self.ui.cb_product.setCurrentIndex(-1)

        status_dict = get_json_config("config/status.json")
        self.status_list = status_dict["status_list"].split(",")
        self.ui.cb_status.addItems(self.status_list)
        self.ui.cb_status.setCurrentIndex(-1)

        sel_prod_list = get_json_config("config/selected_products.json")["selected_products"].split(",")
        for prod in sel_prod_list:
            self.slot_product_choice(prod)

        sel_stat_list = get_json_config("config/selected_status.json")["selected_status"].split(",")
        for stat in sel_stat_list:
            self.slot_status_choice(stat)

    def slots_connect(self):
        self.ui.action_config.triggered.connect(self.slot_config_action)
        self.ui.action_login.triggered.connect(self.slot_login)

        self.ui.cb_product.textActivated.connect(self.slot_product_choice)
        self.ui.lw_products.itemDoubleClicked.connect(self.slot_remove_product)
        self.ui.btn_clear_product.clicked.connect(self.slot_remove_all_product)

        self.ui.cb_status.textActivated.connect(self.slot_status_choice)
        self.ui.lw_status.itemDoubleClicked.connect(self.slot_remove_status)
        self.ui.btn_clear_status.clicked.connect(self.slot_remove_all_status)

        self.ui.btn_generate.clicked.connect(self.slot_btn_generate)
        self.ui.btn_open_file.clicked.connect(self.slot_btn_open)

    @Slot()
    def slot_config_action(self):
        self.cfg_dlg.exec_()
        self.bug.set_user_pwd(self.cfg_dlg.config_dict["user"], self.cfg_dlg.config_dict["pwd"])

    @Slot()
    def slot_login(self):
        ret = self.bug.login()
        if ret:
            msg_str = "登录成功"
        else:
            msg_str = "登录失败"

        self.msg_box(msg_str, btn_type=False)

    @Slot()
    def slot_product_choice(self, item_text):
        product_list = list()
        # selected_product = self.ui.cb_product.currentText()
        selected_product = item_text

        if selected_product.endswith("*"):
            self.ui.cb_product.removeItem(self.ui.cb_product.findText(selected_product))
            item_count = self.ui.cb_product.count()
            for cnt in range(item_count):
                product = self.ui.cb_product.itemText(cnt)
                if product.startswith(selected_product.replace("*", "")):
                    # print(product, cnt)
                    product_list.append(product)

            if len(product_list) == 0:
                self.msg_box(f"{selected_product} not in list!", btn_type=False)
                self.ui.cb_product.clearEditText()
                return

        elif self.product_list.count(selected_product) == 0:
            self.msg_box(f"{selected_product} not in list!", btn_type=False)
            self.ui.cb_product.removeItem(self.ui.cb_product.findText(selected_product))
            self.ui.cb_product.clearEditText()
            return

        if len(product_list) == 0:
            product_list = [selected_product]
        # print(len(product_list))
        for product in product_list:
            self.ui.lw_products.addItem(product)
            self.ui.cb_product.removeItem(self.ui.cb_product.findText(product))

        self.slot_product_count()
        self.ui.cb_product.clearEditText()

    @Slot()
    def slot_remove_product(self, item):
        self.ui.lw_products.takeItem(self.ui.lw_products.row(item))
        self.ui.cb_product.addItem(item.text())
        self.slot_product_count()

    @Slot()
    def slot_remove_all_product(self):
        count = int(self.ui.le_product_count.text())
        for lw_index in range(count):
            lw_item = self.ui.lw_products.item(0)
            self.slot_remove_product(lw_item)

    @Slot()
    def slot_product_count(self):
        self.ui.le_product_count.setText(str(self.ui.lw_products.count()))

    @Slot()
    def slot_status_choice(self, item_text):
        status_list = list()
        # selected_status = self.ui.cb_status.currentText()
        selected_status = item_text

        if selected_status.endswith("*"):
            self.ui.cb_status.removeItem(self.ui.cb_status.findText(selected_status))
            item_count = self.ui.cb_status.count()
            for cnt in range(item_count):
                status = self.ui.cb_status.itemText(cnt)
                if status.startswith(selected_status.replace("*", "")):
                    # print(status, cnt)
                    status_list.append(status)

            if len(status_list) == 0:
                self.msg_box(f"{selected_status} not in list!", btn_type=False)
                self.ui.cb_status.clearEditText()
                return

        elif self.status_list.count(selected_status) == 0:
            self.msg_box(f"{selected_status} not in list!", btn_type=False)
            self.ui.cb_status.removeItem(self.ui.cb_status.findText(selected_status))
            self.ui.cb_status.clearEditText()
            return

        if len(status_list) == 0:
            status_list = [selected_status]
        # print(len(status_list))
        for status in status_list:
            self.ui.lw_status.addItem(status)
            self.ui.cb_status.removeItem(self.ui.cb_status.findText(status))

        self.slot_status_count()
        self.ui.cb_status.clearEditText()

    @Slot()
    def slot_remove_status(self, item):
        self.ui.lw_status.takeItem(self.ui.lw_status.row(item))
        self.ui.cb_status.addItem(item.text())
        self.slot_status_count()

    @Slot()
    def slot_remove_all_status(self):
        count = int(self.ui.le_status_count.text())
        for lw_index in range(count):
            lw_item = self.ui.lw_status.item(0)
            self.slot_remove_status(lw_item)

    @Slot()
    def slot_status_count(self):
        self.ui.le_status_count.setText(str(self.ui.lw_status.count()))

    @Slot()
    def slot_btn_generate(self):
        if self.bug.valid_login() is False:
            self.slot_login()
        product_list = list()
        status_list = list()
        for lw_index in range(self.ui.lw_products.count()):
            lw_text = self.ui.lw_products.item(lw_index).text()
            product_list.append(lw_text)

        for lw_index in range(self.ui.lw_status.count()):
            lw_text = self.ui.lw_status.item(lw_index).text()
            status_list.append(lw_text)

        ret = self.bug.search_bug(status_list, product_list)
        if ret is False:
            self.msg_box("搜索发生错误!", btn_type=False)
        else:
            product_dict = {"selected_products": ",".join(product_list)}
            set_json_config(product_dict, "config/selected_products.json")
            status_dict = {"selected_status": ",".join(status_list)}
            set_json_config(status_dict, "config/selected_status.json")
            self.ui.le_result_fp.setText(ret)

    @Slot()
    def slot_btn_open(self):
        fp = self.ui.le_result_fp.text()
        if fp == "":
            return
        cmd = f"start {fp}"
        # print(cmd)
        os.system(cmd)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = BugzillaWindow()
    form.init_devices()
    form.slots_connect()
    form.show()
    app_ret = app.exec_()
    sys.exit(app_ret)
