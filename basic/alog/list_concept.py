#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: list_concept.py
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/genejiang2012
Description: 
"""

symbols = '$¢£¥€¤'

codes = []

for symbol in symbols:
    codes.append(ord(symbol))

print(codes)

codes_le = [ord(symbol) for symbol in symbols]
print(codes_le)

