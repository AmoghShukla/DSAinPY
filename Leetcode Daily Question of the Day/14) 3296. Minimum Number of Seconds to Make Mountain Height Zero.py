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