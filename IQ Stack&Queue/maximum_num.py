class Stack:

    def __init__(self):
        self.array = []
        self.max_stack = []
    
    def push(self, data):
        self.array.append(data)

        if len(self.max_stack) == 0:
            self.max_stack.append(data)
        elif data > self.max_stack[-1]:
            self.max_stack.append(data)
        else:
            self.max_stack.append(self.max_stack[-1])
        



    def pop(self):
        if len(self.array) < 1:
            return -1

        data = self.array[-1]
        del self.array[-1]
        return data
    
    def peek(self):
        return self.array[-1]
    
    def stack_size(self):
        return len(self.array)
    
    def is_empty(self):
        return self.array == []
    
    def get_max(self):
        if len(self.array) < 1:
            raise Exception('List is empty')

        return self.max_stack[-1]    

    
if __name__=='__main__':
    stack = Stack()
    stack.push(10)
    stack.push(40)
    stack.push(120)
    stack.push(100)

    print(stack.get_max())