'''
Given an integer array nums, find the subarray with the largest sum, and return its sum.


Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
'''


def MaxSubarray(nums: list[int]) -> int:
    current_sum = nums[0]
    total_sum = nums[0]
    for num in nums:
        current_sum = max(num, current_sum + num)
        total_sum = max(total_sum, current_sum)
    return total_sum


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(MaxSubarray(nums))
