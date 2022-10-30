class Stack:

    def __init__(self):
        self.stack = []
    
    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        if len(self.stack) < 1:
            return -1

        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return self.stack == []
    
    def stack_size(self):
        return len(self.stack)
    
if __name__=='__main__':
    stack = Stack()
    stack.push(8)
    stack.push(6)
    stack.push(4)
    stack.push(2)

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