#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: mysql_operation.py
Author: Gene Jiang
Email: zhengrong.jiang@chiefclouds.com
Github: https://github.com/yourname
Description: 
"""

import time
import configparser as cparser
from pymysql import connect, cursors


db_config_file_path='db_config.ini'

segmentList=[
    ['TOTAL', 1418776352],
    ['SG001', 418776352]
]


class ParseConfigIni():
    """
    Parse the config INI file_concept
    """
    def __init__(self, config_file_path):
        """
        initial the ParseConfigIni
        :param config_file_path:
        """
        self.config_file_path = config_file_path
        self.cf = cparser.ConfigParser()
        self.cf.read(self.config_file_path)

    def get_data(self, section_name, key_name):
        """

        :param section_name:
        :param key_name:
        :return:
        """
        key_value = self.cf.get(section_name, key_name)
        return key_value


class MySQLDb(object):
    """docstring for MySQL_DB"""
    def __init__(self):
        parse_mysql_config = ParseConfigIni(db_config_file_path)

        host = parse_mysql_config.get_data("mysqlconf", "host")
        port = parse_mysql_config.get_data("mysqlconf", "port")
        db = parse_mysql_config.get_data("mysqlconf", "db_name")
        user = parse_mysql_config.get_data("mysqlconf", "user")
        password = '0rkY76R{VncjN#ba_8nptyuf%'


        try:
            self.conn = connect(host=host, 
                                user=user, 
                                password=password, 
                                db=db)
        except Exception as e:
            print("MySQL error %d: %s" % (e.args[0], e.args[1]))

    def clear(self, table_name):
        """
        clear data from the specified table
        :param table_name: the table name from the database
        :return:
        """
        real_sql = "DELETE FROM " + table_name + ";"

        with self.conn.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.conn.commit()

    def insert(self, table_name, table_data):
        """

        :param table_name:
        :param table_data:
        :return:
        """
        for key in table_data:
            table_data[key] = "'" + str(table_data[key]) + "'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO " + table_name + \
                "(" + key + ") VALUES (" + value + ");"

        print("The SQL sentence is {}: ".format(real_sql))

        with self.conn.cursor() as cursor:
            cursor.execute(real_sql)

        self.conn.commit()

    def close(self):
        self.conn.close()

    def query(self, query_data, table_name, condition):
        """

        :param table_name:
        :return:
        """
        real_sql = "SELECT " + query_data + \
                   " FROM " + table_name + \
                   " WHERE " + condition

        with self.conn.cursor() as cursor:
            cursor.execute(real_sql)
            result_items = cursor.fetchall()

        return result_items


def get_tag():
    parse_config_ini = ParseConfigIni(db_config_file_path)
    db = MySQLDb()
    tag = parse_config_ini.get_data('Tag', 'tagname')
    tag_list = tag.split(',')
    tag_new_list = []
    for i in range(len(tag_list)):
        table_name = "audience.first_party_tag"
        item = tag_list[i].strip()
        condition = 'id=' + "'" + item + "'"
        results = db.query("id, coverage", table_name, condition)
        # sub_list = []
        # sub_list = [results[j] for j in range(len(results))]

        for j in range(len(results)):
            sub_list = results[j]

        tag_new_list.append(list(sub_list))

    tag_list = []
    for k in range(len(tag_new_list)):
        lst_key = ['tag_id', 'coverage']
        lst_temp = tag_new_list[k]
        dict_value = dict(zip(lst_key, lst_temp))

        tag_list.append(dict_value)

    return tag_list


def get_tag_value():
    tag_list = get_tag()

    tag_value_list=[]
    for i in range(len(tag_list)):
        tag_name = tag_list[i]['tag_id']

        db = MySQLDb()
        table_name = "audience.first_party_tag_value"
        condition = 'tag_id=' + "'" + tag_name + "'"

        results = db.query("tag_id, id, coverage", table_name, condition)


        tag_name_list = []
        tag_name1 = tag_name_list.append(tag_name)

        for j in range(len(results)):
            sub_list = results[j]
            tag_value_list.append(list(sub_list))

    return tag_value_list


def get_tag_value_list():
    tag_list = get_tag()
    tag_value_list = get_tag_value()

    temp_list_1 = []
    temp_list_2 = []

    for i in range(len(tag_list)):
        temp_list_1 = []
        for j in range(len(tag_value_list)):
            tag_id = tag_list[i]['tag_id']
            temp_list_2 = []
            tag_value = tag_value_list[j][0]
            if tag_id == tag_value:
                temp_list_2.append(tag_value_list[j][1])
                temp_list_2.append(tag_value_list[j][2])
                temp_list_1.append(temp_list_2)

        tag_list[i]['tag_value_list'] = temp_list_1

    return tag_list


def createSQL():
    global segmentList
    tagList = get_tag_value_list()
    sqlValuesList = []
    for i in range(len(segmentList)):
        for j in range(len(tagList)):
            segId = segmentList[i][0]
            segCoverage = segmentList[i][1]
            tagId = tagList[j]['tag_id']
            tagCoverage = tagList[j]['coverage']
            for k in range(len(tagList[j]['tag_value_list'])):
                tagOptionId = tagList[j]['tag_value_list'][k][0]
                tagOptionCoverage = tagList[j]['tag_value_list'][k][1]
                if tagList[j]['coverage'] == None or \
                        tagList[j]['tag_value_list'][k][1] == None:
                    tagOptionCoveragePercent =0
                    featureCoverage = None
                else:
                    tagOptionCoveragePercent = float(tagList[j]['tag_value_list'][k][1])/float(tagList[j]['coverage'])
                    featureCoverage = int(int(tagList[j]['coverage'])*tagOptionCoveragePercent)
                current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                sqlValuesList.append("('"+str(tagId)+"','"+str(segId)+"','" + \
                                     str(tagOptionId)+"','"+str(segCoverage)+ \
                                     "','"+str(featureCoverage)+"','"+\
                                     str(tagCoverage)+ \
                                     "','"+ current_time + "','" + \
                                     current_time + "','dmp_user@172.16.6.9')")
    return sqlValuesList


if __name__ == "__main__":
    lst_sql = createSQL()
    with open('test.txt', 'w') as f:
        for i in range(len(lst_sql)):
            f.write(lst_sql[i] + ',\n')










