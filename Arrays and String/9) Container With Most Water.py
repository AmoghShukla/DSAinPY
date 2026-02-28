# Leetcode Question Number : 11
# Title : Container With Most Water
'''
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]). 
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.

Formula : (right - left) * min(list[right], list[left])

Level : Medium

Example:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

'''

def maxArea(height: list[int]) -> int:
    left: int = 0
    right: int = len(height) - 1
    Capacity: list[int] = []
    while( left < right):
        cap: int = (right - left) * min(height[left], height[right])
        Capacity.append(cap)
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return max(Capacity)


height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))
