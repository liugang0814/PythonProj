# -*- coding: utf-8 -*-
# @Time    : 2020/1/28 10:29
# @Author  : liugang
# @Email   : liugang0814@126.com
# @File    : bugzilla.py
# @Software: PyCharm

import datetime
import time
# import configparser
import json
import requests
import logging
import pandas as pd
from pandas import DataFrame

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def time_conv(str_time):
    date_time = datetime.datetime.strptime(str_time, "%Y-%m-%dT%H:%M:%SZ")
    # print(date_time,type(date_time))
    modfiy_datetime = date_time + datetime.timedelta(hours=8)
    # print(modfiy_datetime)
    # t_str = date_time.strftime("%Y-%m-%d %H:%M:%S")
    t_str = modfiy_datetime.strftime("%Y-%m-%d %H:%M:%S")
    return t_str


def web_strptime(str_time, tz=8):
    ptime = datetime.datetime.strptime(str_time, "%Y-%m-%dT%H:%M:%SZ") + datetime.timedelta(hours=tz)

    return ptime


def diff_days(later_time, early_time):
    days = later_time - early_time
    return days.days


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


def get_name_df():
    ret_df = pd.read_csv("config/name_list.csv")
    return ret_df


def check_site(name_df, email):
    ret_df = name_df.query(f"Email=='{email.lower()}'")
    # print(ret_df)
    if ret_df.shape[0] == 0:
        return False
    else:
        return ret_df.iloc[0, 1]


class Bugzilla:
    def __init__(self, user='', pwd=''):
        self.user = user
        self.pwd = pwd
        self.login_url = "https://bugzilla.unisoc.com/bugzilla/rest/login?login=%s&password=%s" % (user, pwd)
        self.url_base = "https://bugzilla.unisoc.com/bugzilla"
        self.session = requests.session()
        self.id = int()
        self.token = ""
        self.token_str = ""
        self.token_dict = dict()

    def __del__(self):
        self.session.close()

    def set_user_pwd(self, user, pwd):
        self.user = user
        self.pwd = pwd
        self.login_url = "https://bugzilla.unisoc.com/bugzilla/rest/login?login=%s&password=%s" % (user, pwd)

    def login(self):
        result = self.session.get(self.login_url)
        # print(self.login_url)
        if result.status_code != 200:
            print("Connect Fail!")
            return False

        ret_login = result.json()
        # print(ret)
        self.id = ret_login["id"]
        self.token = ret_login["token"]
        self.token_str = "&token=" + self.token
        self.token_dict["token"] = self.token
        # print("Login Success!")

        return True

    def valid_login(self):
        url = self.url_base + "/rest/valid_login?login=%s&token=%s" % (self.user, self.token)
        print(url)
        result = self.session.get(url)
        # print(result.json())
        return result.ok

    def logout(self):
        url = self.url_base + "/rest/logout?token=%s" % self.token
        result = self.session.get(url)
        # print(result.json())
        return result.ok

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
        df = DataFrame(ret_list)

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

                # if x["field_name"] == 'cf_assigneddate':
                #
                #     change_when = d["when"]
                #     # change_assignee = x["added"]
                #     t_str = time_conv(change_when)
                #     change_dict = dict()
                #     try:
                #         change_dict = {
                #             "assign_date": t_str,
                #             "assignee": ret_list[-1]["assignee"]
                #         }
                #     except IndexError:
                #         change_dict = {
                #             "assign_date": t_str,
                #             "assignee": d["who"]
                #         }
                #     ret_list.append(change_dict)
                #     break

                if (x["added"] == 'Assigned' and x["removed"] != 'NEW') \
                        or (x["field_name"] == 'cf_assigneddate'):
                    change_when = d["when"]
                    # change_assignee = x["added"]
                    t_str = time_conv(change_when)
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

    def search_bug(self, status: list, product: list):
        url = self.url_base + "/rest/bug"
        par_dict = dict()
        par_dict["status"] = status
        par_dict["product"] = product
        par_dict["token"] = self.token
        par_dict["include_fields"] = "id,product,component,assigned_to,status,severity," \
                                     "summary,creator,creation_time,last_change_time"

        result = self.session.get(url, params=par_dict)
        if result.ok is False:
            logger.error("Query Fail!")
            return False

        logger.debug(f"Search elapsed:{result.elapsed}")
        rslt_dict = result.json()
        bug_dict = dict()
        bug_dict["team"] = list()
        bug_dict["id"] = list()
        bug_dict["product"] = list()
        bug_dict["component"] = list()
        bug_dict["assignee"] = list()
        bug_dict["status"] = list()
        bug_dict["severity"] = list()
        bug_dict["summary"] = list()
        bug_dict["reporter"] = list()
        bug_dict["creation_time"] = list()
        bug_dict["elapsed_days"] = list()
        name_df = get_name_df()
        for bug in rslt_dict["bugs"]:
            assigned_email = bug["assigned_to"]
            team_str = check_site(name_df, assigned_email)
            if team_str is False:
                continue

            bug_dict["team"].append(team_str)
            bug_dict["id"].append(
                f'=HYPERLINK("https://bugzilla.unisoc.com/bugzilla/show_bug.cgi?id={bug["id"]}", {bug["id"]})')
            bug_dict["product"].append(bug["product"])
            bug_dict["component"].append(bug["component"])
            bug_dict["assignee"].append(assigned_email)
            bug_dict["status"].append(bug["status"])
            bug_dict["severity"].append(bug["severity"])
            bug_dict["summary"].append(bug["summary"])
            bug_dict["reporter"].append(bug["creator"])
            bug_dict["creation_time"].append(time_conv(bug["creation_time"]))
            bug_dict["elapsed_days"].append(diff_days(datetime.datetime.now(), web_strptime(bug["last_change_time"])))

        print(f"Total found {len(rslt_dict['bugs'])}")
        df = DataFrame(bug_dict)
        print(f"Match name list:{df.shape[0]}")

        excel_name = f"result/result_{gettime(0)}.xlsx"
        sheet_name = gettime(1)
        df.to_excel(excel_name, sheet_name)
        return excel_name

    def get_product_names(self, product_sort=None):
        # cfg = configparser.ConfigParser()
        # cfg.read("products.ini")
        with open("config/product.json", "r") as cfg_fp:
            cfg_dict = json.load(cfg_fp)

        cur_date = gettime(1)
        # if cur_date == cfg.get("config", "update_date"):
        #     names_str = cfg.get("config", "product_list")
        #     names_list = names_str.split(",")
        if cur_date == cfg_dict["update_date"]:
            names_str = cfg_dict["product_list"]
            names_list = names_str.split(",")
        else:
            logger.debug("Updating products.ini!!")
            url = self.url_base + "/rest/product"
            par_dict = dict()
            par_dict["token"] = self.token
            par_dict["type"] = "selectable"
            result = self.session.get(url, params=par_dict)
            if not result.ok:
                return False
            print(result.elapsed)
            result_dict = result.json()
            names_list = list()
            for product in result_dict["products"]:
                # print(product["name"])
                names_list.append(product["name"])
            names_str = ",".join(names_list)
            cfg_dict["product_list"] = names_str
            cfg_dict["update_date"] = cur_date
            with open("config/product.json", "w") as fp:
                json.dump(cfg_dict, fp, indent=4)

        if product_sort is None:
            return names_list
        else:
            sorted_list = list()
            for product in names_list:
                if product.count(product_sort) != 0:
                    sorted_list.append(product)
            return sorted_list


if __name__ == '__main__':
    bz = Bugzilla("*", "*")
    ret = bz.login()
    if ret is True:
        print("Login success!")
    # status_list = ['NEW', 'Assigned', 'Root-Caused', 'Code-Committed', 'ReOpen', 'Need_Info', 'CustomerVerified']
    status_list = ['NEW', 'Assigned', 'Root-Caused', 'Code-Committed', 'ReOpen', 'Need_Info']
    # product_list = bz.get_product_names("SPCSS")
    # print(product_list)
    product_list = ["SC9832E_ANDROID10_TRUNK", "SC7731E_ANDROID10_TRUNK", "9863A_ANDROID10_TRUNK"]
    bz.search_bug(status_list, product_list)
    # print(bz.get_name_df())
    # print(diff_days(datetime.datetime.now(), web_strptime("2020-2-10T13:38:24Z")))
    bz.logout()
