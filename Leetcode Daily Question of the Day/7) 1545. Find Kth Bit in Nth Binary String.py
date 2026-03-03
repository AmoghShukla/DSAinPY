'''
Question No. : 1545
Title : Find Kth Bit in Nth Binary String
Difficulty : Medium

Given two positive integers n and k, the binary string Sn is formed as follows:
S1 = "0"
Si = Si-1 + "1" + reverse(invert(Si-1)) for i > 1
Where + denotes the concatenation operation, reverse(x) returns the reversed string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).
For example, S2 = "0" + "1" + reverse(invert("0")) = "0" + "1" + reverse("1") = "0" + "1" + "1" = "011".
Return the kth bit in Sn. It is guaranteed that k is valid for the given n.

Example 1:
Input: n = 3, k = 1
Output: "0"
Explanation: S3 is "0111001". The 1st bit is "0".
'''

def findKthBit(n: int, k: int) -> str:
    if n < 1:
        return '0'
    bit = "0"
    for i in range(1, n):
        inverted = ''.join("1" if c == "0" else "0" for c in bit)
        bit = bit + "1" + inverted[::-1]
    return bit[k-1]

print(findKthBit(3, 1))