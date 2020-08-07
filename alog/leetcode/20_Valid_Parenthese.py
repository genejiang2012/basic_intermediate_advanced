import pdb

class Stack:
    def __init__(self):
        self.items = []

    def push(self, data: str):
        return self.items.append(data)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def traversal(self):
        for item in self.items:
            print(item)


class Solution:
    def isValid(self, s: str) -> bool:
        pdb.set_trace()
        temp_stack = Stack()
        balanced = True
        index = 0

        while index < len(s) and balanced:
            symbol = s[index]

            if symbol in "([{":
                temp_stack.push(symbol)
            else:
                if temp_stack.is_empty():
                    return False
                else:
                    top = temp_stack.pop()
                    print(top)

            index = index + 1

        temp_stack.traversal()

        if temp_stack.is_empty() and balanced:
            return True
        else:
            return False


if __name__ == '__main__':
    my_sloution = Solution()
    test_string = "()"

    print(my_sloution.isValid(test_string))
