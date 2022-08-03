import os
import jaydebeapi as jp
from dotenv import load_dotenv
from util.query_util import set_query_sort_by, get_query_month_list
import json


class CustomerV1:
    def __init__(self, conn):
        self.conn = conn

    def get_login_info(self, username, passwd):
        sql = " SELECT SUBS_ID, LOGIN_ID, CREATE_DATE, ..."
        result = None

        with self.conn.cursor() as curs:
            try:
                curs.execute(sql)
                result = curs.fetchall()
                return result[0]
            except Exception as msg:
                return result

    def get_stats_count(self, query_dict, one=False):
        sql = "SELECT COUNT(*) as Count FROM ( SELECT RA..."
        result = None

        with self.conn.cursor() as curs:
            try:
                curs.execute(sql)
                result = [dict((curs.description[i][0], str(value)) \
                               for i, value in enumerate(row)) for row in curs.fetchall()]
                return (result[0] if result else None) if one else result
            except Exception as msg:
                return result

    def get_stats_list(self, query_dict, one=False):
        ...

        sql = " SELECT RAISEDATE as raisedate, MSG_TYPE as msg_serv...
        with self.conn.cursor() as curs:
            try:
                curs.execute(sql)
                result = [dict((curs.description[i][0], str(value)) \
                               for i, value in enumerate(row)) for row in curs.fetchall()]
                return (result[0] if result else None) if one else result
            except Exception as msg:
                return result

    def get_msghist_count(self, query_dict, one=False):
        ...

        result = None
        with self.conn.cursor() as curs:
            try:
                curs.execute(sql)
                result = [dict((curs.description[i][0], str(value)) \
                               for i, value in enumerate(row)) for row in curs.fetchall()]
                return (result[0] if result else None) if one else result
            except Exception as msg:
                return result

    def get_msghist_list(self, query_dict, one=False):
        ...

        with self.conn.cursor() as curs:
            try:
                curs.execute(sql)
                result = [dict((curs.description[i][0], str(value)) \
                               for i, value in enumerate(row)) for row in curs.fetchall()]
                return (result[0] if result else None) if one else result
            except Exception as msg:
                return result