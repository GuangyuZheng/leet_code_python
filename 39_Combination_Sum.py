from typing import List


class Solution:
    def calculate(self, candidates, current, target):
        results = []
        for i in range(len(candidates)):
            if current + candidates[i] == target:
                results.append([candidates[i]])
            elif current + candidates[i] < target:
                rs = self.calculate(candidates[i:], current+candidates[i], target)
                for r in rs:
                    results.append([candidates[i]] + r)
            else:
                break
        return results

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        results = self.calculate(candidates, 0, target)
        return results


# DP version
class SolutionDP:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        d = {}
        for i in range(1, target + 1):
            d[i] = []

        for n in range(1, target + 1):
            for c in candidates:
                if (n - c) in d:
                    for s in d[n - c]:
                        tmp = sorted(s + [c])
                        if tmp not in d[n]:
                            d[n].append(tmp)
                if c == n:
                    d[n].append([c])
        return d[target]
