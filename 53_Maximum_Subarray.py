from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return None
        result = nums[0]
        prev_max = nums[0]
        for i in range(1, len(nums)):
            if prev_max >= 0:
                prev_max = prev_max + nums[i]
            else:
                prev_max = nums[i]
            result = max(result, prev_max)
        return result
