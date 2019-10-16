from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []
        results = [[1]]
        prev = [1]
        current = []
        for i in range(1, numRows):
            num = i + 1
            for j in range(num):
                if j == 0 or j == num-1:
                    current.append(1)
                else:
                    current.append(prev[j-1] + prev[j])
            results.append(current)
            prev = current
            current = []
        return results
