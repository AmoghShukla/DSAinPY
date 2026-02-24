'''
You are given an integer array nums of length n and an integer target.

Return all unique quadruplets [a, b, c, d] such that:

a + b + c + d == target

The indices of a, b, c, d are all distinct

The quadruplets must be returned in lexicographically sorted order

No duplicate quadruplets should appear in the output
'''
# Bruteforce

def Four_Sum(nums, target):
    Output = []
    for i in range(len(nums) - 4):
        for j in range(i+1, len(nums) - 3):
            for k in range(j+1, len(nums) - 2):
                for l in range(k+1, len(nums) - 1):
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        Output.append([nums[i] , nums[j] , nums[k] , nums[l]])
                    else:
                        continue
    return Output
                    

# Better

def Four_Sum(nums: list[int], target: int) -> list[int]:
    Output = []
    
    for i in range(len(nums) - 4):
        for j in range(i+1, len(nums) - 3):
            left = j+1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[j] + nums[left] + nums[right] == target:
                    Output.append([i, j, left, right])
                    Output.append([nums[i] , nums[j] , nums[left] , nums[right]])
                elif left == right - 1:
                    break
                left += 1
    return Output

# def Four_Sum(nums, target):
#     left_first: int = 0
#     right_first: int = right_second - 1
#     left_second: int = left_first + 1
#     right_second: int = len(nums) - 1

#     while left_second < right_first:
#         if nums[left_first] + nums[left_second] + nums[right_first] + nums[right_second] == target:
#             return [nums[left_first] , nums[left_second] , nums[right_first] , nums[right_second]]
#         else:
#             left_second += 1




nums = [7, -3, 2, 9, 1, -6, 4, 8, -2, 5, 3, -1, 6, 0 , 5, 5, 5, 5]
target = 20
print(Four_Sum(nums, target))