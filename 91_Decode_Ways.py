class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l = len(s)
        arr = [[-1 for i in range(len(s))] for i in range(len(s))]

        def helper(current, start, end):
            if arr[start][end] != -1:
                return arr[start][end]
            if current[0] == '0':
                for i in range(l):
                    arr[start][i] = 0
                return arr[start][end]
            if len(current) == 1:
                arr[start][end] = 1
                return arr[start][end]
            count = 0
            for i in range(len(current)):
                if i == 0:
                    if current[1:] == '':
                        count += 1
                    else:
                        count += helper(current[1:], start + 1, end)
                if i == 1:
                    if 10 <= ord(current[1]) - ord('0') + 10 * (ord(current[0]) - ord('0')) <= 26:
                        if current[2:] == '':
                            count += 1
                        else:
                            count += helper(current[2:], start + 2, end)
            arr[start][end] = count
            return arr[start][end]

        result = helper(s, 0, len(s) - 1)
        return result


# DP time O(n) space O(n)
class SolutionV2:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if s[0] == '0':
            return 0
        dp = [0 for i in range(len(s)+1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(1, len(s)):
            if s[i] == '0':
                if 1 <= ord(s[i-1])-ord('0') <= 2:
                    dp[i+1] = dp[i-1]
                else:
                    return 0
            else:
                if 10 < (ord(s[i-1])-ord('0'))*10 + (ord(s[i])-ord('0')) <= 26:
                    dp[i+1] = dp[i] + dp[i-1]
                else:
                    dp[i+1] = dp[i]
        return dp[len(s)]


# DP time O(n) space O(1)
class SolutionV3:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if s[0] == '0':
            return 0
        prev = 1  # 上上位
        cur = 1  # 上一位
        for i in range(1, len(s)):
            if s[i] == '0':
                if 1 <= ord(s[i-1])-ord('0') <= 2:
                    tmp = cur
                    cur = prev
                    prev = tmp
                else:
                    return 0
            else:
                if 10 < (ord(s[i-1])-ord('0'))*10 + (ord(s[i])-ord('0')) <= 26:
                    tmp = cur
                    cur = cur + prev
                    prev = tmp
                else:
                    prev = cur
                    cur = cur
        return cur
