# Leetcode Question Number : 42 
# Problem Title : Trapping Rain Water

'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Level : Hard

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

'''

def trap(height: list[int]) -> int:
    left : int = 0
    right :  int = len(height) - 1

    Left_max : list[int] = 0
    Right_max : list[int]= 0

    water: int = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= Left_max:
                Left_max = height[left]
            else:
                water += Left_max - height[left]
            left += 1
        else:
            if height[right] >= Right_max:
                Right_max = height[right]
            else:
                water += Right_max - height[right]
            right -= 1
    return water
