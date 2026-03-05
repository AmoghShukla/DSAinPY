"""
Question No. : 1758
Question Title : Minimum Changes To Make Alternating Binary String
Difficulty : Easy

Given a binary string s, return the minimum number of character flips to make s alternating.
The string is called alternating if no two adjacent characters are equal. 
For example, the string "010" is alternating, while the string "0100" is not.
Return the minimum number of operations needed to make s alternating.

"""

def minOperations(s: str) -> int:
    counter1 : int = 0
    counter2 : int = 0
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] != '0':
                counter1 += 1
            if s[i] != '1':
                counter2 += 1
        else:
            if s[i] != '1':
                counter1 += 1
            if s[i] != '0':
                counter2 += 1
        
    return min(counter1, counter2)

s = '10010100'
print(minOperations(s))

        