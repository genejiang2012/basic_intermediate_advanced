#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: tuple_concept.py
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/genejiang2012
Description: 
"""

travel_ids = [('USA', '31195855'), ('CN', 'CN17280145'),
              ('EXP', 'XDA205856')]


for passport in sorted(travel_ids):
    print('%s-%s' % passport)

for country, _ in travel_ids:
    print(country)


