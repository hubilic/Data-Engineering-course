class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.first = None


    def append(self, value):
        new_node = Node(value)

        if self.first is None:
            self.first = new_node
            return self

        current = self.first

        while current.next is not None:
            current = current.next

        current.next = new_node
        return self


    def prepend(self, value):
        new_node = Node(value)

        new_node.next = self.first
        self.first = new_node

    def read(self, index):
        if index < 0:
            raise IndexError

        current = self.first
        current_index = 0

        while current is not None:
            if current_index == index:
                return current.value

            current = current.next
            current_index += 1

        raise IndexError


    def remove(self, index):

        if index < 0:
            raise IndexError

        if self.first is None:
            raise IndexError


        current = self.first
        previous = None

        if index == 0:
            self.first = self.first.next
            return

        current = self.first
        previous = None



        current_index = 0
        while current is not None:
            if current_index == index:
                previous.next = current.next
                return
            previous = current
            current = current.next
            current_index += 1
        raise IndexError



    def __repr__(self):
        current = self.first

        result = ""

        while current is not None:
            result += str(current.value)

            if current.next is not None:
                result += "-"
            current = current.next

        return result


linked = LinkedList()
linked.append(10).append(20).append(30)
linked.remove(1)
linked.prepend(0)
print(linked.read(1))

current = linked.first
print(linked)
