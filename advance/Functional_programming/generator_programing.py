def my_generator():
    yield 1
    yield 2
    yield 'a'


if __name__ == '__main__':
    next(my_generator())
