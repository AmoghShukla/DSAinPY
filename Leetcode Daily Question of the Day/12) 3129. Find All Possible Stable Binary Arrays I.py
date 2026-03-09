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
