'''
Question : 3296
Title : Minimum Number of Seconds to Make Mountain Height Zero
Difficulty : Medium
You are given an integer mountainHeight and a 0-indexed integer array workerTimes, where workerTimes[i] is the time taken by the ith worker to reduce the mountain height by 1.
In one second, you can assign any number of workers to work on the mountain simultaneously. A worker can only be assigned to work on the mountain once per second. The height of the mountain is reduced by the number of workers assigned to work on it in that second.
Return the minimum number of seconds needed to reduce the mountain height to 0.

Example 1:
Input: mountainHeight = 3, workerTimes = [1,2,3]
Output: 2
Explanation:
- In the first second, we can assign all three workers to work on the mountain. The height of the mountain is reduced by 3 (1 + 2 + 3) and becomes 0.
Thus, the minimum number of seconds needed to reduce the mountain height to 0 is 1.


'''


class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:

        def can_finish(T):
            total = 0

            for t in workerTimes:
                k = int(((-1 + (1 + 8*T//t)**0.5) // 2))
                total += k

                if total >= mountainHeight:
                    return True

            return False

        left = 1
        right = 10**18

        ans = right

        while left <= right:
            mid = (left + right) // 2

            if can_finish(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans