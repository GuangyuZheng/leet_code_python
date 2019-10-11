from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        start, end = 0, len(nums)-1
        mid = -1
        while start <= end:
            mid: int = (start+end)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        if nums[mid] < target:
            return mid + 1
        else:
            return mid
