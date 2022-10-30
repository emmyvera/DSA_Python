class Node:

    def __init__(self, data):
        self.data = data
        self.prev_node = None
        self.next_node = None

    def __repr__(self):
        return str(self.data)

# Modify for Queue Sha
class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.num_of_node = 0

    def insert(self, data):
        self.num_of_node += 1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev_node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node

    def remove(self):
        if self.head is None:
            return
        
        self.num_of_node -= 1
        current_node = self.head
        self.head = current_node.next_node
        current_node.prev_node = None

    def forward_traverse(self):

        current_node = self.head

        while current_node is not None:
            print(current_node)
            current_node = current_node.next_node

    def size_of_list(self):
        return self.num_of_node

class Queue:
    
    def __init__(self):
        self.queue = DoublyLinkedList()
    
    def enqueue(self, data):
        self.queue.insert(data)
    
    def denqueue(self):
        if self.queue.head is None:
            return -1

        data = self.queue.head
        self.queue.remove()
        return data
    
    def peek(self):
        data = self.queue.head
        return data
    
    def queue_size(self):
        return self.queue.size_of_list()

    def is_empty(self):
        return self.queue.size_of_list() == 0
        

if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(3)
    queue.enqueue(5)
    queue.enqueue(7)

    print('Queue Size: ', queue.queue_size())
    print('Dequeue: ', queue.denqueue())
    print('*'*10)
    print('Queue Size: ', queue.queue_size())
    print('*'*10)
    print('Peeked: ', queue.peek())
    print('Queue Size: ', queue.queue_size())
    print('Dequeue: ', queue.denqueue())
    print('Dequeue: ', queue.denqueue())
    print('Dequeue: ', queue.denqueue())
    print('Dequeue: ', queue.denqueue())
    print('Queue Size: ', queue.queue_size())
    print('Is the stack empty: ', queue.is_empty())