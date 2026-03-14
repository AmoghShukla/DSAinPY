'''
Question No. : 1415
Title : The k-th Lexicographical String of All Happy Strings of Length n
Difficulty : Medium
A happy string is a string that:
consists only of letters of the set ['a', 'b', 'c'].
s[i] != s[i + 1] for all values of i from 1 to s.length - 2 (inclusive).
For example, "abc", "ac", "b" and "abcbab" are happy strings and "aa", "baa" and "ababbc" are not happy strings.
Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.
Return the kth string of this list or return an empty string if there are less than k happy strings of length n.
Example 1:
Input: n = 1, k = 3
Output: "c"


'''


def getHappyString(n: int, k : int) -> str:
    res = []

    def backtrack(curr):
        if len(curr) == n:
            res.append(curr)
        
        for char in 'abc':
            if not curr or char != curr[-1]:
                backtrack(curr + char)
        
    backtrack('')
    return res[k-1] if k <= len(res) else ""

n = 3
k = 9
print(getHappyString(n, k))