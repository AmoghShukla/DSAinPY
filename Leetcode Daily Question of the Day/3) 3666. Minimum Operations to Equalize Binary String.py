'''
3666. Minimum Operations to Equalize Binary String

You are given a binary string s, and an integer k.
In one operation, you must choose exactly k different indices and flip each '0' to '1' and each '1' to '0'.
Return the minimum number of operations required to make all characters in the string equal to '1'. If it is not possible, return -1.


Input: s = "110", k = 1

Output: 1

Explanation:

There is one '0' in s.
Since k = 1, we can flip it directly in one operation.


'''


class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        ts = [SortedSet() for _ in range(2)]
        for i in range(n + 1):
            ts[i % 2].add(i)
        cnt0 = s.count('0')
        ts[cnt0 % 2].remove(cnt0)
        q = deque([cnt0])
        ans = 0
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == 0:
                    return ans
                l = cur + k - 2 * min(cur, k)
                r = cur + k - 2 * max(k - n + cur, 0)
                t = ts[l % 2]
                j = t.bisect_left(l)
                while j < len(t) and t[j] <= r:
                    q.append(t[j])
                    t.remove(t[j])
            ans += 1
        return -1
    

s = "110"
k = 1

print(Solution().minOperations(s, k))