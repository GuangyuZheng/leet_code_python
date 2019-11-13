from typing import List


class Solution:
    def calculate(self, candidates, current, target):
        results = []
        for i in range(len(candidates)):
            if i > 0 and candidates[i] == candidates[i-1]:
                continue
            if current + candidates[i] == target:
                results.append([candidates[i]])
            elif current + candidates[i] < target:
                rs = self.calculate(candidates[i+1:], current+candidates[i], target)
                for r in rs:
                    results.append([candidates[i]] + r)
            else:
                break
        return results

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        results = self.calculate(candidates, 0, target)
        return results
