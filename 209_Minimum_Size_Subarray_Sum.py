from typing import List
import bisect


# o(n)
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        tl = 10e9
        ts = 0

        for i in range(n):
            ts += nums[i]
            while ts >= s:
                tl = min(i - start + 1, tl)
                ts -= nums[start]
                start += 1

        return tl if tl != 10e9 else 0


# binary search version o(nlog(n))
class SolutionV2:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        sums = [0 for i in range(n + 1)]
        tl = 10e9
        for i in range(n):
            if i == 0:
                sums[i + 1] = nums[i]
            else:
                sums[i + 1] = nums[i] + sums[i]
        for i in range(1, n):
            t = s + sums[i - 1]
            end = bisect.bisect_left(sums, t, lo=i, hi=len(sums))
            if end != n + 1:
                tl = min(tl, end - i + 1)
        return tl if tl != 10e9 else 0
