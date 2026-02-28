'''
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Level : Easy

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
'''

def MaxSubarray(nums: list[int]):
    current_sum = nums[0]
    total_sum = nums[0]

    temp_start = 0
    start_index = 0
    end_index = 0

    for i in range(1, len(nums)):

        if current_sum + nums[i] < nums[i]:
            current_sum = nums[i]
            temp_start = i
        else:
            current_sum += nums[i]

        if current_sum > total_sum:
            total_sum = current_sum
            start_index = temp_start
            end_index = i

    return nums[start_index:end_index + 1], total_sum
