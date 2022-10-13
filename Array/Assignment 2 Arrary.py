'''
"A palindrome is a string that 
reads the same forward and backward"

For example: radar or madam

Our task is to design an optimal algorithm 
for checking whether a given string is palindrome or not! 
'''

from ast import Try


def my_answer_palindrome(word):
    if word == word[::-1]: # [::-1] return the reverse word
        return(True)

    return(False)

# Solution

def is_palindrome(word):
    orginal_data = word
    reverse_data = reverse(word)

    if orginal_data == reverse_data:
        return True
    
    return False

def reverse(data):
    
    # This convert the string to list
    data = list(data)

    start_index = 0
    
    # Get the last item in the list
    end_index = len(data) - 1

    while end_index > start_index:
        data[start_index], data[end_index] = data[end_index], data[start_index]
        start_index = start_index + 1
        end_index = end_index - 1
    
    # Convert the list back to string
    return ''.join(data)

if __name__ == '__main__':
    print(is_palindrome('madam'))
    print(is_palindrome('man'))