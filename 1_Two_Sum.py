from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        afterSub = [target - nums[i] for i in range(len(nums))]
        for i in range(len(nums)):
            if nums[i] in afterSub:
                b = afterSub.index(nums[i])
                if i != b:
                    return [i, b]
