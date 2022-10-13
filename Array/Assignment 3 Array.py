'''
Our task is to design an efficient algorithm to 
reverse a given integer. For example if the input 
of the algorithm is 1234 then the output should be 4321.
'''

def reverse(data): 
    # This convert the int to list
    data = list(str(data))

    start_index = 0
    
    # Get the last item in the list
    end_index = len(data) - 1

    while end_index > start_index:
        data[start_index], data[end_index] = data[end_index], data[start_index]
        start_index = start_index + 1
        end_index = end_index - 1
    
    # Convert the list back to int
    return int(''.join(data))

# The best solution
def reverse_int(n):
    remainder = 0
    reversed = 0

    while n > 0:
        remainder = n % 10
        n = n // 10
        reversed = reversed * 10 + remainder
    
    return reversed


if __name__ == '__main__':
    print(reverse_int(4321))
    print(reverse_int(6421))