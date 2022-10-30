class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, data):
        self.queue.append(data)
    
    def denqueue(self):
        if len(self.queue) < 1:
            return -1
        
        data = self.queue[0]
        del self.queue[0]
        return data
    
    def peek(self):
        return self.queue[0]
    
    def is_empty(self):
        return self.queue == []
    
    def queue_size(self):
        return len(self.queue)

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