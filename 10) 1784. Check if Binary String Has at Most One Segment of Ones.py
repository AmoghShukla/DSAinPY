'''
Question No. : 1784
Title : Check if Binary String Has at Most One Segment of Ones
Difficulty : Easy

Given a binary string s, return true if all the 1's in s are grouped into a single segment.
 In other words, return true if s contains at most one contiguous segment of 1's.
Example 1:
Input: s = "1001"
Output: false
Explanation: The 1's are not in a single segment.

'''

def checkOnesSegment(s: str) -> bool:
    seen_zero = False

    for char in s:
        if char == '1' and seen_zero  == True:
            return False
        elif char == '0':
            seen_zero = True
    return True

