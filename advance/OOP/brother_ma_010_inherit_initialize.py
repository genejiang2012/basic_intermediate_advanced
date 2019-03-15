
class A:
    def __init__(self, a, d=10):
        self.a = a
        self.__d = d


class B(A):
    def __init__(self, b, c):
        A.__init__(self, b+c, b-c)
        self.b = b
        self.c = c

    def printv(self):
        print(self.b)
        print(self.a)


f = B(200, 300)
print(f.__dict__)
print(f.__class__.__bases__)
f.printv()