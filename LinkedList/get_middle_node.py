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

    def insert(self, data):
        self.num_of_node += 1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def traverse(self):
        actual_node = self.head

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next_node
        
    def reverse_list(self):
        prev_node = None
        next_node = None
        current_node = self.head

        while current_node is not None:
            next_node = current_node.next_node
            current_node.next_node = prev_node
            prev_node = current_node
            current_node = next_node

        self.head = prev_node
    
    def get_middle(self):
        
        current_node = self.head
        middle = self.head

        while current_node.next_node and current_node.next_node.next_node:            
            current_node = current_node.next_node.next_node
            middle = middle.next_node
        
        return middle

    
    def size_of_list(self):
        return self.num_of_node

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert(10)
    linked_list.insert('Emmy')
    linked_list.insert('Vera')
    linked_list.insert(20)
    linked_list.insert(21)
    
    print('*'*10)
    linked_list.traverse()
    

    print('*'*10)
    linked_list.reverse_list()
    linked_list.traverse()

    print('*'*10)
    print(linked_list.get_middle())