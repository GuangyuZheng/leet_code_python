from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        d = 1
        i = len(digits)-1
        while i >= 0:
            num = digits[i] + d
            d = num // 10
            num = num % 10
            digits[i] = num
            i -= 1
        if d != 0:
            digits.insert(0, d)
        return digits
