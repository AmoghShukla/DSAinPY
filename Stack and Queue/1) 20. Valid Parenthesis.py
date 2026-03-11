'''
Question : 20
Title : Valid Parenthesis
Difficulty : Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Example 1:
Input: s = "()"
Output: true
'''

class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []
        
        for char in s:
            if char in dictionary:
                top = stack.pop() if stack else '#'
                if dictionary[char] != top:
                    return False
            else:
                stack.append(char)
        return not stack
    
solution = Solution()
print(solution.isValid("()"))