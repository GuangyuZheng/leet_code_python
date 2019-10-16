class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s)-1
        while start <= end:
            while (s[start].isalpha() is False) and (s[start].isnumeric() is False):
                start += 1
                if start >= len(s):
                    return True
            while (s[end].isalpha() is False) and (s[end].isnumeric() is False):
                end -= 1
                if end < 0:
                    return True
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True
