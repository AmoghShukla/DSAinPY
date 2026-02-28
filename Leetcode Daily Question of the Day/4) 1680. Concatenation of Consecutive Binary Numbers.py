'''
Given an integer n, return the decimal value of the binary string formed by concatenating 
the binary representations of 1 to n in order, modulo 109 + 7.

Input: n = 12
Output: 505379714
Explanation: The concatenation results in "1101110010111011110001001101010111100".
The decimal value of that is 118505380540.
After modulo 109 + 7, the result is 505379714.
'''

def concatenatedBinary(n: int) -> int:
    string = ""
    for i in range(1, n+1):
        binary = bin(i)[2:]
        string += binary
    integer = int(string, 2)
    if integer > 1000000007:
        return integer % 1000000007
    else:
        return integer

n = 12
print(concatenatedBinary(n))