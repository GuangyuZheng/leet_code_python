class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2 ** 31 - 1
        MIN = - 2 ** 31
        p = 1 if x >= 0 else -1
        result = 0
        x = x if x >= 0 else -x
        while x > 0:
            digit = x % 10
            x = int(x / 10)
            if (result > int(MAX / 10) or (result == int(MAX/10) and digit > 7)) and p == 1:
                return 0
            if (result > int(MAX / 10) or (result == int(MAX/10) and digit > 8)) and p == -1:
                return 0
            result = result * 10 + digit
        result = p * result
        return result
