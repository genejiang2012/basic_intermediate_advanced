#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class B:
    x=1

    @classmethod
    def test(cls):
        print(cls, cls.x)

B.test()


class A(object):
    bar = 1
    
    def func1(self):
        print('foo')

    @classmethod
    def func2(cls):
        print('func2')
        print(cls.bar)
        cls().func1()

A.func2()

class Demo(object):
    @classmethod
    def classmeth(*args):
        return args

    @staticmethod
    def statmeth(*args):
        return args


print(Demo.classmeth())

print(Demo.statmeth('Spam'))

print(Demo.statmeth())

print(Demo.statmeth('Spam'))


