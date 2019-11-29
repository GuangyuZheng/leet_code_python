from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        current = nums[0]
        j = 0
        cnt = 0
        for i in range(n):
            if nums[i] == current:
                cnt += 1
            else:
                current = nums[i]
                cnt = 1
            if cnt <= 2:
                if nums[j] != nums[i]:
                    nums[j] = nums[i]
                j += 1
        return j
