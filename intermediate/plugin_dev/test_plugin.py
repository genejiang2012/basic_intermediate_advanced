if __name__ == '__main__':
    my_class = __import__('plug')
    my_class.getattr(my_class, 'A')
    my_class().show_me()