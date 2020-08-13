#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: client.py
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/genejiang2012
Description: 
"""
import sys

from design_pattern.greeting_mvc.controller import GenericController

if __name__ == '__main__':
    g_controller = GenericController()
    g_controller.handle(sys.argv[1])

