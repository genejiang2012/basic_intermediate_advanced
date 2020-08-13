#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: view.py
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/genejiang2012
Description: 
"""



class GreetingView(object):
    """Docstring for GreetingView. """

    def __init__(self):
        """TODO: to be defined1. """
        pass

    def generate_greeting(self, name, known, time_of_day):
        if name == 'Lion':
            print('Rorrrar!')
            return

        if known:
            print("Good {} welcome come back {}".format(time_of_day, name))
        else:
            print("Good {} {} , it is good to meet you!".format(time_of_day,
                                                                 name))
