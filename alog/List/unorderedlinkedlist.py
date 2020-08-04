class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return str(self.data)


class UnorderedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.head == None

    def add(self, item):
        # add the node at the beginning
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def append(self, item):
        new_node = Node(item)
        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node
        new_node.next = None

    def index(self, index):
        current = self.head
        temp_index = 0

        while current is not None:
            current = current.next
            temp_index += 1

            if temp_index == index:
                return current

    def insert(self, index, item):
        if index < 0 or index > self.size:
            raise Exception("The index beyonds the range of the list")

        new_node = Node(item)
        current = self.head

        print("node is {}, index is {}".format(str(new_node.data), str(index)))

        if index == 0:
            new_node.next = self.head
            self.head = new_node
        elif index == self.size:
            while current.next is not None:
                current = current.next
            current.next = new_node
        else:
            pre_node = self.index(index)
            new_node.next = pre_node.next
            pre_node.next = new_node

        self.size += 1

    def pop(self):
        pass

    def tranversal(self):
        current = self.head

        if current is None:
            raise Exception("This is empyt list!")

        while current is not None:
            print(current.data)
            current = current.next

    def length(self):
        current = self.head
        self.size = 0

        while current is not None:
            self.size += 1
            current = current.next

        return self.size

    def search(self, item):
        current = self.head
        _found = False

        while current is not None and not _found:
            if current.data == item:
                return True
            else:
                current = current.next

        return _found

    def remove(self, item):
        current = self.head
        previous = None
        _found = False

        while not _found:
            if current.data == item:
                _found = True
            else:
                previous = current
                current = current.next

        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next


my_unorderedlist = UnorderedList()

my_unorderedlist.add(40)


my_unorderedlist.add(50)
my_unorderedlist.add(60)
my_unorderedlist.add(70)
my_unorderedlist.add(30)
my_unorderedlist.append(80)
my_unorderedlist.append(90)
print(my_unorderedlist.length())
my_unorderedlist.insert(0, 1000)
print(my_unorderedlist.length())
my_unorderedlist.insert(8, 2000)
print(my_unorderedlist.length())
my_unorderedlist.insert(4, 4000)

# print(my_unorderedlist.index(40))
# my_unorderedlist.remove(50)
# my_unorderedlist.remove(40)
my_unorderedlist.tranversal()

my_unorderedlist.search(40)
my_unorderedlist.search(100)
