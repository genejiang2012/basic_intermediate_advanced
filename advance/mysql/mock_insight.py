#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: mock_insight.py
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/genejiang2012
Description: 
"""

import pymysql.cursors
import pymysql
import pandas as pd

#连接配置信息
config = {
          'host': '52.81.25.5',
          'port': 3306,#MySQL默认端口
          'user': 'root',#mysql默认用户名
          'password': "0rkY76R{VncjN#ba_8nptyuf%",
          'db': 'audience'
          # 'charset': 'utf8mb4',
          # 'cursorclass': pymysql.cursors.DictCursor,
}

query_condition = "SELECT id, coverage \
                  FROM audience.first_party_tag_value \
                  WHERE tag_id ='FT583'"
# 创建连接
con = pymysql.connect(**config)
# 执行sql语句
try:
    with con.cursor() as cursor:
        # sql = "select * from audience.first_party_tag_value where status='1'"
        sql = query_condition
        cursor.execute(sql)
        result = cursor.fetchall()

finally:
    con.close()

print(type(result))
print(result)

new_list = []
for i in range(len(result)):
    new_list.append(list(result[i]))


print(new_list)

