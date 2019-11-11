from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        for i in range(len(nums)):
            if nums[i] > 0:
                return results
            if i > 0 and nums[i] == nums[i-1]:
                continue
            start = i+1
            end = len(nums)-1
            while start < end:
                if nums[i] + nums[start] + nums[end] == 0:
                    results.append([nums[i], nums[start], nums[end]])
                    start += 1
                    while start < end and nums[start] == nums[start-1]:
                        start += 1
                    end -= 1
                    while start < end and nums[end] == nums[end+1]:
                        end -= 1
                elif nums[i] + nums[start] + nums[end] < 0:
                    start += 1
                else:
                    end -= 1
        return results
