from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        candicates = list(n * '(' + n * ')')
        chosed = [False for i in range(2 * n)]
        results = []

        def check_parentheses(s):
            balance = 0
            for c in s:
                if c == ')':
                    balance -= 1
                if c == '(':
                    balance += 1
                if balance < 0:
                    return False
            return balance == 0

        def helper(result, candicates, chosed):
            if len(result) == 2 * n:
                if result not in results:
                    if check_parentheses(result):
                        results.append(result)
            else:
                l = len(candicates)
                i = 0
                while i < l:
                    if len(result) == 0 and candicates[i] == ')':
                        i += 1
                        continue
                    if len(result) == 2 * n - 1 and candicates[i] == '(':
                        i += 1
                        continue
                    if not chosed[i]:
                        chosed[i] = True
                        helper(result + candicates[i], candicates, chosed)
                        chosed[i] = False
                        while i + 1 < l and candicates[i + 1] == candicates[i]:
                            i += 1
                        i += 1
                    else:
                        i += 1

        helper('', candicates, chosed)
        return results


class SolutionV1:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        results = []

        def helper(result, left, right):
            if left > n or right > n or left < right:
                return
            if len(result) == 2 * n:
                results.append(result)
            else:
                if len(result) != 2 * n - 1:
                    helper(result + '(', left + 1, right)
                if len(result) != 0:
                    helper(result + ')', left, right + 1)

        helper('', 0, 0)
        return results


class SolutionV2:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        results = []

        def helper(result, left, right):
            if len(result) == 2 * n:
                results.append(result)
            else:
                if left < n:
                    helper(result + '(', left + 1, right)
                if left > right:
                    helper(result + ')', left, right + 1)

        helper('', 0, 0)
        return results


class SolutionV3:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return ['']
        ans = []
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans
