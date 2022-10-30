array = [10,3,7,4]

# Indexing start with 0

# Print the first item
print(array[0])

# Print the third item
print(array[2])

# Print the all item
print(array[:])

# Print the first two item
print(array[0:2])

# Print the second to third item
print(array[1:3])

# Print all the item except the last one
print(array[:-1])

# Print all the item except the last two
print(array[:-2])

# we can store string in the same one dim array in python
array = [10,3,'Adam',4]

# Print the third item 'Adam'
print(array[2])

# We can update the array 
array[2] = 'Kelvin'
print(array[:])

array = [10, 42, 55, 4, 2,12]
# Get the maxium item 
# Using linear search which is O(N) running time algorithm

max_num = array[0]
for num in array:
    if max_num < num:
        max_num = num

print(max_num)


# Get the minium item 
# Using linear search which is O(N) running time algorithm

min_num = array[0]
for num in array:
    if min_num > num:
        min_num = num

print(min_num)