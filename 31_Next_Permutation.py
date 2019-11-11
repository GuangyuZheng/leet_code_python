from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        reverse = None
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                reverse = i
                p = len(nums) - 1
                while p >= i and nums[p] <= nums[i - 1]:
                    p -= 1
                tmp = nums[p]
                nums[p] = nums[i - 1]
                nums[i - 1] = tmp
                break
            if reverse is not None:
                break
        if reverse is None:
            nums[:] = nums[::-1]
        else:
            nums[reverse:] = nums[len(nums) - 1:reverse - 1:-1]

    # clean code
    def nextPermutationV2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1
            while j >= i + 1 and nums[j] <= nums[i]:
                j -= 1
            tmp = nums[j]
            nums[j] = nums[i]
            nums[i] = tmp

        if i >= 0:
            nums[i + 1:] = nums[len(nums) - 1:i:-1]
        else:
            nums[:] = nums[::-1]
