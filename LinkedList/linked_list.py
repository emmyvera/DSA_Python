
class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self) -> str:
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        self.num_of_node = 0

    def insert_start(self, data):
        self.num_of_node += 1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_end(self, data):
        self.num_of_node += 1
        new_node = Node(data)

        actual_node = self.head

        if self.head is None:
            self.head = new_node
        else:
            while actual_node.next_node is not None:
                actual_node = actual_node.next_node

            actual_node.next_node = new_node

    
    def traverse(self):
        actual_node = self.head

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next_node


    def size_of_list(self):
        return self.num_of_node

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_start(10)
    linked_list.insert_start('Emmy')
    linked_list.insert_start('Vera')
    linked_list.insert_start(20)
    linked_list.traverse()