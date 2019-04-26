class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @age.deleter
    def age(self):
        # del self.__age
        print('del')


    def get_age(self):
        return (self.__age)

    def set_age(self, age):
        self.__age = age


tom = Person('Tom',20)
print(tom.get_age())
tom.set_age(30)
print(tom.get_age())
tom.age = 20
print(tom.age)
del tom.age