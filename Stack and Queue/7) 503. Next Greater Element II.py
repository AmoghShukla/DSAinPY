'''
Question No. : 1622
Title : Next Greater Element II
Difficulty : Medium
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.
Example 1:
Input: nums = [1,2,1]
Output: [2,-1,2]

'''

def nextGreaterElements(nums):
    n = len(nums)
    Stack = []
    Result = [-1] * n
    
    for i in range(2 * n):
        while Stack and nums[i % n] > nums[Stack[-1]]:
            Result[Stack.pop()] = nums[i % n]
    
        if i < n:
            Stack.append(i)
    
    return Result