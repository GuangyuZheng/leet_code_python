class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i in range(0, len(s)):
            d = ord(s[i]) - ord('A') + 1
            result = result * 26 + d
        return result
