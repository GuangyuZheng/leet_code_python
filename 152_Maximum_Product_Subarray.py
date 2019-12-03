from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        imax = 1
        imin = 1
        result = -10e5
        n = len(nums)
        for i in range(n):
            if nums[i] < 0:
                imax, imin = imin, imax
            imax = max(imax * nums[i], nums[i])
            imin = min(imin * nums[i], nums[i])
            result = max(result, imax)
        return result
