#from LinkedList.doubly_linked_list import DoublyLinkedList
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



class StackLinkedList:
    
    def __init__(self):
        self.stack = DoublyLinkedList()

    def push(self, data):
        self.stack.insert(data)

    def pop(self):
        if self.stack.size_of_list() < 1:
            return -1

        data = self.stack.tail.data
        self.stack.num_of_node -= 1
        current_node = self.stack.tail
        self.stack.tail = current_node.prev_node
        current_node.next_node = None

        return data

    def peek(self):
        return self.stack.tail.data

    def is_empty(self):
        return self.stack.size_of_list() == 0

    def stack_size(self):
        return self.stack.size_of_list()


if __name__ == '__main__':
    stack = StackLinkedList()
    stack.push(2)
    stack.push(4)
    stack.push(6)

    print('Stack Size: ', stack.stack_size())
    print('Poped: ', stack.pop())
    print('*'*10)
    print('Stack Size: ', stack.stack_size())
    print('*'*10)
    print('Peeked: ', stack.peek())
    print('Stack Size: ', stack.stack_size())
    print('Poped: ', stack.pop())
    print('Poped: ', stack.pop())
    print('Poped: ', stack.pop())
    print('Poped: ', stack.pop())
    print('Stack Size: ', stack.stack_size())
    print('Is the stack empty: ', stack.is_empty())