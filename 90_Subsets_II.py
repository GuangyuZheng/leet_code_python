from typing import List


class Solution:
    def _subsets(self, nums, start, end):
        if start > end:
            return [[]]
        else:
            subsets = []
            tmp_subsets = self._subsets(nums, start + 1, end)
            for t in tmp_subsets:
                subsets.append(t)
                if [nums[start]] + t not in tmp_subsets:
                    subsets.append([nums[start]] + t)
            return subsets

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        return self._subsets(nums, 0, len(nums) - 1)


# backtracking version
class SolutionV2:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums = sorted(nums)

        def backtrack(i, tmp):
            if i == n:
                return
            res.append(tmp)
            for j in range(i+1, n):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                backtrack(j, tmp+[nums[j]])
        backtrack(-1, [])
        return res
