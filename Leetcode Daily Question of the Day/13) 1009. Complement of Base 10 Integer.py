'''
Question No. : 1009.
Title :  Complement of Base 10 Integer
Difficulty : Easy

Given a base-10 integer n, return the base-10 integer denoting its complement. 
The complement of a base-10 integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

Example 1:
Input: n = 5
Output: 2

'''

def bitwiseComplement(self, n: int) -> int:
    binary = bin(n)[2:]
    complement = ''
    for i in range(len(binary)):
        if binary[i] == '1':
            complement += '0'
        else:
            complement += '1'
    return int(complement, 2)

n = 12
print(bitwiseComplement(n))