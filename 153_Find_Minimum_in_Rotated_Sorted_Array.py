from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n-1
        pivot = 0
        while left <= right:
            pivot = (left+right)//2
            if nums[pivot] > nums[(pivot+1) % n]:
                break
            if nums[pivot] >= nums[0]:
                left = pivot + 1
            else:
                right = pivot - 1
        pivot = (pivot+1) % n
        return nums[pivot]
