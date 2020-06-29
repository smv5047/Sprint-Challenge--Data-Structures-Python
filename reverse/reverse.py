class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # if none return

        if self.head is None:
            return

        elif self.head.next_node is None:
            return
        else:
            current_node = self.head
            while current_node is not None:
                self.add_to_head(current_node.value)
                current_node = current_node.next_node
            return


test_ll = LinkedList()
test_ll.add_to_head(1)
test_ll.add_to_head(2)
test_ll.add_to_head(3)
test_ll.add_to_head(4)
test_ll.add_to_head(5)
test_ll.reverse_list('', 'none')
print(test_ll.head.value)
