'''
Question No. : 645
Title : Set Mismatch
Difficulty : Easy

You have a set of integers s, which originally contains all the numbers from 1 to n. 
Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
You are given an integer array nums representing the data status of this set after the error.
Find the number that occurs twice and the number that is missing and return them in the form of an array.
Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
Explanation: 2 is the number that occurs twice and 3 is the number that is missing.

'''
def SetMismatch(nums: list) -> list:
    n = len(nums)
    expected_sum = n * (n+1) // 2
    actual_sum = sum(nums)
    New_nums : list = []
    duplicate : int
    missing: int
    for i in nums:
        if i not in New_nums:
            New_nums.append(i)
        if i in New_nums:
            duplicate = i
    missing = expected_sum - (actual_sum - duplicate)

    return [duplicate, missing]

nums = [1,2,2,4]
print(SetMismatch(nums))