"""
Given n non-negative integers representing an 
elevation map where the width of each bar is 1. 
Compute how much water it can trap after raining!

Here the elevation map (the input for the algorithm) 
is [4,1,3,1,5] and the output is the total units of trapped 
rain water - which is 7.

"""

# My initial solution not failed...
T = [1, 0, 2, 1, 3, 1, 2, 0, 3] #[2, 1, 3, 1, 4] #[4, 1, 3, 1, 5, 1, 5]
i = 0
k = len(T) - 1
large_num = T[0]
rain_fall = 0

while i <= k:
    if large_num < T[i]:
        large_num = T[i]
    
    rain_fall += large_num - T[i]

    i += 1

print(rain_fall)

def trapping_rain_water(height):
    
    if len(height) < 3:
        return 0 

    left_max = [0 for _ in range(len(height))]
    right_max = [0 for _ in range(len(height))]

    # Get the left max values
    for i in range(1, len(height)):
        left_max[i] = max(left_max[i-1], height[i - 1])

    # Get the right max values
    for i in range(len(height)-2 ,-1, -1):
        right_max[i] = max(right_max[i + 1], height[i + 1])

    tapped = 0

    for i in range(1, len(height) - 1):
        if min(left_max[i], right_max[i]) > height[i]:
            tapped += min(left_max[i], right_max[i]) - height[i]
    
    return tapped

print(trapping_rain_water(T))