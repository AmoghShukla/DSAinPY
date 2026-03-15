'''
Question No. : 1622
Title : Next Greater Element I
Difficulty : Easy

The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
Return an array ans where ans[i] is the next greater element as described above.
Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
'''
# Bruteforce 
# def nextGreaterElement(nums1, nums2):
        # Output = []
        # for i in nums1:
        #     ind = nums2.index(i) + 1
        #     for j in nums2[ind:]:
        #         if j > i:
        #             Output.append(j)
        #             break
        #     else:
        #         Output.append(-1)
        # return Output

# Optimal : Using Stack and Hashmap
def nextGreaterElement(nums1, nums2):
    Stack = []
    Hash = {}

    for num in nums2:
        while Stack and num > Stack[-1]:
            Hash[Stack.pop()] = num
        Stack.append(num)

    while Stack:
        Hash[Stack.pop()] = -1

    return [Hash[num] for num in nums1] 

            

nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]

print(nextGreaterElement(nums1, nums2))