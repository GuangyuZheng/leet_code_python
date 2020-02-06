from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        num2letters = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        results = []
        candidates = []
        for d in digits:
            candidates.append(num2letters[d])

        def helper(pos, result):
            if len(result) == len(digits):
                results.append(result)
            else:
                for ch in candidates[pos]:
                    helper(pos + 1, result + ch)

        helper(0, '')
        return results
