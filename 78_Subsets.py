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
                subsets.append([nums[start]] + t)
            return subsets

    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self._subsets(nums, 0, len(nums) - 1)


# bit operation
class SolutionV2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        subsets_l = 1 << l

        subsets = []
        for i in range(subsets_l):
            subset = []
            for j in range(l):
                if (i >> j) & 1 == 1:
                    subset.append(nums[j])
            subsets.append(subset)
        return subsets


# backtracking simple version
class SolutionV3:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(i, tmp):
            if i == n:
                return
            res.append(tmp)
            for j in range(i+1, n):
                backtrack(j, tmp + [nums[j]])

        backtrack(-1, [])
        return res


# iteration version
class SolutionV4:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        n = len(nums)
        for num in nums:
            res = res + [r+[num] for r in res]
        return res
