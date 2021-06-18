# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/10/22 15:07
# @Author  : Gene Jiang
# @File    : dev2_db.py
# @Description:

import pymysql


class DBConnection:
    def __init__(self, host, port=3306, user='root', password='abc123', db="Default"):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db

    def create_connection(self):
        try:
            connection = pymysql.connect(self.host,
                                         self.port,
                                         self.user,
                                         self.password,
                                         self.db,
                                         charset='utf8',
                                         cursorclass=pymysql.cursors.DictCursor)
        except:
            print("DB didn't connect!")
        finally:
            return connection

    def execute_query(self, sql):
        connection = self.create_connection()

        queried = -1
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql)

            connection.commit()
            queried = 1
        finally:
            if queried:
                return queried
            connection.close()


if __name__ == "__main__":
    host = 'dp-dev-v2.ccd86.cn'
    port = 3306
    root = 'root'
    password = 'rooT123#@#'
    default_db = 'audience'

    dev2_connection = DBConnection(host, port, root, password, db= default_db)
    dev2_connection.create_connection()

    query_sql = "SELECT * FROM segment"
    dev2_connection.execute_query(qu)