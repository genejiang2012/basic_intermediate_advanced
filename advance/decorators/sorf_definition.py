#!/usr/bin/python3

def sort(iterable, reverse=False):
    ret = []
    for x in iterable:
        for i, y in enumerate(ret):
            flag = x > y if reverse else x < y

            if flag:
                ret.insert(i, x)
                break
        else:
            ret.append(x)
    
    return ret

def add(x,y):
    return x + y

def c_add(x):
    def _c_add(y):
        return x + y
    return _c_add

if __name__ == "__main__":
    print(add(2, 3))
    print(c_add(5)(6))
    print(sort([1, 2, 5, 4, 2, 3, 5, 6]))