'''You are given an integer array 'nums' of length 'n' and an integer 'target'.

Return all pairs of indices (i, j) such that:

nums[i] + nums[j] == target

i < j

The absolute difference between indices satisfies: |i - j| >= k

Where k is a given positive integer.

If no such pairs exist, return an empty list.

nums = [1, 3, 2, 2, 4]
target = 4

'''
# # Bruteforce
# def twosum(nums: list, target: int):
#     differenc = []
#     for i in range(len(nums)):
#         remaining = target - nums[i]
#         if nums[i] in differenc:
#             index = differenc.index(nums[i])
#             return (nums[i], nums[index])
#         else:
#             differenc.append(remaining)


def twosum(nums: list, target: int):
    seen = {}
    for index, values in enumerate(nums):
        difference = target - values
        if difference in seen:
            return (seen[difference], values)
        seen[values] = index        

nums = [1, 3, 2, 2, 4]
target = 4
print(twosum(nums, target))


