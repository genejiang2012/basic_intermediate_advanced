class Root(object):
    def __init__(self):
        print("this is Root")


class B(Root):
    def __init__(self):
        print("enter B")
        print(self)
        super(B, self).__init__()
        print("leave B")


class C(Root):
    def __init__(self):
        print("enter C")
        super(C, self).__init__()
        print("leave C")


class D(B, C):
    pass


if __name__ == '__main__':
    d = D()
    print(d.__class__.__mro__)