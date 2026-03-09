'''
Question Number : 3129
Title : Find All Possible Stable Binary Arrays I
Difficulty : Hard

You are given three integers zero, one, and limit. You have zero 0's and one 1's. You want to construct a binary array that contains exactly zero 0's and one 1's, and the number of consecutive 0's or 1's in the array should be at most limit.
Return the number of such binary arrays. Since the answer may be large, return it modulo 10^9 + 7.
Example 1:
Input: zero = 2, one = 1, limit = 2
Output: 3
Explanation: The possible binary arrays are [0,0,1], [0,1,0], and [1,0,0]. Note that [0,0,1] is not a valid array since it contains three consecutive 0's.


'''


from functools import lru_cache

def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
    MOD = 10**9 + 7

    @lru_cache(None)
    def solve(z, o, last):
        if z == 0 and o == 0:
            return 1

        res = 0

        if last != 0:
            for k in range(1, min(limit, z) + 1):
                res += solve(z-k, o, 0)

        if last != 1:
            for k in range(1, min(limit, o) + 1):
                res += solve(z, o-k, 1)

        return res % MOD

    return solve(zero, one, -1)
