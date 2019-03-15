class Animal:
    def shout(self):
        print('Animal shouts')

    @classmethod
    def define_cls_method(cls):
        print("class_method_animal")

    @staticmethod
    def define_static_method():
        print('static_method_animal')


class Cat(Animal):
    x = 10
    def shout(self):
        print('miao')

    def shout(self):
        print(self.__class__.mro())
        print(super())
        print(super(Cat, self))
        super(Cat, self).shout()
        super().shout()
        self.__class__.__base__.shout(self)

    @classmethod
    def define_cls_method(cls):
        print(cls.x)
        print('class_method_cat')

    @staticmethod
    def define_static_method():
        print('static_method_cat')


a = Animal()
a.shout()
c = Cat()
c.shout()
c.define_cls_method()
c.define_static_method()
print(a.__dict__)
print(c.__dict__)
print(Animal.__dict__)
print(Cat.__dict__)
