from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_cnt, one_cnt, two_cnt = 0, 0, 0
        for num in nums:
            if num == 0:
                zero_cnt += 1
            if num == 1:
                one_cnt += 1
            if num == 2:
                two_cnt += 1
        for i in range(len(nums)):
            if zero_cnt != 0:
                nums[i] = 0
                zero_cnt -= 1
            elif one_cnt != 0:
                nums[i] = 1
                one_cnt -= 1
            else:
                nums[i] = 2
                two_cnt -= 1


# One-pass solution using only constant space
class SolutionV2:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0, curr, p2 = 0, 0, len(nums) - 1

        while curr <= p2:
            if nums[curr] == 0:
                tmp = nums[p0]
                nums[p0] = nums[curr]
                nums[curr] = tmp
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                tmp = nums[p2]
                nums[p2] = nums[curr]
                nums[curr] = tmp
                p2 -= 1
            else:
                curr += 1
