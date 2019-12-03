from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        def helper(k, n, start):
            if k == 1:
                if n < 10:
                    return [[n]]
                else:
                    return []
            else:
                results = []
                for i in range(start, 10):
                    if i+1 <= n-i:
                        t_results = helper(k-1, n-i, i+1)
                        for res in t_results:
                            results.append([i] + res)
                    else:
                        break
                return results

        return helper(k, n, 1)
