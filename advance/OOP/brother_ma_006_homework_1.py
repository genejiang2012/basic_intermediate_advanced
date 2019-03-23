#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: brother_ma_006_homework_1.py
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/genejiang2012
Description: generate the number randomly
"""

import random


class RandomGen:
    """Docstring for RandomGen:. """

    def __init__(self, start=1, stop=100, count=10):
        self.start = start
        self.stop = stop
        self.count = count

    def generate(self, start=1, stop=1000, count=1000):
        return [random.randint(self.start, self.stop) for _ in range(self.count)]


class RandomToolGene:
    @classmethod
    def generate(cls, start=1, stop=100, count=10):
        return [random.randint(start, stop) for _ in range(count)]


class RandomToolGenerator:
    def __init__(self, start=1, stop=10, count=10):
        self.start = start
        self.stop = stop
        self.count = count
        self.gen = self._generate()

    def _generate(self):
        while True:
            yield [random.randint(self.start, self.stop) for _ in range(self.count)]

    def generate(self, count):
        self.count = count
        return next(self.gen)


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "({},{})".format(self.x, self.y)


class Car(object):
    def __init__(self, mark, color, price, speed):
        self.mark = mark
        self.color = color
        self.price = price
        self.speed = speed


class CarInfo(object):
    def __init__(self):
        self.lst = []

    def add_car(self, car: Car):
        self.lst.append(car)

    def get_all(self):
        return self.lst


class Temperature:
    def __init__(self, t, unit='c'):
        self._c = None
        self._f = None
        self._k = None

        if unit == 'k':
            pass
        elif unit == 'f':
            pass
        else:
            self._c = t

    @property
    def c(self):
        return self._c

    @property
    def k(self):
        pass

    @property
    def f(self):
        pass

    @classmethod
    def c2f(cls, c):
        return 9*c/5+32

    @classmethod
    def f2c(cls, f):
        return 5*(f-32)/9

    @classmethod
    def c2k(cls, c):
        return c + 273.15

    @classmethod
    def k2c(cls, k):
        return k - 273.15

    @classmethod
    def f2k(cls, f):
        return cls.c2k(cls.f2c(f))

    @classmethod
    def k2f(cls, k):
        return cls.c2f(cls.k2c(k))




if __name__ == '__main__':
    print("******************RandomGene**************************************")
    little_data = RandomGen(1, 100, 10)
    print(RandomGen.__dict__)
    print(little_data.__dict__)
    print(little_data.generate(1, 100, 10))
    print(little_data.__dict__)

    print("***************RandomToolGene**************************************")
    print(RandomToolGene.generate(1, 100, 10))
    print(RandomToolGene.__dict__)

    print("*********************RandomToolGenerator**************************")
    rg = RandomToolGenerator()
    print(RandomToolGenerator.__dict__)
    print(rg.__dict__)
    lst = rg.generate(10)
    print(lst)

    print("*************************Point*************************************")
    lst1 = [Point(x, y) for x, y in zip(rg.generate(10), rg.generate(10))]
    print(lst1)

    print("*************************Car***************************************")
    car = Car('audi', 'red', 100, 100)
    ci = CarInfo()
    ci.add_car(car)
    print(ci.get_all())
