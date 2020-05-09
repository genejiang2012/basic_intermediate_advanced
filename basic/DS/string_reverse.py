class ReverseString(object):
    def __init__(self, my_string):
        self.local_string = my_string

    def reverse_by_string_property(self):
        return self.local_string[::-1]

    def reverse_by_list(self):
        local = list(self.local_string)
        return local.reverse()


obj_ReverseString = ReverseString('abcd')
print(obj_ReverseString.reverse_by_string_property())
print(obj_ReverseString.reverse_by_list())
