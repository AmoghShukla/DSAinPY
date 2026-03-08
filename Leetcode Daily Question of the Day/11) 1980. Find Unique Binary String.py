'''
Question Number : 1980
Title : Find Unique Binary String
Difficulty : Medium

Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. 
If there are multiple answers, you may return any of them.
Example 1:
Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.

'''

def findDifferentBinaryString(nums: list[str]) -> str:
    length = len(nums[0])
    val = 2 ** length

    
    for i in range(val):
        binary_value = bin(i)[2:].zfill(length)
        if str(binary_value) not in nums:
            return str(binary_value)

nums = ["01","10"]
print(findDifferentBinaryString(nums))