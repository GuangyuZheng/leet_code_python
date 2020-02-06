class Solution:
    def myAtoi(self, s: str) -> int:
        SIGNS = ['+', '-']
        NUMS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        MIN = -2**31
        MAX = 2**31 - 1
        result = 0
        signed = 0
        started = False

        for c in s:
            if c != ' ' and (c not in SIGNS) and (c not in NUMS):
                break
            if c == ' ':
                if not started:
                    continue
                else:
                    break
            if c in SIGNS:
                started = True
                if signed != 0:
                    break
                if c == '+':
                    signed = 1
                else:
                    signed = -1
            if c in NUMS:
                started = True
                if signed == 0:
                    signed = 1
                result = result * 10 + int(c)
                if signed * result < MIN:
                    return MIN
                if signed * result > MAX:
                    return MAX
        return signed * result
