'''
Question Number : 448
Title : Find All Numbers Disappeared in an Array
Difficulty : Easy

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Explanation: The numbers 5 and 6 do not appear in the array.

'''


def findDissappearedNums(nums: list) -> list:
    Missing : list = []
    length : int  = len(nums)

    for i in nums:
        idx = abs(i) - 1
        if nums[idx] > 0:
            nums[idx] = -nums[idx]
    
    for i in range(length):
        if nums[i] > 0:
            Missing.append(i+1)
    return Missing

nums = [4,3,2,7,8,2,3,1]
print(findDissappearedNums(nums))