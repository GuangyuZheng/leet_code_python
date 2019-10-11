from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        total_len = len(nums)
        remove_num = 0
        current = 0
        while current < total_len - remove_num:
            if nums[current] == val:
                nums[current] = nums[total_len - remove_num - 1]
                remove_num += 1
            else:
                current += 1
        return total_len - remove_num
