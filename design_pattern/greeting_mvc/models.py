#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: models.py
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/genejiang2012
Description: models to store the data
"""
import datetime
import os


class NameModel:
    """name model to store the filename"""

    def __init__(self):
        self.filename = 'names.dat'

    def _get_write_append(self):
        if os.path.exists(self.filename):
            return 'a'

        return 'w'

    def get_name_list(self):
        if not os.path.exists(self.filename):
            return False

        with open(self.filename, 'r') as data_file:
            names = data_file.read().split('\n')

        return names

    def save_name(self, name):
        with open(self.filename, self._get_write_append()) as data_file:
            data_file.write('{}\n'.format(name))


class TimeModel:
    """TimeModel for dealing with the Time. """

    def __init__(self):
        pass

    def get_time_of_day(self):
        time = datetime.datetime.now()

        if time.hour < 12:
            return 'Morning'
        elif 12 <= time.hour < 18:
            return 'Afternoon'
        elif time.hour > 18:
            return 'Evening'
