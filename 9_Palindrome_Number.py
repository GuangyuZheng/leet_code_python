class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reverse = 0
        ori_x = x
        while x > 0:
            digit = x % 10
            x = int(x / 10)
            reverse = reverse * 10 + digit
        if reverse == ori_x:
            return True
        else:
            return False


class SolutionHalfSearch:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x % 10 == 0 and x != 0:
            return False
        reverse = 0
        while reverse < x:
            digit = x % 10
            x = int(x / 10)
            reverse = reverse * 10 + digit
        if reverse == x:
            return True
        elif int(reverse / 10) == x:
            return True
        else:
            return False
