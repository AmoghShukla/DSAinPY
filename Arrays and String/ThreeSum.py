'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

'''
# Bruteforce

def threeSum(nums: list, target: int):
    final_Output: list = []
    length: int = len(nums)
    i: int = 0 
    j: int = i+1
    k: int = length - 1
    while (i <= length - 2 and j <= length-1 and k <= length):
        
        if nums[i] + nums[j] + nums[k] == target:
            final_Output.append([nums[i] , nums[j] , nums[k]])
            if k == length - 1 and j == k-1 and i == j - 1:
                break
            if k == j:
                i += 1
                j = i + 1
                k = length - 1
            else:
                k -= 1
        elif nums[i] + nums[j] + nums[k] != target:
            if k == length - 1 and j == k-1 and i == j - 1:
                break
            if k == j:
                i += 1
                j = i + 1
                k = length - 1
            else:
                k -= 1
    return final_Output

nums = [1,2,3,4,5,6,7,8,9]
print(threeSum(nums, 20))