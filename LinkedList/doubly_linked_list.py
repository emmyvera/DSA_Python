class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.prev_node = None
    
    def __repr__(self):
        return str(self.data)

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.num_of_node = 0
    
    def insert(self, data):

        new_node = Node(data)
        
        if self.head is None:            
            self.num_of_node += 1
            self.head = new_node
            self.tail = new_node
        else:
            self.num_of_node += 1
            new_node.prev_node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node
        
    def remove(self, data):
        # No data dey this list
        if self.head is None:
            return
        
        current_node = self.head
        
        # Track both previous and next node
        prev_node = None        

        while current_node is not None and current_node.data != data:
            prev_node = current_node
            #next_node = current_node.next_node
            current_node = current_node.next_node
        
        # These data no dey the list
        if current_node is None:
            return
        
        # Na the head we get remove
        if prev_node is None:
            self.num_of_node -= 1
            self.head = current_node.next_node
            current_node.prev_node = None
        else:
            self.num_of_node -= 1
            prev_node.next_node = current_node.next_node
            current_node.next_node.prev_node = prev_node
        


    def forward_traverse(self):
        current_node = self.head

        while current_node is not None:
            print(current_node)
            current_node = current_node.next_node
    
    def backward_traverse(self):
        current_node = self.tail

        while current_node is not None:
            print(current_node)
            current_node = current_node.prev_node
    
    def size_of_list(self):
        return self.num_of_node

if __name__ == '__main__':
    linked_list = DoublyLinkedList()
    linked_list.insert(10)
    linked_list.insert('Emmy')
    linked_list.insert('Vera')
    linked_list.insert(20)
    linked_list.insert(21)
    
    linked_list.forward_traverse()
    print('*'*10)
    linked_list.backward_traverse()
    
    linked_list.remove('Vera')

    print('*'*10)
    linked_list.forward_traverse()
    print('*'*10)
    linked_list.backward_traverse()

