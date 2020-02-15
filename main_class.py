#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-11-7 下午10:25
# @Author  : Liu Gang
# @Site    : 
# @File    : main_class.py
# @Software: PyCharm
import requests
import datetime
import time
import wx
import os
import threading
import xlrd
import xlwt
# from collections import OrderedDict
from pandas import DataFrame
from pandas import ExcelWriter
# from bs4 import BeautifulSoup
from wx_ui import BugzillaFrame


def time_conv(str_time):
    date_time = datetime.datetime.strptime(str_time, "%Y-%m-%dT%H:%M:%SZ")
    # print(date_time,type(date_time))
    modfiy_datetime = date_time + datetime.timedelta(hours=8)
    # print(modfiy_datetime)
    # t_str = date_time.strftime("%Y-%m-%d %H:%M:%S")
    t_str = modfiy_datetime.strftime("%Y-%m-%d %H:%M:%S")
    return t_str


def gettime(time_format=0):
    """
    get system current time
    :param time_format: the format for return value
    :return:
    """
    if time_format == 0:
        return time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    elif time_format == 1:
        return time.strftime("%Y%m%d", time.localtime(time.time()))
    elif time_format == 2:
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    else:
        return None


class Bugzilla:
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd
        self.login_url = "https://bugzilla.unisoc.com/bugzilla/rest/login?login=%s&password=%s" % (user, pwd)
        self.url_base = "https://bugzilla.unisoc.com/bugzilla"
        self.session = requests.session()
        self.id = int()
        self.token = ""
        self.token_str = ""

    def __del__(self):
        self.session.close()

    def login(self):
        result = self.session.get(self.login_url)
        # print(self.login_url)
        if result.status_code != 200:
            print("Connect Fail!")
            return False

        ret = result.json()
        # print(ret)
        self.id = ret["id"]
        self.token = ret["token"]
        self.token_str = "&token=" + self.token
        # print("Login Success!")

        return True

    def valid_login(self):
        url = self.url_base + "/rest/valid_login?login=%s&token=%s" % (self.user, self.token)
        print(url)
        result = self.session.get(url)
        print(result.json())

    def logout(self):
        url = self.url_base + "/rest/logout?token=%s" % self.token
        result = self.session.get(url)
        print(result.json())

    def get_user(self):
        url = self.url_base + "/rest/user/1?include_fields=id,name"
        result = self.session.get(url)
        print(result.json())

    def get_bug(self, id_list):
        id_str_list = map(lambda x: str(x), id_list)
        url = self.url_base + "/rest/bug?id="
        id_str = ",".join(id_str_list)
        # print(id_str)
        url = url + id_str
        result = self.session.get(url + self.token_str)

        result_dict = result.json()

        # for x in result_dict:
        #     print(x,result_dict[x])

        bugs_dict = result_dict["bugs"]

        ret_list = list()

        # for x in bugs_dict[0]:
        #     print(x,bugs_dict[0][x])

        for bugs_num in range(len(bugs_dict)):
            # for x in bugs_dict[bugs_num]:
            #     print(x,bugs_dict[bugs_num][x])

            bug_id = bugs_dict[bugs_num]["id"]
            bug_status = bugs_dict[bugs_num]["status"]
            bug_needinfodate = bugs_dict[bugs_num]["cf_needinfodate"]
            bug_asignee = bugs_dict[bugs_num]["assigned_to"]
            bug_creationdate = time_conv(bugs_dict[bugs_num]["creation_time"])
            # bug_asigndate = bugs_dict[bugs_num]["cf_assigneddate"]
            # bug_dict = OrderedDict()
            if bug_needinfodate is not None:
                t_str = time_conv(bug_needinfodate)
            else:
                t_str = ""

            bug_dict = {
                "id": bug_id,
                "status": bug_status,
                # "needinfo_date": bug_needinfodate,
                "needinfo_date": t_str,
                "asignee": bug_asignee,
                "creation_date": bug_creationdate
                # "asign_date": bug_asigndate
            }
            ret_list.append(bug_dict)

        # print(ret_list)
        df = DataFrame(ret_list)
        # print(df)
        # return ret_list
        return df

    def bug_history(self, id_str):
        url = self.url_base + "/rest/bug/%s/history?token=%s" % (id_str, self.token)
        print(url)
        result = self.session.get(url)
        result_dict = result.json()
        bug_history = result_dict["bugs"][0]["history"]

        ret_list = list()
        for d in bug_history:
            # print(d)
            # df = DataFrame(d["changes"])
            # print(df.loc[df.field_name=="assigned_to"])
            for x in d["changes"]:
                # print(x)

                if x["field_name"] == 'assigned_to':
                    print(x)
                    change_when = d["when"]
                    change_assignee = x["added"]
                    t_str = time_conv(change_when)

                    change_dict = {
                        # "assign_date": change_when,
                        "assign_date": t_str,
                        "assignee": change_assignee
                    }
                    ret_list.append(change_dict)
                    break

                if x["field_name"] == 'cf_assigneddate':
                    print(x)
                    change_when = d["when"]
                    # change_assignee = x["added"]
                    t_str = time_conv(change_when)
                    change_dict = dict()
                    try:
                        change_dict = {
                            "assign_date": t_str,
                            "assignee": ret_list[-1]["assignee"]
                        }
                    except IndexError:
                        change_dict = {
                            "assign_date": t_str,
                            "assignee": d["who"]
                        }
                    ret_list.append(change_dict)
                    break

                if x["added"] == 'Assigned' and x["removed"] != 'NEW':
                    print(x)
                    print(x["added"], x["removed"])
                    change_when = d["when"]
                    # change_assignee = x["added"]
                    t_str = time_conv(change_when)
                    change_dict = dict()
                    try:
                        change_dict = {
                            "assign_date": t_str,
                            "assignee": ret_list[-1]["assignee"]
                        }
                    except IndexError:
                        change_dict = {
                            "assign_date": t_str,
                            "assignee": d["who"]
                        }
                    ret_list.append(change_dict)
                    break

        df = DataFrame(ret_list)
        return df


class QueryFrame(BugzillaFrame):
    def __init__(self, parent):
        super(QueryFrame, self).__init__(parent)
        self.bug_id_path = ""
        self.b_exit = False
        self.bug_list_file = "bug_list.xls"
        self.gen_file = ""
        self.bug_list = list()
        self.m_btn_gen.Disable()
        self.m_btn_open.Disable()
        self.thr_con = threading.Condition()
        thr = threading.Thread(target=self.main_thr)
        thr.setDaemon(True)
        thr.start()

    def on_close(self, event):
        self.b_exit = True
        self.thr_con.acquire()
        self.thr_con.notify()
        self.thr_con.release()
        event.Skip()

    def on_list_sel(self, event):
        self.Show(False)
        self.m_gd_list.ClearGrid()

        if os.path.exists(self.bug_list_file):
            os.remove(self.bug_list_file)

        book = xlwt.Workbook()
        book.add_sheet('bug_list')
        book.save(self.bug_list_file)
        os.system("%s" % self.bug_list_file)
        self.Show(True)
        # self.fill_grid()
        self.m_text_info.AppendText("- Confirm Bug ID Excel Save success.\n")
        self.m_text_info.AppendText("- Please DOUBLE CLICK the sheet label\n")

    def on_gen(self, event):
        self.thr_con.acquire()
        self.thr_con.notify()
        self.thr_con.release()
        event.Skip()

    def on_list_fill(self, event):
        self.m_gd_list.ClearGrid()
        ret = self.fill_grid()
        if ret == 0:
            self.m_text_info.AppendText("- Bug ID Get ERROR\n")
        else:
            self.m_text_info.AppendText("- Bug ID Get Success\n")
            self.m_text_info.AppendText("- Total Count:%d\n" % ret)
            self.m_btn_gen.Enable()

    def fill_grid(self):
        xl_rd = xlrd.open_workbook(self.bug_list_file)

        tb = xl_rd.sheet_by_name('bug_list')

        bug_list = tb.col_values(0)
        # print(bug_list)
        self.bug_list = []
        rows_cnt = 0
        for x in bug_list:
            try:
                self.bug_list.append(int(x))
                self.m_gd_list.SetCellValue(rows_cnt, 0, "%d" % x)
                rows_cnt += 1
            except Exception as e:
                print(e)
                continue
        print(self.bug_list)
        return rows_cnt

    def on_open(self, event):
        self.m_btn_open.Disable()
        os.system("start %s" % self.gen_file)
        self.m_text_info.AppendText("- Query Result Open Success!\n")
        event.Skip()

    def main_thr(self):
        bz = Bugzilla("icecream.ma", "123@abAB")
        ret = bz.login()
        if ret is True:
            self.m_text_info.AppendText("- Login Success!\n")

        while True:
            self.thr_con.acquire()
            self.thr_con.wait()
            self.thr_con.release()

            if self.b_exit is True:
                break
            print("calculating")
            df = bz.get_bug(self.bug_list)
            if len(df) == 0:
                self.m_text_info.AppendText("- Bug List Get Fail!\n")
                continue

            self.m_text_info.AppendText("- Bug List Get Success!\n")

            columns_list = ["id", "status", "creation_date", "needinfo_date", "asignee", "asign_date", "asignee0",
                            "asign_date0",
                            "asignee1",
                            "asign_date1", "asignee2", "asign_date2", "asignee3", "asign_date3"]
            df = df.reindex(columns=columns_list)
            base_cnt = 3
            self.m_text_info.AppendText(" ")
            for id in self.bug_list:
                self.m_text_info.AppendText("* ")
                df_index = df[df.id == id].index.values[0]
                if df.iloc[df_index, 1] == "NEW":
                    continue
                df_hist = bz.bug_history(str(id))
                try:
                    row_cnt = df_hist.iloc[:, 0].size
                except IndexError:
                    continue
                else:
                    i_cnt = 0
                    if row_cnt > 0:
                        print(df_hist)
                        for x in range(row_cnt - 1, -1, -1):
                            df.iloc[df_index, base_cnt + 2 * i_cnt] = df_hist.iloc[x, 1]
                            df.iloc[df_index, base_cnt + 2 * i_cnt + 1] = df_hist.iloc[x, 0]
                            i_cnt += 1
                            if i_cnt == 5:
                                break
            self.m_text_info.AppendText("\n")
            self.gen_file = "QueryResult_%s.xls" % gettime(0)
            write = ExcelWriter(self.gen_file)
            df.to_excel(write, columns=columns_list)
            write.save()
            self.m_result_path.Clear()
            self.m_result_path.AppendText(self.gen_file)
            self.m_btn_open.Enable()
            self.m_btn_gen.Disable()
            self.m_text_info.AppendText("- Query Result Save Success!!\n")


def main_opr():
    bz = Bugzilla("icecream.ma", "123@abAB")
    bz.login()
    # bug_list = [963506]
    bug_list = range(963500, 963520)
    df = bz.get_bug(bug_list)
    columns_list = ["id", "status", "needinfo_date", "asignee", "asign_date", "asignee0", "asign_date0", "asignee1",
                    "asign_date1", "asignee2", "asign_date2", "asignee3", "asign_date3"]
    df = df.reindex(columns=columns_list)
    # print(df)
    base_cnt = 3
    for id in bug_list:

        df_index = df[df.id == id].index.values[0]

        if df.iloc[df_index, 1] == "NEW":
            continue

        df_hist = bz.bug_history(str(id))

        try:
            row_cnt = df_hist.iloc[:, 0].size
        except IndexError:
            continue
        else:
            i_cnt = 0
            if row_cnt > 0:
                print(df_hist)
                for x in range(row_cnt - 1, -1, -1):
                    # print(id)
                    print(x)
                    # print(df_index)
                    # print(df.iloc[df_index,base_cnt+2*i_cnt+1])
                    # print(df_hist.iloc[x, 0])
                    df.iloc[df_index, base_cnt + 2 * i_cnt] = df_hist.iloc[x, 1]
                    # print(df.iloc[df_index,base_cnt+2*i_cnt+1])
                    # print(df_hist.iloc[x, 1])
                    df.iloc[df_index, base_cnt + 2 * i_cnt + 1] = df_hist.iloc[x, 0]
                    i_cnt += 1
                    if i_cnt == 5:
                        break

    # df_hist = bz.bug_history(963595)
    # print(df_hist)
    # print(df_hist.iloc[:, 0].size)

    write = ExcelWriter("QueryResult_%s.xlsx" % gettime(0))
    df.to_excel(write, columns=columns_list)
    write.save()


if __name__ == '__main__':
    # main_opr()
    app = wx.App()  # 实例化一个主循环<br>
    frame = QueryFrame(None)  # 实例化一个窗口<br>
    frame.Show()  # 调用窗口展示功能<br>
    app.MainLoop()  # 启动主循环
