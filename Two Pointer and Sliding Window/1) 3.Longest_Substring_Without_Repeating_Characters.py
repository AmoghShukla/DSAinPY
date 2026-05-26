'''
Question No. : 3 
Title : Longest Substring Without Repeating Characters
Difficulty : Medium
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers

'''

class SlidingWindow:

    @staticmethod
    def longest_substring_without_repeating_characters(s : str) -> int:
        left, maxlen = 0 , 0
        window = set()

        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left += 1
            window.add(s[right])
            maxlen = max(maxlen, right-left+1)
        return maxlen
    
print(SlidingWindow.longest_substring_without_repeating_characters("abcabcbb"))