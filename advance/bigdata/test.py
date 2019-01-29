from datetime import date
from datetime import timedelta
import random
import os

# 随机生成身份证号
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DC_PATH = BASE_DIR + "/advance/bigdata/districtcode.txt"


def getdistrictcode():
    with open(DC_PATH) as file:
        data = file.read()
        districtlist = data.split('\n')
    for node in districtlist:
        # print node
        if node[10:11] != ' ':
            state = node[10:].strip()
        if node[10:11] == ' ' and node[12:13] != ' ':
            city = node[12:].strip()
        if node[10:11] == ' ' and node[12:13] == ' ':
            district = node[14:].strip()
            code = node[0:6]
            codelist.append({"state": state, "city": city, "district": district,
                             "code": code})


def gennerator():
    global codelist
    codelist = []
    if not codelist:
        getdistrictcode()
    print(len(codelist))
    id = codelist[random.randint(0, len(codelist))]['code']  # 地区项
    id = id + str(random.randint(1930, 2013))  # 年份项
    da = date.today() + timedelta(days=random.randint(1, 366))  # 月份和日期项
    id = id + da.strftime('%m%d')
    id = id + str(random.randint(100, 300))  # ，顺序号简单处理

    i = 0
    count = 0
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
    checkcode = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7',
                 '6': '6', '7': '5', '8': '5', '9': '3', '10': '2'}  # 校验码映射
    for i in range(0, len(id)):
        count = count + int(id[i]) * weight[i]
        id = id + checkcode[str(count % 11)]  # 算出校验码
        return id


def generate_id(num):
    all_id = []
    for i in range(num):
        temp_id = gennerator()
        all_id.append(temp_id)

    return all_id


if __name__ == "__main__":
    print(generate_id(1000000))