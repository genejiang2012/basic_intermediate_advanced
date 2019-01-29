#!/usr/bin/env python3
# -*- coding:utf-8 -*-

dct_pwd_name = {
    'name1': {'password': '123', 'count': 0},
    'name2': {'password': '123', 'count': 0},
    'name3': {'password': '123', 'count': 0}
}

while True:
    name = input('username >>: ')

    if not name in dct_pwd_name:
        print('The user is not existed.')
    elif dct_pwd_name[name]['count'] > 2:
        print('Try too many times!')
        continue

    pwd = input('password >>:')

    if pwd == dct_pwd_name[name]['password']:
        print("Log in successfully!")
        break
    else:
        print('name or password error!')
        dct_pwd_name[name]['count'] += 1
