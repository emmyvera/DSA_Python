"""
The problem is that we want to sort a T[] 
one-dimensional array of integers in O(N) running time - 
and without any extra memory. 
The array can contain values: 0, 1 and 2 
(check out the theoretical section for further information).
"""

list_a = [1, 0, 1, 2, 1, 0, 0, 2, 1, 2]

def sort_list(T, mid):
    a = 0
    b = 0
    c = len(T) - 1

    while b <= c:
        if T[b] < mid:
            T[a], T[b] = T[b], T[a]
            a += 1
            b += 1
        
        elif T[b] > mid:
            T[b], T[c] = T[c], T[b]
            c -= 1
        
        else:
            b += 1
    
    return T


print(sort_list(list_a, 1))