#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: threading.py
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/genejiang2012
Description: 
"""

import random
import threading
import datetime

results = []


def compute():
    """TODO: Docstring for compute.
    :returns: TODO

    """
    results.append(sum([random.randint(1, 100) for i in range(1000000)]))


if __name__ == '__main__':
    begin = datetime.datetime.now()

    workers = [threading.Thread(target=compute) for x in range(8)]

    for worker in workers:
        worker.start()
    for worker in workers:
        worker.join()

    print("Results: %s" % results)

    end = datetime.datetime.now()
    print('Time cost: %s' % (end - begin))
