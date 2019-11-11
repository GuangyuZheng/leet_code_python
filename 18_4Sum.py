from typing import List


class Solution:
    def threeSum(self, nums, target):
        results = []
        for i in range(len(nums) - 2):
            start = i + 1
            end = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # pruning
            if nums[i] + nums[i + 1] + nums[i + 2] > target:
                break
            n = len(nums)
            if nums[i] + nums[n - 1] + nums[n - 2] < target:
                continue

            while start < end:
                s = nums[i] + nums[start] + nums[end]
                if s == target:
                    results.append([nums[i], nums[start], nums[end]])
                    start += 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                    end -= 1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1
                elif s < target:
                    start += 1
                else:
                    end -= 1
        return results

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        results = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # pruning
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            n = len(nums)
            if nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target:
                continue

            ts_results = self.threeSum(nums[i + 1:], target - nums[i])
            if len(ts_results) > 0:
                for r in ts_results:
                    r.append(nums[i])
                    results.append(r)
        return results
