#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: array_concept.py
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/genejiang2012
Description: 
"""

from array import array
from random import random

floats = array('d', (random() for i in range(10**7)))
print(floats[0])
