'''
The problem is that we want to reverse a T[] array in O(N) 
linear time complexity and we want the algorithm to be 
in-place as well - so no additional memory can be used!

For example: input is [1,2,3,4,5] then the output is [5,4,3,2,1]

'''
# My Solution
T = [1,2,3,4,5]
ans = []

for i in T[::-1]:
    ans.append(i)

print(ans)

# The another solution (Best)
def reverse(num):
    
    
    start_index = 0
    
    # Get the last item in the list
    end_index = len(num) - 1

    while end_index > start_index:
        num[start_index], num[end_index] = num[end_index], num[start_index]
        start_index = start_index + 1
        end_index = end_index - 1

if __name__ == '__main__':
    n = [1, 2, 3, 4, 5, 6]
    reverse(n)
    print(n)