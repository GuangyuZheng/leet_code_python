from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 1):
            start = i + 1
            end = len(nums) - 1
            if start == end:
                break

            # If target is less than tmp_min, then the two pointers will always place at start and (start+1) finally
            tmp_min = nums[i] + nums[start] + nums[start + 1]
            if target < tmp_min:
                if abs(tmp_min - target) < abs(result - target):
                    result = tmp_min
                    continue
            # Vise versa
            tmp_max = nums[i] + nums[end - 1] + nums[end]
            if target > tmp_max:
                if abs(tmp_max - target) < abs(result - target):
                    result = tmp_max
                    continue

            while start < end:
                tmp = nums[i] + nums[start] + nums[end]
                if abs(tmp - target) < abs(result - target):
                    result = tmp
                if result == target:
                    return result
                if tmp < target:
                    start += 1
                    # skip repeated numbers
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                else:
                    end -= 1
                    # skip repeated numbers
                    while end > start and nums[end] == nums[end + 1]:
                        end -= 1
        return result

