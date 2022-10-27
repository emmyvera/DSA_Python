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

    def remove(self, data):

        # Well the list is empty
        if self.head is None:
            return

        current_node = self.head

        # We need to track the previous node 
        # So when we get the node we replace the Ref
        previous_node = None

        while current_node is not None and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next_node
        
        # He no dey the list
        if current_node is None:
            return

        # Omo na the head we won remove O(1) running time
        if previous_node is None:
            self.num_of_node -= 1
            self.head = current_node.next_node

        else:
            # Remove and replace the next node ref
            self.num_of_node -= 1
            previous_node.next_node = current_node.next_node
        

    def size_of_list(self):
        return self.num_of_node

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_start(10)
    linked_list.insert_start('Emmy')
    linked_list.insert_start('Vera')
    linked_list.insert_start(20)
    linked_list.insert_end(21)
    linked_list.traverse()
    print(linked_list.size_of_list())
    linked_list.remove('Emmy')
    print('*'*10)
    linked_list.traverse()
    print(linked_list.size_of_list())